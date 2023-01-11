# flask --app hello run
# flask --app hello --debug run

from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"


@app.route("/<path:name>")
def hello(name):
    return f"Hello, {escape(name)}!"


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

