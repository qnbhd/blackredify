from blackredify.api import API

app = API()


@app.route('/home')
def home(request, response):
    response.text = 'Привет, это моя главная страница'


@app.route('/about')
def about(request, response):
    response.text = 'Привет, это страница о нас!'


@app.route('/hello/{name}')
def greeting(request, response, name):
    response.text = f"Hello, {name}"


@app.route('/users/{user}/{age}')
def user(request, response, user, age):
    response.text = f'Hello, {user}, {age}'
