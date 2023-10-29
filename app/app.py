from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db/postgres'
db = SQLAlchemy(app)

# モデルの定義
class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    text = db.Column(db.String(500))

@app.route('/')
def index():
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        entry = Entry(title=title, text=text)

        db.session.add(entry)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_entry(id):
    entry = Entry.query.filter_by(id=id).first_or_404()

    if request.method == 'POST':
        entry.title = request.form['title']
        entry.text = request.form['text']

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', entry=entry)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_entry(id):
    entry = Entry.query.filter_by(id=id).first_or_404()

    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
