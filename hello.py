# flask --app hello run
# flask --app hello --debug run

from flask import Flask, url_for, request, render_template, make_response, abort, redirect, session
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
        abort(400)

@app.get('/login2')
def login_get():
    return "Login2 decorator GET"

@app.post('/login2')
def login_post():
    return "Login2 decorator POST"


@app.route("/template/")
@app.route("/template/<name>")
def template_display(name=None):
    style_url = url_for('static', filename='mystyle.css')
    return render_template("template.html", name=name, style_url=style_url)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files)
        #f = request.files['invoice_summary.csv']
        f = request.files['']
        f.save('uploaded_file.txt')
        return "upload post"
    return "upload"


@app.route('/set_cookie/<day>')
def set_cookie(day):
    style_url = url_for('static', filename='mystyle.css')
    resp = make_response(render_template("template.html", name="set cookie", style_url=style_url))
    resp.set_cookie('day_name', day)
    return resp


@app.route('/read_cookie')
def read_cookie():
    day = request.cookies.get("day_name")
    style_url = url_for('static', filename='mystyle.css')
    return render_template("template.html", name=day, style_url=style_url)


@app.route("/me_api")
def me_api():
    return {
        "username": "matthew",
        "theme": "narc",
        "image": "image file",
    }



with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('index'))
    print(url_for("hello", name="test"))

