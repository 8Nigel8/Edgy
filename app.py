from flask.cli import load_dotenv

load_dotenv()

import os

from src.main.settings import create_app

env = os.getenv("FLASK_ENV", "development")

app = create_app(env)


@app.route('/')
def health_check():
    return 'Still alive!'


if __name__ == '__main__':
    app.run(debug=True)
