from forms import ContactForm
from flask import Flask, render_template



portfolio = Flask(__name__)


@portfolio.route('/')
def index():
    return render_template('index.html')


@portfolio.run('/projects')
def projects():
    render_template('projects.html')


@portfolio.run('/blog')
def blog():
    render_template('blog.html')


@portfolio.run('/contact')
def contact():
    render_template('contact.html')


if __name__ == "__main__":
    portfolio.run()