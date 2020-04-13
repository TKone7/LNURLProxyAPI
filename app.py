from flask import Flask, request
from flask_restful import Api
from database import db

from resources.lnurl import LnurlCreate, LnurlAwait, LnurlRequest, LnurlWithdraw

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "Thisisfornowmysecretkey"

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(LnurlCreate, "/v1/lnurl")
api.add_resource(LnurlAwait, "/v1/lnurl/<string:uuid>/await-invoice")
api.add_resource(LnurlRequest, "/v1/lnurl/<string:uuid>")
api.add_resource(LnurlWithdraw, "/v1/lnurl/<string:uuid>/withdraw")

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)