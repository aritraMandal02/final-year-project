from flask import Flask, render_template
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
    app.run(host='0.0.0.0', debug=True)
