from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # makes id column to uniquely id each entry
    username = db.Column(db.String(200), nullable=False) #string field to store the user's input username in the db
    password = db.Column(db.String(200), nullable=False) #string field to store the user's input password in the db
    books = db.relationship("Has_Read",back_populates="user")

class Has_Read(db.Model): #association object
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    bookid = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True)
    rating = db.Column(db.Integer, default=0) #the rating the user gave the book (like=1,dislike=1)
    date = db.Column(db.Date) #the date the use made the book record
    book = db.relationship("Book", back_populates="users")
    user = db.relationship("User", back_populates="books")

class Book(db.Model): #global library of all books
    id = db.Column(db.Integer, primary_key=True) # makes id column to uniquely id each entry
    title = db.Column(db.String(200), nullable=False)# name of the book
    author = db.Column(db.String(200), nullable=False)# author of the book
    date = db.Column(db.Date) #need to add specific formatting to it like i did with todo
    blurb = db.Column(db.String(500))# short desc of the book
    filepath = db.Column(db.String(500))# path to the file which is the book's front cover
    upvotes = db.Column(db.Integer, default=0)# way for users to rate a book
    downvotes = db.Column(db.Integer, default=0)
    users = db.relationship("Has_Read",back_populates="book")
