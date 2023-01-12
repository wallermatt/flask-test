# flask --app hello run
# flask --app hello --debug run

from flask import Flask, url_for, request
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"


@app.route("/index/")
def index():
    return "<p>Index</p>"


@app.route("/<path:name>")
def hello(name):
    return f"Hello, {escape(name)}!"


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return request.headers.get("key1")
    else:
        return "boring old get"


with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('index'))
    print(url_for("hello", name="test"))

