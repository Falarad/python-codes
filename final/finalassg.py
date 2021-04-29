from flask import *
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'host':"mongodb+srv://Xerxes:SnFMtKOI18croJag@metaverse.2ydnc.azure.mongodb.net/XNN?retryWrites=true&w=majority"}
db = MongoEngine()
db.init_app(app)

class Articles(db.Document):
    title = db.StringField()
    body = db.StringField()
    likes = db.IntField()

class Tips(db.Document):
    email = db.StringField()
    subject = db.StringField()
    body = db.StringField()

class Link():
    def __init__(self, url, text):
        self.link = url
        self.text = text

app.run()
navigation = [Link('/', 'Home'), Link('/contact', 'Contact Us'), Link('/submit', 'Submit an article'), Link('/news', 'All News')]

@app.route('/')
def index():
    featured = Articles.objects().order_by('-likes').first()
    return render_template('index.jinja', navigation=navigation, title=featured.title, body=featured.body, likes=featured.likes)

@app.route('/news')
def news():
    news = Articles.objects().order_by('-likes')
    return render_template('news.jinja', navigation=navigation, news=news)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'GET':
        return render_template('contact.jinja', navigation=navigation)
    else:
        Tips(email=request.form['email'], subject=request.form['subject'], body=request.form['body']).save()
        return redirect(url_for('index'))

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template('article.jinja', navigation=navigation)
    else:
        Articles(title=request.form['title'], body=request.form['body'], likes=0).save()
        return redirect(url_for('index'))
