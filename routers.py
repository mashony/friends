from flask import render_template, request, make_response, session
from authomatic.adapters import WerkzeugAdapter
from utils import find_mutual_friends
from main import app, authomatic, mongo


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def login(provider_name):
    response = make_response()
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name,
                              session=session,
                              session_saver=lambda: app.save_session(session, response))
    if result:
        friends = None
        if result.user:
            result.user.update()
            if not mongo.db.social_users.find_one({"id": result.user.id, "provider": result.provider.name}):
                mongo.db.social_users.insert({"id": result.user.id, "provider": result.provider.name})
            friends = find_mutual_friends(result.provider, result.user.id)
        return render_template('login.html', result=result, friends=friends)
    return response