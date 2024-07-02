from flask import Flask
from src.main.models.models import db, Collection
from src.main.models.schemas import collection_schema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db.init_app(app)

with app.app_context():
    db.create_all()

    data = {
        'name': 'abcd',
        'description': 'b'
    }

    collection = collection_schema.load(data, session=db.session)


    print(collection_schema.dumps(collection))