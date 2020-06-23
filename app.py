from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

posts = {
    0: {'post_id': 1,
        'title': "Heyyy",
        'content': "You"
    }
}

@app.route('/')
def home():
    return render_template('home.jinja2')


if __name__ == '__main__':
    app.run(debug=True)
