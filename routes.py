from flask import (
    session,
    redirect,
    url_for,
    render_template,
    request,
    Blueprint
)

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/enter', methods=['POST'])
def enter():
    name = request.form.get('name')
    if name is not None:
        session['name'] = name
        return redirect(url_for('.chat'))
    else:
        return redirect(url_for('.index'))


@main.route('/chat')
def chat():
    name = session.get('name', '')
    if name == '':
        return redirect(url_for('.index'))
    else:
        return render_template('chat.html')
