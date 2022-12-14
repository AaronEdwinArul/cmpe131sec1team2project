from app import myapp_obj, db
from flask import render_template, redirect, url_for, request
from app.models import User, Post, Likes, Follows
from app.forms import LoginForm, LogoutForm, SignupForm, PostForm, LikeForm, SearchForm, SearchResult, FollowForm, unfollowForm, unfollowForm2, ProfileEditForm, Delete_Account_Form

#importing spanish forms
from app.forms import Delete_Account_Form_Spanish, ProfileEditForm_Spanish
from app.forms import SLoginForm, SSignupForm, SPostForm, SSearchForm, SSearchResult, SFollowForm, SunfollowForm, SunfollowForm2

from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required

@myapp_obj.route('/')   #routes to the base page
def base():
    return render_template("base.html")

@myapp_obj.route('/login', methods=['POST', 'GET']) #routes to login page
def login():
    current_form = LoginForm()
    errorMessage = ''
    if current_form.validate_on_submit():   #checks once submit button is pressed
        users = User.query.all()  
        for user in users:
            if user.username == current_form.username.data: #checks if username is in database
                if check_password_hash(user.password,current_form.password.data): #checks if password is correct
                    if current_form.remember_me.data:
                        login_user(user, remember=True)
                    login_user(user, remember=current_form.remember_me.data) #logs in user
                    return redirect('/home')
            else:
                errorMessage = 'Invalid Username or Password'
    return render_template('login.html', form=current_form, error=errorMessage)

@myapp_obj.route('/logout') #logs out and routes to base page
@login_required
def logout():
    current_form = LogoutForm()
    logout_user()
    return render_template('base.html', form=current_form)

@myapp_obj.route('/delete_account', methods = ['POST', 'GET'])  #deletes account and routes to signup page
@login_required
def delete_account():

    current_form = Delete_Account_Form()
    user = User.query.filter_by(username=current_user.username).first()

    if current_form.validate_on_submit() and check_password_hash(user.password,current_form.password.data): #checking if password is correct
                
        user_posts = Post.query.filter_by(user_id = current_user.id).all() #collecting all posts, likes, and follows of user
        user_likes = Likes.query.filter_by(liker = current_user.id).all()
        user_follows = Follows.query.filter_by(follower = current_user.username).all() 
        user_followed = Follows.query.filter_by(followee = current_user.username).all()
                    
        for u in user_posts:        #deleteing all posts, likes, and follows of user
            db.session.delete(u)
        for u in user_likes:
            db.session.delete(u)
        for u in user_follows:
            db.session.delete(u) 
        for u in user_followed:
            db.session.delete(u)
                    
        db.session.delete(user) #deleting user
        db.session.commit()
        return redirect('/signup')
            
    return render_template('delete_account.html', form = current_form)

