from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    temperature = db.Column(db.String(20), nullable=False)


db.create_all()


@app.route('/', methods=['GET'])
def main():
    return render_template('main.html', days=Day.query.all())


@app.route('/add_tmp', methods=['POST'])
def add_tmp():
    text = request.form['text']
    temperature = request.form['temperature']

    db.session.add(Day(text=text, temperature=temperature))
    db.session.commit()

    return redirect(url_for('main'))


@app.route('/delete_tmp', methods=['POST'])
def delete_tmp():
    text = request.form['text']

    db.session.delete(Day.query.filter_by(text=text).first())
    db.session.commit()

    return redirect(url_for('main'))


@app.route('/get_days')
def show_days_temperature():
    return render_template('days.html', days=Day.query.all())


@app.route('/delete', methods=['GET'])
def delete_day():
    return render_template('delete_day.html', days=Day.query.all())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
