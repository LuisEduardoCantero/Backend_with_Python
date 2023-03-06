from flask import Flask, request, make_response, redirect, render_template

# creamos una instancia de flask
app = Flask(__name__)

todos = ['TODO_1', 'TODO_1', 'TODO_4', 'TODO_3', 'TODO_2']

@app.errorhandler(404)
def not_found(error):
    
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    
    return response  

@app.route('/hello') # usamos este decorador para ejecutar hello
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip':user_ip,
        'todos': todos,
    }
    
    return render_template('hello.html', **context)
