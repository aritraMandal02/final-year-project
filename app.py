from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, ValidationError
import xgboost

regressor = xgboost.XGBRegressor()


def check_float(form, field):
    try:
        float(field.data)
    except ValueError:
        raise ValidationError('Not a valid input.')


class MyForm(FlaskForm):
    v = StringField('V', validators=[DataRequired(), check_float])
    a = StringField('A', validators=[DataRequired(), check_float])
    s = StringField('S', validators=[DataRequired(), check_float])
    n = StringField('N', validators=[DataRequired(), check_float])
    submit = SubmitField('Predict')


app = Flask(__name__)
app.secret_key = 'A Secret Key'
filename = 'finalized_model.sav'
regressor.load_model(f'model/{filename}')
show = False
result = None
v, a, s, n = None, None, None, None


@app.route('/', methods=['GET', 'POST'])
def index():
    global v, a, s, n, result, show
    form = MyForm(v=v, a=a, s=s, n=n)
    if form.validate_on_submit():
        v = form.v.data
        a = form.a.data
        s = form.s.data
        n = form.n.data
        result = regressor.predict([[float(v), float(a), float(s), float(n)]])
        show = True
        return redirect(url_for('index'))
    return render_template('index.html', form=form, result=result, show=show)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
