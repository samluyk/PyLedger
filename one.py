import os
from flask import Flask, render_template,session,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FloatField,DateField,validators,TextField,SelectField
from wtforms.validators import DataRequired

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'temporarysecuritykey'

# Below is the fields the form will have
class ExpenseForm(FlaskForm):

    theExpense = StringField("Enter your expense: ",validators=[DataRequired()])
    expenseAmount = FloatField("Enter the amount: ",validators=[DataRequired()])
    #expensePrimaryCategory = StringField("Choose the primary category: ",validators=[DataRequired()])
    #expenseSecondaryCategory = StringField("Choose the secondary category: ",validators=[DataRequired()])
    expenseAbout = TextField("Enter any comments: ")
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    #theExpense = False
    form = ExpenseForm()
    if form.validate_on_submit():
        session['theExpense'] = form.theExpense.data
        session['expenseAmount'] = form.expenseAmount.data
        session['expenseAbout'] = form.expenseAbout.data
        return redirect(url_for('submitted'))

    return render_template('index.html',form=form)
    
@app.route("/submitted")
def submitted():
    return render_template('submitted.html')

if __name__ == '__main__':
        app.run(debug=True)