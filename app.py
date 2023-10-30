from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import xgboost

regressor = xgboost.XGBRegressor()

class MyForm(FlaskForm):
    v = StringField('V', validators=[DataRequired()])
    a = StringField('A', validators=[DataRequired()])
    s = StringField('S', validators=[DataRequired()])
    n = StringField('N', validators=[DataRequired()])
    submit = SubmitField('Predict')


app = Flask(__name__)
app.secret_key = 'A Secret Key'
filename = 'finalized_model.sav'
regressor.load_model(f'model/{filename}')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        v = float(form.v.data)
        a = float(form.a.data)
        s = float(form.s.data)
        n = float(form.n.data)
        result = regressor.predict([[v, a, s, n]])
        return render_template('index.html', form=form, result=result, show=True)
    return render_template('index.html', form=form, show=False)


if __name__ == '__main__':
    app.run(debug=True)
