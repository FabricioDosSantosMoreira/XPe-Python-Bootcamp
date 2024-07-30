from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class UserForm(FlaskForm):

    nome = StringField('Nome', validators=[DataRequired(), Length(max=100)])
    telefone = StringField('Telefone', validators=[DataRequired(), Length(min=14, max=14)])
    endereco = StringField('Endereço', validators=[DataRequired(), Length(max=200)])
    cpf = StringField('CPF', validators=[DataRequired(), Length(min=11, max=11)])

    submit = SubmitField('Submit')
