from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://billy@localhost/testdb'
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Tariff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120), unique=True, nullable=False)
    tariff_metadata = db.Column(db.JSON(80), unique=False, nullable=True)

    def __repr__(self):
        return '<Tariff %r>' % self.description

    def __init__(self, description, tariff_metadata):
        self.description = description
        self.tariff_metadata = tariff_metadata


@app.route("/tariff", methods=["POST"])
def add_tariff():
    description = request.json['description']
    tariff_metadata = request.json['tariff_metadata']

    new_tariff = Tariff(description, tariff_metadata)

    db.session.add(Tariff)
    db.session.commit()

    return jsonify(new_tariff)


@app.route("/tariff", methods=["GET"])
def get_all_tariffs():
    all_tariffs = Tariff.query.all()
    return jsonify(all_tariffs)


if __name__ == '__main__':
    app.run(debug=True)
