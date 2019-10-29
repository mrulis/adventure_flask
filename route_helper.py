"""
The simple_route decorator allows us to quickly make routes that have proper
state being passed in and manipulated.

This file also establishes the reset route, with the idea that everyone
would like to be able to reset their game.
"""

import json
from functools import wraps

from flask import request, session, redirect

from app import app


INITIAL_BLOG = {
    "title": "",
    "caption": None,
    "blog_type": "",
    "picture": ""
}


def simple_route(path: str, **options):
    """
    Creates a new route for the URL endpoint `path`. This decorator wraps
    the View endpoint to pass in the current `world` (deserialized from session data
    upon function entrance and serialized back into session once the function is
    done), any URL parameters, and then any request parameters (sorted by key name).

    :param path: The URL endpoint to use
    :type path: str
    :param options: Options to pass along to Flask's app.route. Usually you can ignore this.
    :return: Decorated function
    """
    def decorator(f):
        @app.route(path, **options)
        @wraps(f)
        def decorated_function(*args, **kwargs):
            blog = json.loads(session.get('blog', json.dumps(INITIAL_BLOG)))
            values = [v for k, v in sorted(request.values.items())]
            result = f(blog, *args, *values, **kwargs)
            session['blog'] = json.dumps(blog)
            return result
        return decorated_function
    return decorator


@app.route("/reset/")
def reset():
    """
    Resets the game's world state (stored in session) and redirects to
    the root page.
    :return: Redirection to '/'
    """
    session['blog'] = json.dumps(INITIAL_BLOG)
    return redirect('/')

