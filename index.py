from flask import Flask
from flask_restful import Resource, Api

from parsers.remitly import Remitly
from parsers.xoom import Xoom

app = Flask(__name__)
api = Api(app)


class Exchange(Resource):
    def get(self, exchange):
        if exchange == "remitly":
            return Remitly.get_amount()
        elif exchange == "xoom":
            return Xoom.get_amount()
        else:
            return {"hi": "yo"}


api.add_resource(Exchange, '/<string:exchange>')

if __name__ == '__main__':
    app.run(debug=True)
