from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from config import DefaultConfig


def configure_app(app, config=None):
    if config:
        app.config.from_object(config)
    else:
        app.config.from_object(DefaultConfig)


def create_app(config=None, app_name=None):
    if app_name is None:
        app_name = DefaultConfig.PROJECT

    app = Flask(__name__, instance_relative_config=True)
    configure_app(app, config)

    return app


app = create_app()
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Tariff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120))
    tariff_metadata = db.Column(db.JSON(80))

    def __repr__(self):
        return '<Tariff %r>' % self.description

    def __init__(self, description, tariff_metadata):
        self.description = description
        self.tariff_metadata = tariff_metadata


@app.route("/tariff", methods=["POST"])
def add_tariff():
    print(request.json)
    description = request.json['description']
    tariff_metadata = request.json['tariff_metadata']

    new_tariff = Tariff(description, tariff_metadata)

    db.session.add(new_tariff)
    db.session.commit()

    return jsonify(new_tariff.description)


@app.route("/tariff", methods=["GET"])
def get_all_tariffs():
    all_tariffs = Tariff.query.all()

    return jsonify([tariff.description for tariff in all_tariffs])


if __name__ == '__main__':
    app.run(debug=True)
