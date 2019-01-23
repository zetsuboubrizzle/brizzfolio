from forms import ContactForm
import config
from flask import Flask, render_template



portfolio = Flask(__name__)
portfolio.config['SECRET_KEY'] = config.environ_var(config.environ['SECRET_KEY'])

@portfolio.route('/')
def index():
    return render_template('index.html')


@portfolio.route('/projects')
def projects():
    render_template('projects.html')


@portfolio.route('/blog')
def blog():
    render_template('blog.html')


@portfolio.route('/contact')
def contact():
    render_template('contact.html')


if __name__ == "__main__":
    portfolio.run()