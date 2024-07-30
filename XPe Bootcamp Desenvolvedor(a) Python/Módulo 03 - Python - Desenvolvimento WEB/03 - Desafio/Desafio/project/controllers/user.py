from typing import List, Union

from flask import Response, redirect, render_template, request, url_for
from flask_wtf import FlaskForm
from project.app import csrf, database
from project.forms import UserForm
from project.models.user import User


@csrf.exempt
def index() -> str:
    with database.session() as session:

        users: List[User] = session.query(User).all()
        users_as_json = [user.serialize() for user in users]

        return render_template("users_index.html", users=users_as_json)
    

@csrf.exempt
def create() -> Union[Response, str]:
    form: FlaskForm = UserForm()

    if request.method == "POST" and form.validate_on_submit():
        with database.session() as session:
            try:
                new_user = User(
                    nome=form.nome.data,
                    telefone=form.telefone.data,
                    endereco=form.endereco.data,
                    cpf=form.cpf.data
                )

                session.add(new_user)
                session.commit()

                return redirect(url_for('user_bp.index'))
            
            except Exception as exc:
                print(exc)
                session.rollback()

    return render_template('user_create.html', form=form)


@csrf.exempt
def update(user_id) -> Union[Response, str]:
    user = User.query.get(user_id)
    form: FlaskForm = UserForm(obj=user)

    # Método PUT que vem do HTML
    # <input type="hidden" name="_method" value="PUT">
    if request.form['_method'] == 'PUT' and form.validate_on_submit():
        print("SALVANDO")
        with database.session() as session:
            try:
                session.query(User).filter_by(id=user_id).update({
                    'nome': form.nome.data,
                    'telefone': form.telefone.data,
                    'endereco': form.endereco.data,
                    'cpf': form.cpf.data
                })
                session.commit()
                return redirect(url_for('user_bp.index'))
            except Exception as exc:
                print(exc)
                session.rollback()

    return render_template('user_update.html', form=form, user=user)


@csrf.exempt
def delete(user_id) -> Response:

    # Método DELETE que vem do html
    # <input type="hidden" name="_method" value="DELETE">
    if request.form['_method'] == 'DELETE':
        with database.session() as session:
            try:
                user = session.query(User).get(user_id)
                session.delete(user)
                session.commit()

            except Exception as exc:
                print(exc)
                session.rollback()
    
    return redirect(url_for('user_bp.index'))
