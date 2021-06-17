from flask_wtf import Form
from wtforms import TextField, SubmitField,HiddenField
from wtforms.validators import InputRequired
from wtforms.fields.html5 import DateTimeLocalField



class SendTestEmail(Form):
    newsletter_subject = TextField('newsletter_subject')

class ScheduleForm(Form):
    schedule_date = DateTimeLocalField('schedule_date', format='%Y-%m-%dT%H:%M')


