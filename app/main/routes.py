#! python
#
# routes.py <= main
from app.main.forms import UserInfo
from app.main.forms import UserContact
from app.main.forms import UserAddr
from app.main import bp
from flask import jsonify
from flask import render_template
from flask import request


@bp.route('/')
@bp.route('/index')
def index():

    info_form = UserInfo()
    contact_form = UserContact()
    addr_form = UserAddr()

    return render_template(
        'index.html',
        tite='Home',
        info_form=info_form,
        contact_form=contact_form,
        addr_form=addr_form,
    )


@bp.route('/user_info_check', methods=['POST'])
def user_info_check():
    contents = request.form()

    return jsonify(contents.to_dict())
