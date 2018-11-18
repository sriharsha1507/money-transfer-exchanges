from flask import Flask, jsonify
from flask_restful import Resource, Api

from parsers.remitly import Remitly
from parsers.xoom import Xoom

app = Flask(__name__)
api = Api(app)


class Exchange(Resource):
    def get(self, exchange):
        if exchange == "remitly":
            return Remitly().get_amount()
        elif exchange == "xoom":
            return Xoom().get_amount()
        elif exchange == "list":
            return {"list": [
                Xoom().meta_data(),
                Remitly().meta_data()
            ]}
        elif exchange == "all":
            return jsonify({
                'xoom': Xoom().get_amount(),
                'remitly': Remitly().get_amount()
            })
        else:
            return {"bad request": "Wrong endpoint"}


api.add_resource(Exchange, '/exchange/<string:exchange>')

if __name__ == '__main__':
    app.run(debug=True)
