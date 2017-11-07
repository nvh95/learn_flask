from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url


class BookmarkForm(FlaskForm):
    url = URLField('Your URL: ', validators=[DataRequired(), url()])
    description = StringField('Description: ')