from flask import render_template, app
from flask import request
from route_helper import simple_route
from flask import Flask
app = Flask(__name__)


@simple_route('/')
def hello(blog: dict) -> str:
    """
    The welcome screen for the game.

    :param blog: The current world
    :return: The HTML to show the player
    """
    return render_template('index.html')


@simple_route('/aesthetic/')
def set_aesthetic_blogname(blog: dict):
    return render_template('aesthetic_initial.html')


@simple_route('/food/')
def set_food_blogname(blog: dict):
    return render_template('food_initial.html')


@simple_route('/travel/')
def set_travel_blogname(blog: dict):
    return render_template('travel_initial.html')

NAME_BLOG = """
<body bgcolor="#34526F">
<!-- Curly braces let us inject values into the string -->
you are creating a new {} blog. decide on a handle!<br>

<!-- Image taken from site that generates random Corgi pictures-->
<img src="http://placecorgi.com/260/180" /><br>
    
what will your username be?

<!-- Form allows you to have more text entry -->    
<form action="/save/name/">
    <input type="text" name="title"><br>
    <input type="submit" value="Submit"><br>
</form>
"""


@app.route('/aesthetic_picture_set/', methods=['POST'])
def set_aesthetic_pictures(blog: dict):
    blog['title'] = request.form['title']
    print(request.form)
    print(blog['title'])
    return render_template('aesthetic_picture_bank.html', blog_title=blog['title'])


@simple_route("/save/title/")
def save_name(blog: dict, blog_name: str) -> str:
    """
    Decide name of blog.

    :param blog: The current world
    :param blog_name:
    :return:
    """
    blog['name'] = blog_name

    return BLOG_HEADER+"""this is your {type} blog, and your username is {blog_name}
    <br><br>
    <a href='/'>Return to the start</a>
    """.format(type=blog['location'], blog_name=blog['name'])



