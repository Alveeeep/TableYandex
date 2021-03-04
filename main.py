from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime
from flask import Flask, render_template, redirect
from forms.user import RegisterForm, LoginForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    return render_template("index.html", jobs=jobs)


def main():
    db_session.global_init("db/mars_explorer.db")

    app.run()


if __name__ == '__main__':
    main()
