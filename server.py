from flask import Flask, render_template, request, url_for, redirect
from fake_news_model import fake_news_model

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/fake_news/')
def fake_news():
    return render_template('fake_news.html', fake = "")

@app.route('/new', methods=['POST'])
def new():
    title = request.form['title']
    text = request.form['text']
    fake_news = fake_news_model(title,text);
    fake = str(fake_news.isFake())
    return render_template('fake_news.html', fake=fake)

if __name__ == '__main__':
    app.run(debug=True)