@myapp_obj.route('/home', methods=['POST', 'GET'])  #routes to home page
@login_required
def home():
    follows = Follows.query.filter_by(follower=current_user.username)    #finds all users that current user is following
    followedids = []
    posts = []      #list of dictionaries
    for i in follows:
        followedids.append(User.query.filter_by(username = i.followee).first().id)
    for userid in followedids:
        post = Post.query.filter_by(user_id = userid)   #query all posts   
        for i in post:              #iterate through all queries
            text = {}               #create a dictionary of 'body':'text', etc.
            text['body'] = i.post
            text['link'] = i.link
            text['id'] = i.id
            text['author'] = i.get_author(i.user_id)
            text['date'] = i.date
            
            likecheck = Likes.query.filter_by(post = i.id)  # for each like object for this post,
            count = 0           
            text['likestatus'] = "Like" 
            bool = False        
            for like in likecheck:          
                count += 1              # count how many 'likers' there are
                if current_user.id == int(like.liker):  # if the current logged user is in the table, display unlike button rather than like
                    bool = True
            if bool == True:
                text['likestatus'] = "Unlike"
            text['likes'] = count       # save count to display likes for each post

            posts.append(text)      #add individual dictionaries to array
            
            #create a submit form for each button
            postbutton = LikeForm(prefix = str(i.id))   
            if bool == True:            #check likestatus confirmed previously
                postbutton.submit.label.text = 'Unlike'
            text['button'] = postbutton #add submit button to dictionary
            
        for i in posts: #when returning page read button presses
            if i['button'].validate_on_submit():    #check validation for each button
                if i['likestatus'] == 'Like':   #if unliked
                    #add like to sb
                    addlike = Likes()               #create like object
                    addlike.liker = current_user.id #current user is the liker
                    addlike.post = i['id']          #button and corresponding post
                    db.session.add(addlike)
                    db.session.commit()
                else:   #else the post is liked
                    #remove like from db
                    removelike = Likes.query.filter_by(post = i['id'])  #filter all likers of target post
                    for l in removelike:            #iterate through each liker
                        if int(current_user.id) == int(l.liker):    #when current user id is found as a liker,
                            db.session.delete(l)                    #delete that object
                            db.session.commit()
                            
                return redirect('/home')    #refresh page to update like status
        
    # /feed page will display each body text and have access to the link to show the image
    return render_template('home.html', posts = posts)

