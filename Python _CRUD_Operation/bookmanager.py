import os
from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLALchemy


project_dir =os.path.dirname(os.path.abspath(__file__))
database_file ="sqlite:///{}".format(os.path.join(project_dir,"bookdatabase.db"))
print(database_file)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLALchemy(app)
class  Book(db.Model):
        title=db.column(db.string(80),unique=True,nullable=True, primary_key=True)
        def __repr__(self):
            return "<Title: {}>".format(self.title)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        book = Book(title=request.form.get("title"))
        db.session.add(book)
        db.session.commit()
        books =Book.query.all()
    return render_template("home.html", books=books)
     # @app.route("/update", methods=["POST"])








print(project_dir)

# @app.route('/')
# def index():
#     return 'hello world'




