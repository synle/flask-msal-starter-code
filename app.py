from flask import Flask, render_template, redirect, request, session, abort, jsonify, url_for
from flask_session import Session
import identity, identity.web
import app_config


port=3000
app = Flask(__name__)
app.config.from_object(app_config)
Session(app)


auth = identity.web.Auth(
    session=session,
    authority=app.config["AUTHORITY"],
    client_id=app.config["CLIENT_ID"],
    client_credential=app.config["CLIENT_SECRET"],
)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api/auth/login")
def login():
    auth_request = auth.log_in(
        scopes = app.config["SCOPE"],
        redirect_uri= app.config["REDIRECT_PATH"]
    )

    return redirect(auth_request['auth_uri'])


@app.route(app.config['BASE_REDIRECT_PATH'])
def login_callback():
    auth.complete_log_in(request.args)
    return redirect('/api/auth/user')


@app.route("/api/auth/user")
def get_user_profile():
    if not auth.get_user():
        return abort(401)
    return auth.get_user()


@app.route("/api/auth/logout")
def logout():
    auth.log_out('/')
    return '', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
