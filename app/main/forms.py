from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, \
    TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me-upload area'),
                             validators=[Length(min=10, max=1000)])
    submit = SubmitField(_l('Upload'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class PostForm(FlaskForm):
    post = TextAreaField(_l('Upload article'), validators=[DataRequired()])
    submit = SubmitField(_l('Upload'))


class RootForm(FlaskForm):
    customers = StringField(_l('customers'), validators=[DataRequired()])
    business = StringField(_l('business'), validators=[DataRequired()])
    other = StringField(_l('other'), validators=[DataRequired()])
    submit = SubmitField(_l('Update'))


class CareersForm(FlaskForm):
    WorkLocationinclude = StringField(_l('Work Location Include'), validators=[DataRequired()])
    CareerCategory = StringField(_l('Career Category'), validators=[DataRequired()])
    JobTitle = StringField(_l(' Job Title'), validators=[DataRequired()])
    Category = StringField(_l('Category'), validators=[DataRequired()])
    Location = StringField(_l('Location'), validators=[DataRequired()])
    submit = SubmitField(_l('Update Careers'))
