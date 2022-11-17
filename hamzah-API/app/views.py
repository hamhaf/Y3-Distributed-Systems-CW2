# from flask import render_template, flash, request, redirect, url_for, g, session
# from app import app, models, db, admin
# from .forms import UserForm, BookForm, SUForm
# from flask_admin.contrib.sqla import ModelView
# from sqlalchemy import exists
# import os,time
# from datetime import date
# from werkzeug.utils import secure_filename

# admin.add_view(ModelView(models.User, db.session))
# admin.add_view(ModelView(models.Has_Read, db.session))
# admin.add_view(ModelView(models.Book, db.session))

# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# @app.before_request
# def before_request():
# 	if 'user_id' in session:
# 		user = models.User.query.filter_by(id = session['user_id']).first()
# 		g.user = user


# @app.route('/')
# def index():#the home page will be the login/sign up page
# 	if 'user_id' in session:
# 		app.logger.info('%s: user \"%s\" has logged out',time.asctime(),g.user.username)
# 	#this should pop the session when a user logs out/returns to login page
# 	session.pop('user_id',None)
# 	form = UserForm()
# 	return render_template('home.html', title='Sign in', form=form)#renders the home.html template passing the appropriate variabels

# @app.route('/login', methods=['POST','GET'])
# def login():
# 	form = UserForm()
# 	user = models.User(username=form.username.data, password=form.password.data)
# 	temp = models.User.query.filter_by(username = user.username).first()
# 	if temp != None:
# 		if temp.password == user.password:
# 			# correct login details
# 			#session to store the current logged in user's username
# 			session['user_id'] = temp.id
# 			app.logger.info('%s: \"%s\" logged in',time.asctime(),temp.username)
# 			return redirect(url_for('profile'))
# 		else:
# 			app.logger.info('%s: failed attempt to log in',time.asctime())
# 			flash('incorrect username/password','error')
# 	else:
# 		app.logger.info('%s: failed attempt to log in',time.asctime())
# 		flash('incorrect username/password','error')
# 	return redirect(url_for('index'))

# @app.route('/signup')
# def signup():
# 	form = SUForm()
# 	return render_template('signup.html', title='Sign up', form=form)

# @app.route('/create', methods=['POST'])
# def create():
# 	form = SUForm()
# 	user = models.User(username=form.username.data, password=form.password.data)
# 	temp = models.User.query.filter_by(username = user.username).first()
# 	#print("user.username =" , user.username)
# 	if temp == None:# unique username
# 		if form.validate_on_submit():#this line just makes sure the user is inputting valid data and that it is a POST request
# 			#if form.password.data == form.password2.data: #user has validated their pass
# 			db.session.add(user)#adds the object as an entry to the database
# 			db.session.commit()#saves the changes made to the database
# 			flash('account created','success')
# 			app.logger.info('%s: account created { username = \"%s\" || password = \"%s\" }',time.asctime(),user.username,user.password)
# 			return redirect(url_for('index'))
# 	flash('try again','error')
# 	return redirect(url_for('signup'))

# @app.route('/newpassword')
# def newpassword():
# 	if 'user_id' in session:
# 		form = SUForm()
# 		return render_template('newpassword.html', title="Change password", form=form)
# 	else:
# 		flash('you must be logged in to access this page','error')
# 		return redirect(url_for('index'))

# @app.route('/changepassword', methods=['POST'])
# def changepassword():
# 	form = SUForm()
# 	password = form.password.data
# 	password2 = form.password2.data
# 	if password == password2:
# 		temp = models.User.query.filter_by(id = g.user.id).first()
# 		temp.password = password
# 		db.session.commit()
# 		flash('password changed.','success')
# 		app.logger.info('%s: user \"%s\" changed their password to \"%s\" }',time.asctime(),temp.username,temp.password)
# 		return redirect(url_for('index'))
# 	else:
# 		flash('try again.','error')
# 		return redirect(url_for('newpassword'))

# @app.route('/profile')
# def profile():
# 	'''
# 	#querying the has_read table
# 	readquery = g.user.books
# 	for book in readquery:
# 		#print("bookid =",book.bookid)
# 	'''
# 	if 'user_id' in session:
# 		# make the function get the user's name and display it as the page title
# 		return render_template('profile.html', title=str(g.user.username)+"\'s profile")
# 	else:
# 		flash('you must be logged in to access this page','error')
# 		return redirect(url_for('index'))


# @app.route('/library')
# def library():
# 	books = models.Book.query.all()
# 	if 'user_id' in session:
# 		# make the function get the user's name and display it as the page title
# 		return render_template('library.html', title="The Library", books=books)
# 	else:
# 		flash('you must be logged in to access this page','error')
# 		return redirect(url_for('index'))


