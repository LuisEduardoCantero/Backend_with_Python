from flask import Flask, request, make_response, redirect, render_template, session, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest
from app import create_app
from app.forms import LoginForm

# creamos una instancia de flask y de Bootstrap
app = create_app()

todos = ['Comprar cafe', 'Comprar leche', 'Comprar todo', 'Comprar Saldo', 'Comprar puntos']

    
@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)
    
    
    
@app.errorhandler(404)
def not_found(error):
    
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    
    return response  

@app.route('/hello', methods = ['GET', 'POST']) # usamos este decorador para ejecutar hello
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    context = {
        'user_ip':user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': username
    }
    
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('Nombre registrado con exito!')
        
        return redirect(url_for('index'))
    
    return render_template('hello.html', **context)
#

















