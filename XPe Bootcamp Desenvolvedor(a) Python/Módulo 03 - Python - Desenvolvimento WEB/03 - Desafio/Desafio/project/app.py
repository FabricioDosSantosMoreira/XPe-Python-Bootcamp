from flask import Flask, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

database = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()


def get_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("project.config.DevelopmentConfig")

    csrf.init_app(app)
    database.init_app(app)
    migrate.init_app(app, db=database)

    from project.routes.user import user_bp
    app.register_blueprint(user_bp)

    @app.route("/")
    def index():
        return redirect(url_for('user_bp.index'))
    

    return app

if __name__ == "__main__":
    app = get_app()
    app.run(debug=True)