@myapp_obj.route('/signup', methods = ['POST','GET'])   #routes to signup page
def create():
    current_form = SignupForm()
    errorMessage = ''
    if current_form.validate_on_submit():   
        if not(validPassword(current_form.password.data)):
            errorMessage = 'Password must be longer than 8 characters'
        elif not(validEmail(current_form.email.data)):
            errorMessage = 'Invalid email address (must have domain .com,.org,.edu)'
        else:
            user = User()
            user.first = current_form.first.data
            user.last = current_form.last.data
            user.email = current_form.email.data
            user.username = current_form.username.data
            user.password = generate_password_hash(current_form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect('/login')        #redirect to login page when implemented

    return render_template('signup.html',form=current_form, error = errorMessage)

@myapp_obj.route('/post', methods = ['POST','GET'])   #routes to post page
@login_required
def post():
    current_form = PostForm()
    if current_form.validate_on_submit():
        post = Post()
        post.post = current_form.text.data  #save body text to db
        post.link = current_form.link.data  #save image url to db
        post.user_id = current_user.id      #save current user's id to track poster
        today = date.today()
        post.date = str(today).replace('-','')      #date of post stored as yyyymmdd
        with myapp_obj.app_context():       #add object to db
            db.session.add(post)
            db.session.commit()
        return redirect('/feed')        #redirects to home after posting, will show post
    return render_template('post.html', form = current_form)

@myapp_obj.route('/feed', methods = ['POST','GET'])  #routes to feed page
@login_required
def view():
    #create form for redirecting to another page
    post = Post.query.all()     #query all posts
    posts = []                  #list of dictionaries
    for i in post:              #iterate through all queries
        text = {}               #create a dictionary of 'body':'text', etc.
        text['body'] = i.post
        text['link'] = i.link
        text['id'] = i.id
        text['author'] = i.get_author(i.user_id)
        text['date'] = i.date
        
        likecheck = Likes.query.filter_by(post = i.id)  # for each like object for this post,
        count = 0           
        text['likestatus'] = "Like" 
        bool = False        
        for like in likecheck:          
            count += 1              # count how many 'likers' there are
            if current_user.id == int(like.liker):  # if the current logged user is in the table, display unlike button rather than like
                bool = True
        if bool == True:
            text['likestatus'] = "Unlike"
        text['likes'] = count       # save count to display likes for each post

        posts.append(text)      #add individual dictionaries to array
        
        #create a submit form for each button
        postbutton = LikeForm(prefix = str(i.id))   
        if bool == True:            #check likestatus confirmed previously
            postbutton.submit.label.text = 'Unlike'
        text['button'] = postbutton #add submit button to dictionary
        
    for i in posts: #when returning page read button presses
        if i['button'].validate_on_submit():    #check validation for each button
            if i['likestatus'] == 'Like':   #if unliked
                #add like to sb
                addlike = Likes()               #create like object
                addlike.liker = current_user.id #current user is the liker
                addlike.post = i['id']          #button and corresponding post
                db.session.add(addlike)
                db.session.commit()
            else:   #else the post is liked
                #remove like from db
                removelike = Likes.query.filter_by(post = i['id'])  #filter all likers of target post
                for l in removelike:            #iterate through each liker
                    if int(current_user.id) == int(l.liker):    #when current user id is found as a liker,
                        db.session.delete(l)                    #delete that object
                        db.session.commit()
                        
            return redirect('/feed')
        
    # /feed page will display each body text and have access to the link to show the image
    return render_template('feed.html', posts = posts)

@myapp_obj.route('/search', methods = ['POST','GET'])   #routes to search page
@login_required
def search():
    current_form = SearchForm()
    errormessage = ''
    if request.method == "GET": #before anything is entered show basic search html page
        return render_template('search.html', form = current_form)
    if request.method == "POST":    #after information is entered
        searched = request.form["username"] #finds what was entered in the search bar
        users = User.query.all()
        for user in users:
            if user.username == searched:   #if the searched username is found in the database
                data.searchedUser=searched   #store searched username             
                return redirect(url_for("user", usr=searched))  #redirect to user page
            else: 
                errormessage = 'User not found'  
    return render_template('search.html', error = errormessage)

@myapp_obj.route('/user/<usr>', methods = ['POST','GET'])   #usr url is the searched username
def user(usr):
    current_form = SearchResult()
    return render_template('searchResult.html', form=current_form, username=usr)

@myapp_obj.route('/user-profile', methods=['GET', 'POST'])  #routes to searched user profile page
def user_profile():
    current_form = FollowForm()
    errormessage = ''
    users = User.query.filter_by(username=data.searchedUser)
    follow = Follows.query.filter_by(follower=current_user.username,followee=data.searchedUser) #filters if current user is following searched user
    for follow in follow:   #if current user is following searched user redirect to next page to unfollow
        return redirect('/user-profile1')
    else:
        for user in users:
            if request.method == "GET": #base html page for user profile
                name=user.username
                first=user.first
                last=user.last
                email=user.email
            if request.method == "POST":    #if follow button is clicked
                follow = Follows()
                search = data.searchedUser
                follow.follower = current_user.username
                follow.followee = search
                db.session.add(follow)  #store follower and followee into db
                db.session.commit()
                return redirect('/user-profile1')
    return render_template('user-profile.html', form=current_form, username=name, first=first, last=last, email=email, error=errormessage)

@myapp_obj.route('/user-profile1', methods=['GET', 'POST']) #routes to searched user profile1 page
def user_profile1():
    current_form = unfollowForm()
    errormessage = ''
    users = User.query.filter_by(username=data.searchedUser)
    for user in users:
        if request.method == "GET": #base html page for user profile1
            name=user.username
            first=user.first
            last=user.last
            email=user.email
            errormessage = 'You are following ' + data.searchedUser
        if request.method == "POST":
            follow = Follows.query.filter_by(follower=current_user.username, followee=data.searchedUser)    #finds the follow object
            for follow in follow:   #if current user is following searched user
                db.session.delete(follow)   #delete current user and searched user from db
                db.session.commit()
                return redirect('/user-profile2')
    return render_template('user-profile1.html', form=current_form, username=name, first=first, last=last, email=email, error=errormessage)

@myapp_obj.route('/user-profile2', methods=['GET', 'POST']) #routes to searched user profile2 page
def user_profile2():
    current_form = unfollowForm2()
    errormessage = ''
    users = User.query.filter_by(username=data.searchedUser)
    for user in users:
        if request.method == "GET": #base html page for user profile2
            name=user.username
            first=user.first
            last=user.last
            email=user.email
            errormessage = 'You are no longer following ' + data.searchedUser   #special implementation so that user cannot spam follow/unfollow button
        if request.method == "POST":
            return redirect('/home')    #can only go to home page after unfollowing to prevent spam clicking
    return render_template('user-profile2.html', form=current_form, username=name, first=first, last=last, email=email, error=errormessage)

@myapp_obj.route('/followers', methods=['GET', 'POST']) #routes to followers page
@login_required
def followers():
    errormessage = ''  
    follow = Follows.query.filter_by(followee=current_user.username)    #finds all users that are following current user
    for follow in follow:
        errormessage += follow.follower + '\n' #displays everyone following current user
    return render_template('followers.html', error=errormessage)

@myapp_obj.route('/profile')    #routes to current user profile page
@login_required
def test12():
    name= current_user.username
    bio = current_user.bio
    location = current_user.location
    email = current_user.email
    password = current_user.password
    dob = current_user.dob
    return render_template("profile.html", username=name, bio=bio, location=location, email=email, password=password, dob=dob)

@myapp_obj.route('/profile_edit', methods = ['POST','GET']) #routes to profile edit page
@login_required
def profile_edit():
    current_form = ProfileEditForm()
    errorMessage = ''
    user = User.query.filter_by(username=current_user.username).first() #retreiving current user
    if current_form.validate_on_submit():

        if len(current_form.bio.data) > 200:
            errorMessage = 'Bio is too long! (Max characters is 200)'
           
        else:
            user.dob = current_form.dob.data            #updating dob, location, and bio of user
            user.location = current_form.location.data
            user.bio = current_form.bio.data
            db.session.add(user)
            db.session.commit()
            return redirect('/profile') #redirects to profile after submitting form, will show updated bio, dob, location
    return render_template('profile_edit.html', form=current_form, error = errorMessage)


# helper functions

class DataStore():  #class to store searched user
    searchedUser = None

data = DataStore()

def validPassword(string):  #checks if password is valid
    if len(string) < 8:
        return False
    return True

def validEmail(string): #checks if email is valid
    boolAddress = False
    boolDomain = False
    for i in string:
        if i == '@':
            boolAddress = True
    if (string[len(string)-4:len(string)] == '.com') or (string[len(string)-4:len(string)]) == '.org' or (string[len(string)-4:len(string)] == '.edu'):
        boolDomain = True
    return boolAddress and boolDomain


#SPANISH VERSION

@myapp_obj.route('/profile_spanish')
@login_required
def Stest():
    name=current_user.username
    bio =current_user.bio
    location= current_user.location
    email=current_user.email
    password=current_user.password
    dob=current_user.dob
    return render_template("profile_spanish.html", username=name, bio=bio, location=location, email=email, password=password, dob=dob)

@myapp_obj.route('/Slogin', methods=['POST', 'GET'])
def Slogin():
    current_form = SLoginForm()
    errorMessage = ''
    if current_form.validate_on_submit():   #checks once submit button is pressed
        users = User.query.all()  
        for user in users:
            if user.username == current_form.username.data: #checks if username is in database
                if check_password_hash(user.password,current_form.password.data): #checks if password is correct
                    if current_form.remember_me.data:
                        login_user(user, remember=True)
                    login_user(user, remember=current_form.remember_me.data) #logs in user
                    return redirect('/Shome')
            else:
                errorMessage = 'Usuario o contraseña invalido'
    return render_template('Slogin.html', form=current_form, error=errorMessage)

@myapp_obj.route('/Shome', methods=['POST', 'GET'])
@login_required
def Shome():
    follows = Follows.query.filter_by(follower=current_user.username)    #finds all users that current user is following
    followedids = []
    posts = []      #list of dictionaries
    for i in follows:
        followedids.append(User.query.filter_by(username = i.followee).first().id)
    for userid in followedids:
        post = Post.query.filter_by(user_id = userid)   #query all posts   
        for i in post:              #iterate through all queries
            text = {}               #create a dictionary of 'body':'text', etc.
            text['body'] = i.post
            text['link'] = i.link
            text['id'] = i.id
            text['author'] = i.get_author(i.user_id)
            text['date'] = i.date
            
            likecheck = Likes.query.filter_by(post = i.id)  # for each like object for this post,
            count = 0           
            text['likestatus'] = "Like" 
            bool = False        
            for like in likecheck:          
                count += 1              # count how many 'likers' there are
                if current_user.id == int(like.liker):  # if the current logged user is in the table, display unlike button rather than like
                    bool = True
            if bool == True:
                text['likestatus'] = "Unlike"
            text['likes'] = count       # save count to display likes for each post

            posts.append(text)      #add individual dictionaries to array
            
            #create a submit form for each button
            postbutton = LikeForm(prefix = str(i.id)) 
            postbutton.submit.label.text = 'Me gusta'  
            if bool == True:            #check likestatus confirmed previously
                postbutton.submit.label.text = 'Hasta saber'
            text['button'] = postbutton #add submit button to dictionary
            
        for i in posts: #when returning page read button presses
            if i['button'].validate_on_submit():    #check validation for each button
                if i['likestatus'] == 'Like':   #if unliked
                    #add like to sb
                    addlike = Likes()               #create like object
                    addlike.liker = current_user.id #current user is the liker
                    addlike.post = i['id']          #button and corresponding post
                    db.session.add(addlike)
                    db.session.commit()
                else:   #else the post is liked
                    #remove like from db
                    removelike = Likes.query.filter_by(post = i['id'])  #filter all likers of target post
                    for l in removelike:            #iterate through each liker
                        if int(current_user.id) == int(l.liker):    #when current user id is found as a liker,
                            db.session.delete(l)                    #delete that object
                            db.session.commit()
                            
                return redirect('/Shome')    #refresh page to update like status
        
    # /feed page will display each body text and have access to the link to show the image
    return render_template('Shome.html', posts = posts)

@myapp_obj.route('/Ssignup', methods = ['POST','GET'])
def Screate():
    current_form = SSignupForm()
    errorMessage = ''
    if current_form.validate_on_submit():   
        if not(validPassword(current_form.password.data)):
            errorMessage = 'La contraseña debe tener más de 8 caracteres'
        elif not(validEmail(current_form.email.data)):
            errorMessage = 'Dirección de correo electrónico no válida (debe tener dominio .com, .org, .edu)'
        else:
            user = User()
            user.first = current_form.first.data
            user.last = current_form.last.data
            user.email = current_form.email.data
            user.username = current_form.username.data
            user.password = generate_password_hash(current_form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect('/Slogin')        #redirect to login page when implemented

    return render_template('Ssignup.html',form=current_form, error = errorMessage)

@myapp_obj.route('/Spost', methods = ['POST','GET'])
@login_required
def Spost():
    error = ''
    current_form = SPostForm()
    if current_form.validate_on_submit():
        if len(current_form.text.data) > 500:
            error = '¡La publicación es demasiado larga! (El máximo de caracteres es 500)'
        else:
            post = Post()
            post.post = current_form.text.data  #save body text to db
            post.link = current_form.link.data  #save image url to db
            post.user_id = current_user.id      #save current user's id to track poster
            today = date.today()
            post.date = str(today).replace('-','')      #date of post stored as yyyymmdd
            with myapp_obj.app_context():       #add object to db
                db.session.add(post)
                db.session.commit()
            return redirect('/Sfeed')        #redirects to home after posting, will show post
    return render_template('Spost.html', form = current_form, error = error)

@myapp_obj.route('/Sfeed', methods = ['POST','GET'])
def Sview():
#create form for redirecting to another page
    post = Post.query.all()     #query all posts
    posts = []                  #list of dictionaries
    for i in post:              #iterate through all queries
        text = {}               #create a dictionary of 'body':'text', etc.
        text['body'] = i.post
        text['link'] = i.link
        text['id'] = i.id
        text['author'] = i.get_author(i.user_id)
        text['date'] = i.date
        
        likecheck = Likes.query.filter_by(post = i.id)  # for each like object for this post,
        count = 0           
        text['likestatus'] = "Like" 
        bool = False        
        for like in likecheck:          
            count += 1              # count how many 'likers' there are
            if current_user.id == int(like.liker):  # if the current logged user is in the table, display unlike button rather than like
                bool = True
        if bool == True:
            text['likestatus'] = "Unlike"
        text['likes'] = count       # save count to display likes for each post

        posts.append(text)      #add individual dictionaries to array
        
        #create a submit form for each button
        postbutton = LikeForm(prefix = str(i.id))   
        postbutton.submit.label.text = 'Me gusta'
        if bool == True:            #check likestatus confirmed previously
            postbutton.submit.label.text = 'Hasta saber'
        text['button'] = postbutton #add submit button to dictionary
        
    for i in posts: #when returning page read button presses
        if i['button'].validate_on_submit():    #check validation for each button
            if i['likestatus'] == 'Like':   #if unliked
                #add like to sb
                addlike = Likes()               #create like object
                addlike.liker = current_user.id #current user is the liker
                addlike.post = i['id']          #button and corresponding post
                db.session.add(addlike)
                db.session.commit()
            else:   #else the post is liked
                #remove like from db
                removelike = Likes.query.filter_by(post = i['id'])  #filter all likers of target post
                for l in removelike:            #iterate through each liker
                    if int(current_user.id) == int(l.liker):    #when current user id is found as a liker,
                        db.session.delete(l)                    #delete that object
                        db.session.commit()
                        
            return redirect('/Sfeed')
        
    # /feed page will display each body text and have access to the link to show the image
    return render_template('Sfeed.html', posts = posts)

@myapp_obj.route('/Ssearch', methods = ['POST','GET'])
@login_required
def Ssearch():
    current_form = SSearchForm()
    errormessage = ''
    if request.method == "GET": #before anything is entered show basic search html page
        return render_template('Ssearch.html', form = current_form)
    if request.method == "POST":    #after information is entered
        searched = request.form["username"] #finds what was entered in the search bar
        users = User.query.all()
        for user in users:
            if user.username == searched:   #if the searched username is found in the database
                data.searchedUser=searched   #store searched username             
                return redirect(url_for("Suser", usr=searched))  #redirect to user page
            else: 
                errormessage = 'Usuario no encontrado'  
    return render_template('Ssearch.html', error = errormessage)

@myapp_obj.route('/Suser/<usr>', methods = ['POST','GET'])   #usr url is the searched username
def Suser(usr):
    current_form = SSearchResult()
    #if request.method == "POST":
        #return redirect('user-profile')
    return render_template('SsearchResult.html', form=current_form, username=usr)

@myapp_obj.route('/Suser-profile', methods=['GET', 'POST'])
def Suser_profile():
    current_form = SFollowForm()
    errormessage = ''
    users = User.query.filter_by(username=data.searchedUser)
    follow = Follows.query.filter_by(follower=current_user.username,followee=data.searchedUser) #filters if current user is following searched user
    for follow in follow:   #if current user is following searched user redirect to next page to unfollow
        return redirect('/Suser-profile1')
    else:
        for user in users:
            if request.method == "GET": #base html page for user profile
                name=user.username
                first=user.first
                last=user.last
                email=user.email
            if request.method == "POST":    #if follow button is clicked
                follow = Follows()
                search = data.searchedUser
                follow.follower = current_user.username
                follow.followee = search
                db.session.add(follow)  #store follower and followee into db
                db.session.commit()
                return redirect('/Suser-profile1')
    return render_template('Suser-profile.html', form=current_form, username=name, first=first, last=last, email=email, error=errormessage)

@myapp_obj.route('/Suser-profile1', methods=['GET', 'POST'])
def Suser_profile1():
    current_form = SunfollowForm()
    errormessage = ''
    users = User.query.filter_by(username=data.searchedUser)
    for user in users:
        if request.method == "GET": #base html page for user profile1
            name=user.username
            first=user.first
            last=user.last
            email=user.email
            errormessage = 'Usted esta siguiendo ' + data.searchedUser
        if request.method == "POST":
            follow = Follows.query.filter_by(follower=current_user.username, followee=data.searchedUser)    #finds the follow object
            for follow in follow:   #if current user is following searched user
                db.session.delete(follow)   #delete current user and searched user from db
                db.session.commit()
                return redirect('/Suser-profile2')
    return render_template('Suser-profile1.html', form=current_form, username=name, first=first, last=last, email=email, error=errormessage)

@myapp_obj.route('/Suser-profile2', methods=['GET', 'POST'])
def Suser_profile2():
    current_form = SunfollowForm2()
    errormessage = ''
    users = User.query.filter_by(username=data.searchedUser)
    for user in users:
        if request.method == "GET": #base html page for user profile2
            name=user.username
            first=user.first
            last=user.last
            email=user.email
            errormessage = 'ya no sigues ' + data.searchedUser   #special implementation so that user cannot spam follow/unfollow button
        if request.method == "POST":
            return redirect('/Shome')    #can only go to home page after unfollowing to prevent spam clicking
    return render_template('Suser-profile2.html', form=current_form, username=name, first=first, last=last, email=email, error=errormessage)

@myapp_obj.route('/Sfollowers', methods=['GET', 'POST'])
@login_required
def Sfollowers():
    errormessage = ''  
    follow = Follows.query.filter_by(followee=current_user.username)    #finds all users that are following current user
    for follow in follow:
        errormessage += follow.follower + '\n' #displays everyone following current user
        #s=errormessage.replace("\n","<br/>")
        #errormessage = s
    #else:
        #errormessage = 'You have no followers'
        #print(follow.follower)
    return render_template('Sfollowers.html', error=errormessage)

@myapp_obj.route('/profile_spanish', methods = ['POST', 'GET'])
@login_required
def profile_spanish():
    return render_template('profile_spanish.html')

@myapp_obj.route('/profile_edit_spanish', methods = ['POST','GET'])
@login_required
def profile_edit_spanish():
    current_form = ProfileEditForm_Spanish()
    errorMessage = ''
    user = User.query.filter_by(username=current_user.username).first() #retreiving current user
    if current_form.validate_on_submit():

        if len(current_form.bio.data) > 200:
            errorMessage = '¡La biografía es demasiado larga! (El máximo de caracteres es 200)'
           
        else:
            user.dob = current_form.dob.data            #updating dob, location, and bio of user
            user.location = current_form.location.data
            user.bio = current_form.bio.data
            db.session.add(user)
            db.session.commit()
            return redirect('/profile_spanish') #redirects to profile after submitting form, will show updated bio, dob, location
    return render_template('profile_edit_spanish.html', form=current_form, error = errorMessage)

@myapp_obj.route('/delete_account_spanish', methods = ['GET', 'POST'])
@login_required
def delete_account_spanish():
    current_form = Delete_Account_Form_Spanish()
    user = User.query.filter_by(username = current_user.username).first()

    if current_form.validate_on_submit() and check_password_hash(user.password,current_form.password.data): #checking if password is correct

        user_posts = Post.query.filter_by(user_id = current_user.id).all() #collecting all posts, likes, and follows of user
        user_likes = Likes.query.filter_by(liker = current_user.id).all()
        user_follows = Follows.query.filter_by(follower = current_user.id).all()   
                  
        for u in user_posts:
                db.session.delete(u)
        for u in user_likes:
                db.session.delete(u)
        for u in user_follows:
                db.session.delete(u)
                    
        db.session.delete(user)   
        db.session.commit()
        return redirect('/signup')

    return render_template('delete_account_spanish.html', form = current_form)
