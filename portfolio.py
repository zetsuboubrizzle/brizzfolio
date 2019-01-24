from forms import ContactForm
import config
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap



portfolio = Flask(__name__)
bootstrap = Bootstrap(portfolio)
portfolio.config['SECRET_KEY'] = 'a capella' #config.environ_var(config.environ['SECRET_KEY'])


@portfolio.route('/')
def index():
    return render_template('index.html')


@portfolio.route('/about')
def about():
    return render_template('about.html')


@portfolio.route('/projects')
def projects():
    return render_template('projects.html')


@portfolio.route('/blog')
def blog():
    return render_template('blog.html')


@portfolio.route('/contact')
def contact():
    form = ContactForm()
    return render_template('contact.html', form=form)


if __name__ == "__main__":
    portfolio.run()