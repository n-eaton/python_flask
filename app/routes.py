from app import app
from flask import render_template
from app.models import Post 


@app.route("/")  # function decorator


def home():      # another function 
    context = {
        'posts': Post.query.all()
    }
    # return render_template('home.html', body='this is the first post', first_name='Nati', last_name='Doe', date_posted=9 )
    return render_template ('home.html', **context)



@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')
