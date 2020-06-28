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


@app.route('/test', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        result = request.form
        print(result)
    return render_template('test.jinja2', result = result)


if __name__ == '__main__':
    app.run(debug=True)
