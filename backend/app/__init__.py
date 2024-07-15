from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate


from dotenv import load_dotenv
load_dotenv()


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_mode):
    app = Flask(__name__)
    app.config.from_object(config_mode)

    db.init_app(app)
    # registyer blueprints
    from auth.routes import auth_bp
    from journals.routes import journal_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(journal_bp)
    
    migrate.init_app(app, db)

    return app