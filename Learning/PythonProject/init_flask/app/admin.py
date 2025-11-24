from flask_admin import Admin
from app import db
from flask_admin.contrib.sqla import ModelView
from app.models import User, Tag, Response
from wtforms import Form, StringField, SelectField, BooleanField, IntegerField


class UserForm(Form):
    username = StringField('Username')
    email = StringField('Email')
    avatar = StringField('Avatar')
    google_id = StringField('Google ID')
    gender = SelectField('Gender', choices=[('male', 'male'), ('female', 'female'), ('other', 'other')])
    status = SelectField('Status', choices=[('active', 'active'), ('banned', 'banned')])
    admin = BooleanField('Admin')


class UserAdmin(ModelView):
    form = UserForm
    form_excluded_columns = ('response', 'create_at', 'update_at', 'id')


class ResponseAdmin(ModelView):
    form_overrides = {
        'status': SelectField,
    }
    form_args = {
        'status': {
            'choices': [('public', 'public'), ('private', 'private')],
        },
        'user': {
            'query_factory': lambda: User.query.all,
            'allow_blank': False,
            'get_label': 'username'
        }
    }
    form_excluded_columns = ('create_at', 'update_at', 'id')


class TagForm(Form):
    name = StringField('Name')


class TagAdmin(ModelView):
    form = TagForm
    form_excluded_columns = ('create_at', 'update_at', 'id')


def init_admin(app):
    admin = Admin(app, name='Save-brain Administration', template_mode='bootstrap4')
    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(ResponseAdmin(Response, db.session))
    admin.add_view(TagAdmin(Tag, db.session))
    return admin
