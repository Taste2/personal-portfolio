from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Stephen Tawiah',
        'title': 'Understanding and Overcoming Tests',
        'content': 'First post content',
        'date_posted': 'August 17, 2022'
    },
    {
        'author': 'Kate Tawiah',
        'title': 'Principles of Marketing',
        'content': 'Second post content',
        'date_posted': 'August 20, 2022'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
@app.route('/home/about')
def about():
    return render_template('about.html', title='About')

app.run(debug=True)