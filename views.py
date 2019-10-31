from pprint import pprint

from flask import render_template, app, redirect
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


@simple_route('/initial/')
def set_blogname(blog: dict, *args):
    blog['blog_type'] = request.values.get('blog_type')
    return render_template('blog_title.html', blog = blog)


@simple_route('/set_title/')
def set_title(blog: dict, *args):
    blog['title'] = request.values.get('title')
    return redirect('/picture_bank/')


@simple_route('/picture_bank/')
def set_pictures(blog: dict, *args):
    return render_template('picture_bank.html', blog = blog)


@simple_route('/set_picture/')
def set_picture(blog: dict, *args):
    blog['picture'] = request.values.get('image')
    return redirect('/blog_page/')


@simple_route('/blog_page/')
def make_page(blog: dict, *args):
    blog['caption'] = request.values.get('caption')
    blog['text_post'] = request.values.get('text_post')
    return render_template('blog_page.html', blog = blog)


@simple_route('/text_post/')
def set_text_post(blog: dict, *args):
    return render_template('text_post.html', blog = blog)


@simple_route('/set_text/')
def set_text(blog: dict, *args):
    blog['text_post'] = request.values.get('text_post')
    return redirect('/blog_page/')



@simple_route('/aesthetic_picture_bank/')
def set_aesthetic_pictures(blog: dict, *args):
    return render_template('aesthetic_picture_bank.html', blog = blog)


@simple_route('/aesthetic_pic_1/')
def aesthetic_blog_1(blog: dict, *args):
    blog['caption'] = request.values.get('caption')
    return render_template('aesthetic_pic_1.html', blog = blog)


@simple_route('/aesthetic_pic_2/')
def aesthetic_blog_2(blog: dict, *args):
    blog['caption'] = request.values.get('caption')
    return render_template('aesthetic_pic_2.html', blog = blog)


@simple_route('/aesthetic_pic_3/')
def aesthetic_blog_3(blog: dict, *args):
    blog['caption'] = request.values.get('caption')
    return render_template('aesthetic_pic_3.html', blog = blog)



@simple_route('/food/')
def set_food_blogname(blog: dict):
    return render_template('food_initial.html')


@simple_route('/food_picture_bank/')
def set_food_pictures(blog: dict, *args):
    blog['title'] = request.values.get('title')
    return render_template('food_picture_bank.html', blog = blog)


@simple_route('/food_pic_1/')
def food_blog_1(blog: dict):
    return render_template('food_pic_1.html', blog = blog)


@simple_route('/food_pic_2/')
def food_blog_2(blog: dict):
    return render_template('food_pic_2.html', blog = blog)


@simple_route('/food_pic_3/')
def food_blog_3(blog: dict):
    return render_template('food_pic_3.html', blog = blog)



@simple_route('/travel/')
def set_travel_blogname(blog: dict):
    return render_template('travel_initial.html')


@simple_route('/travel_picture_bank/')
def set_travel_pictures(blog: dict, *args):
    blog['title'] = request.values.get('title')
    return render_template('travel_picture_bank.html', blog = blog)


@simple_route('/travel_pic_1/')
def travel_blog_1(blog: dict):
    return render_template('travel_pic_1.html', blog = blog)


@simple_route('/travel_pic_2/')
def travel_blog_2(blog: dict):
    return render_template('travel_pic_2.html', blog = blog)


@simple_route('/travel_pic_3/')
def travel_blog_3(blog: dict):
    return render_template('travel_pic_3.html', blog = blog)

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



