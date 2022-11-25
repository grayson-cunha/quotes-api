from flask import Flask
from flask_smorest import Api
from flask_mongoengine import MongoEngine

from resources.category import blp as CategoriesBlueprint

def create_app(db_url=None):
  app = Flask(__name__)

  app.config["PROPAGATE_EXCEPTIONS"] = True
  app.config["API_TITLE"] = "Stores REST API"
  app.config["API_VERSION"] = "v1"
  app.config["OPENAPI_VERSION"] = "3.0.3"
  app.config["OPENAPI_URL_PREFIX"] = "/"
  app.config["OPENAPI_SWAGGER_UI_PATH"] = "/documentation"
  app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
  app.config['MONGODB_SETTINGS'] = {
    'db': 'quotes-api',
  }
  
  db = MongoEngine()
  
  db.init_app(app)
  
  api = Api(app)
  
  api.register_blueprint(CategoriesBlueprint)
  
  return app
