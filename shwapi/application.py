import os
from timemethods import get_midnight
from flask import Flask
from flask_restful import Resource, Api
import db




# EB looks for an 'application' callable by default.
application = Flask(__name__, instance_relative_config=True)
api = Api(application)
application.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(application.instance_path, 'shwapi.sqlite'),
)

db.init_app(application)

@application.route('/hello')
def hello():
    return 'Hello, World!'

class HelloWorld(Resource):
    def get(self):
        return {'hello': get_midnight()}

api.add_resource(HelloWorld, '/')


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()