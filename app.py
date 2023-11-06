from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, ValidationError
import xgboost

regressor = xgboost.XGBRegressor()


def validate_value(form, field):
    try:
        float(field.data)
    except ValueError:
        raise ValidationError('Not a valid input.')
    else:
        if field.name == "v":
            if not (22 <= float(field.data) <= 36):
                raise ValidationError(
                    'Arc Voltage must be in range of (22, 36)')

        if field.name == "a":
            if not (250 <= float(field.data) <= 550):
                raise ValidationError('Current must be in range of (250, 550)')

        if field.name == "s":
            if not (6 <= float(field.data) <= 18):
                raise ValidationError(
                    'Travel speed must be in range of (6, 18)')

        if field.name == "n":
            if not (20 <= float(field.data) <= 34):
                raise ValidationError(
                    'Nozzle to plate distance must be in range of (20, 34)')


class MyForm(FlaskForm):
    v = StringField('V', validators=[DataRequired(), validate_value])
    a = StringField('A', validators=[DataRequired(), validate_value])
    s = StringField('S', validators=[DataRequired(), validate_value])
    n = StringField('N', validators=[DataRequired(), validate_value])
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
