# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash


# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_user = Blueprint('auth', __name__, url_prefix='/user')

# Set the route and accepted methods

@mod_user.route('/', methods=['GET'])
def index():
    return "OK"