# @app.route('/newbook')
# def newbook():
# 	form = BookForm()
# 	if 'user_id' in session:
# 		# make the function get the user's name and display it as the page title
# 		return render_template('newbook.html',title="New book", form=form)
# 	else:
# 		flash('you must be logged in to access this page','error')
# 		return redirect(url_for('index'))

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/addbook', methods=['GET','POST'])
# def addbook():
# 	UPLOAD_FOLDER = 'static/img'
# 	if request.method == 'POST':
# 		file = request.files['file']
# 		filename = secure_filename(file.filename)
# 		#concatenate relative path to images folder and filename
# 		folder = app.root_path +'/'+ str(UPLOAD_FOLDER)
# 		message = "with the default image as it's cover"
# 		if 'file' not in request.files:
# 			filepath = os.path.join(folder, "default.png")
# 			relativepath = UPLOAD_FOLDER + '/' + "default.png"
#         # if user does not select file, browser also
#         # submit an empty part without filename
# 		elif file.filename == '':
# 			filepath = os.path.join(folder, "default.png")
# 			relativepath = UPLOAD_FOLDER + '/' + "default.png"
# 		if file and allowed_file(file.filename):
# 			filepath = os.path.join(folder, filename)
# 			relativepath = UPLOAD_FOLDER + '/' + str(filename)
# 			message = "with a front cover provided by the user"
# 			file.save(filepath)
# 		form = BookForm()
# 		book = models.Book(title=form.title.data , author=form.author.data ,
# 		date=form.date.data , blurb=form.blurb.data , filepath=relativepath )
# 		#check if the book already exists
# 		temp = models.Book.query.filter_by(title=book.title,author=book.author).first()
# 		if temp != None:
# 			flash('book already exists','error')
# 			return redirect(url_for('newbook'))
# 		#if form.validate_on_submit():
# 		db.session.add(book)
# 		db.session.commit()
# 		app.logger.info('%s: user \"%s\" added \"%s\" by \"%s\" to the library, %s',time.asctime(),g.user.username,book.title,book.author,message)
# 	return redirect(url_for('library'))

# @app.route('/addrecord/<id>')
# def addrecord(id):
# 	book = models.Book.query.filter_by(id=int(id)).first()
# 	hasread=models.Has_Read()
# 	hasread.bookid = id
# 	hasread.userid = g.user.id
# 	#date when the user added the record
# 	Date = date.today()
# 	hasread.date = Date
# 	temp = models.Has_Read.query.filter_by(userid=g.user.id,bookid=id).first()
# 	#user has already added the book to their profile
# 	if temp != None:
# 		# flash('this book already exists in your record','error')
# 		app.logger.info('%s: \"%s\" tried to add \"%s\" by \"%s\" to their record of books again, but was rejected',time.asctime(),g.user.username,book.title,book.author)
# 		return redirect(url_for('library'))
# 	db.session.add(hasread)
# 	db.session.commit()
# 	app.logger.info('%s: \"%s\" added \"%s\" by \"%s\" to their record of books ',time.asctime(),g.user.username,book.title,book.author)
# 	return redirect(url_for('profile'))

# @app.route('/upvote/<id>')
# def upvote(id):
# 	book = models.Book.query.filter_by(id=int(id)).first()
# 	# has user read the book?
# 	temp = models.Has_Read.query.filter_by(userid=g.user.id,bookid=id).first()
# 	if temp != None: # user has read the book
# 		if temp.rating == 1: # user has unliked the book (changes rating to neutral)
# 			temp.rating = 0 # reset the rating to neutral
# 			book.upvotes = book.upvotes-1
# 			app.logger.info('%s: user \"%s\" removed their rating for \"%s\" by \"%s\" ',time.asctime(),g.user.username,book.title,book.author)
# 		elif temp.rating == -1: # user changes from dislike to liked
# 			temp.rating = 1
# 			book.upvotes = book.upvotes+1 # add upvote
# 			book.downvotes = book.downvotes-1 # take away a downvote
# 			app.logger.info('%s: user \"%s\" upvoted \"%s\" by \"%s\" ',time.asctime(),g.user.username,book.title,book.author)
# 		else: # first time the user has rated the book
# 			temp.rating = 1 # user has liked the book
# 			book.upvotes = book.upvotes+1 # add upvote
# 			app.logger.info('%s: user \"%s\" upvoted \"%s\" by \"%s\" ',time.asctime(),g.user.username,book.title,book.author)
# 		db.session.commit()
# 	else:
# 		app.logger.info('%s: user \"%s\" tried to rate \"%s\" by \"%s\" without having read it ',time.asctime(),g.user.username,book.title,book.author)
# 	return redirect(url_for('profile'))

# @app.route('/downvote/<id>')
# def downvote(id):
# 	book = models.Book.query.filter_by(id=int(id)).first()
# 	# has user read the book?
# 	temp = models.Has_Read.query.filter_by(userid=g.user.id,bookid=id).first()
# 	if temp != None: # user has read the book
# 		if temp.rating == -1: # user has removed their rating (changes rating to neutral)
# 			temp.rating = 0 # reset the rating to neutral
# 			book.downvotes = book.downvotes-1
# 			app.logger.info('%s: user \"%s\" removed their rating for \"%s\" by \"%s\" ',time.asctime(),g.user.username,book.title,book.author)
# 		elif temp.rating == 1: # user changes from liked to disliked
# 			temp.rating = -1
# 			book.downvotes = book.downvotes+1 # add downvote
# 			book.upvotes = book.upvotes-1 # take away an upvote
# 			app.logger.info('%s: user \"%s\" downvoted \"%s\" by \"%s\" ',time.asctime(),g.user.username,book.title,book.author)
# 		else: # first time the user has rated the book
# 			temp.rating = -1 # user has disliked the book
# 			book.downvotes = book.downvotes+1 # add downvote
# 			app.logger.info('%s: user \"%s\" downvoted \"%s\" by \"%s\" ',time.asctime(),g.user.username,book.title,book.author)
# 		db.session.commit()
# 	else:
# 		app.logger.info('%s: user \"%s\" tried to rate \"%s\" by \"%s\" without having read it ',time.asctime(),g.user.username,book.title,book.author)
# 	return redirect(url_for('profile'))
