from bottle import route, run, template
from bottle import get, post, request # or route

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
        Username: <input name="username" type="text" />
        Password: <input name="password" type="password" />
        <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
def check_login(username, password):
    if (username == "chijuzipi") and (password == "123"):
        return 1 
    else:
        return 0


run(host='localhost', port=8080)
