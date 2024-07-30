from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()
migrate = Migrate()


def get_app() -> Flask:

    from project.routes.users import user_bp

    app = Flask(__name__)
    app.config.from_object("project.config")

    database.init_app(app=app)
    migrate.init_app(app=app, db=database)

    app.register_blueprint(user_bp, url_prefix="/users")

    @app.route("/")
    def index():
        return render_template("index.html")

    return app


if __name__ == "__main__":
    app = get_app()
    app.run(debug=True)
