from flask import Flask, render_template
import pickle
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import sklearn
import xgboost

regressor = xgboost.XGBRegressor()

class MyForm(FlaskForm):
    v = StringField('V', validators=[DataRequired()])
    a = StringField('A', validators=[DataRequired()])
    s = StringField('S', validators=[DataRequired()])
    n = StringField('N', validators=[DataRequired()])


app = Flask(__name__)
app.secret_key = 'A Secret Key'
filename = 'finalized_model.sav'
regressor.load_model(f'model/{filename}')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
