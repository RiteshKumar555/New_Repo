from flask import Flask,render_template,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,validators
from flask_wtf.file import FileField, FileRequired
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

app=Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '-p'
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)



class IndexForm(Form):
    yourregion = StringField('  your region', [validators.Length(min=1, max=50)])
    Atthestage = StringField('At the stage', [validators.Length(min=4, max=25)])
    Reward = StringField('Reward', [validators.Length(min=1, max=50)])
    Industry =StringField(' Industry', [validators.Length(min=1, max=50)])
    thestartingtime=StringField('the starting time', [validators.Length(min=1, max=50)])
    ProjectContact=StringField('Project Contact', [validators.Length(min=1, max=50)])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = IndexForm(request.form)
    if request.method == 'POST' and form.validate():
        yourregion = form.yourregion.data
        Atthestage = form.Atthestage.data
        Reward = form.Reward.data
        Industry = form.Industry.data
        thestartingtime=form.thestartingtime.data
        ProjectContact=form.ProjectContact.data

        cur = mysql.connection.cursor()

      
        cur.execute("INSERT INTO users(yourregion, Atthestage, Reward,  Industry,  thestartingtime, ProjectContact) VALUES(%s, %s, %s, %s, %s, %s)", (yourregion, Atthestage, Reward,  Industry,  thestartingtime, ProjectContact))

     
        mysql.connection.commit()

      
        cur.close()
    return render_template('index.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)    