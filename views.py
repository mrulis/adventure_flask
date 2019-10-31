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
    Where you choose what kind of blog to make.
    """
    return render_template('index.html')


@simple_route('/initial/')
def set_blogname(blog: dict, *args):
    """
    Where you input blog title.
    """
    blog['blog_type'] = request.values.get('blog_type')
    return render_template('blog_title.html', blog = blog)


@simple_route('/set_title/')
def set_title(blog: dict, *args):
    """
    Where blog title is set as value in blog dictionary.
    """
    blog['title'] = request.values.get('title')
    return redirect('/picture_bank/')


@simple_route('/picture_bank/')
def set_pictures(blog: dict, *args):
    """
    Where you choose from set of pictures (options determined by blog type).
    When you delete a post, resets caption value to None so you can inout anew caption later.
    """
    blog['caption'] = None
    return render_template('picture_bank.html', blog = blog)


@simple_route('/set_picture/')
def set_picture(blog: dict, *args):
    """
    Where chosen picture is set as value in blog dictionary.
    """
    blog['picture'] = request.values.get('image')
    return redirect('/blog_page/')


@simple_route('/set_caption/')
def set_caption(blog: dict, *args):
    """
    Where blog caption is set as value in blog dictionary.
    """
    blog['caption'] = request.values.get('caption')
    return redirect('/blog_page/')


@simple_route('/blog_page/')
def make_page(blog: dict, *args):
    """
    Where blog page is.
    Can add caption to chosen photo.
    Can choose to add text post.
    """
    blog['text_post'] = request.values.get('text_post')
    return render_template('blog_page.html', blog = blog)


@simple_route('/text_post/')
def set_text_post(blog: dict, *args):
    """
    Where you can input text post.
    """
    return render_template('text_post.html', blog = blog)


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



