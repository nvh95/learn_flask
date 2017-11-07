from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime

from forms import BookmarkForm

app = Flask(__name__)

bookmarks = []
app.config['SECRET_KEY'] = '\x9c\xf9\xdd\x92\xed\x0c\x13%\xf9%z8\x02\xaa\x9f\xae\xc3\xf0E\xa3\x91\xffs\x16'


def store_bookmark(url, description):
    bookmarks.append(dict(
        url=url,
        description = description,
        user="hung",
        date=datetime.utcnow()
    ))
    print(bookmarks[-1]['url'])


def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=new_bookmarks(5))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        store_bookmark(url, description)
        flash("stored url: '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
