from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:Password1@localhost/Reports'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class running_reports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    report_name = db.Column(db.String(100))
    start_time = db.Column(db.DateTime(timezone=True), server_default=func.now())


@app.route('/')
def index():
    reports = running_reports.query.all()
    return render_template('index.html', reports=reports)

@app.route('/processuser', methods = ['POST'])
def processuser():
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        report_name = request.form['report_name']
        new_user = running_reports(fname=fname, lname=lname, email=email, report_name=report_name)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index'))

@app.route('/adduser')
def adduser():
        return render_template('adduser.html')


#Things to do
    #Get the search bar working.
    #Ask/Look into AJAX for automatic page refreshing
    #Center the reports, add gaps/spacing
    #Figure out how to





#Some helpful info for when you get stuck

#Creating the table
    # 1. make sure you're venv is running.

    # 2. start py

    # 3. import the db:
        # from reporter import db, running_reports

    # 4. create the table:
        #db.create_all()
            #if you need to add columns to the table you must first delete the table and recreate it.
                #db.drop_all()
                #db.create_all()

    # 5. run flask:
        # flask run


#Adding to the table
    # 1. start py

    # 2. import the db

    # 3. save information to a var:
        #random_var = <dbname>(col1='text', col2='text)...and so on...

    # 4. add the object (random_var) to the session:
        #db.session.add(random_var)

    # 5. commit changes:
        # db.session.commit()

#Querying using SQLAlchemy
    #use this link...https://docs.sqlalchemy.org/en/14/orm/tutorial.html#querying
