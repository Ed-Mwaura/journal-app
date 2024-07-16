from flask import Flask
from flask_migrate import Migrate
from exts import db, login_manager

from dotenv import load_dotenv
load_dotenv()


migrate = Migrate()


def create_app(config_mode):
    app = Flask(__name__)
    app.config.from_object(config_mode)

    db.init_app(app)

    # flask_login
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models import Users

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    # registyer blueprints
    from auth.routes import auth_bp
    from journals.routes import journal_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(journal_bp)
    
    migrate.init_app(app, db)

    return app