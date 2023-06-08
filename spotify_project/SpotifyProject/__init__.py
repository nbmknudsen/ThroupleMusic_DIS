import os

import psycopg2
from dotenv import load_dotenv
from flask import Flask
from psycopg2.extras import RealDictCursor

load_dotenv()

app = Flask(__name__)
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

conn = psycopg2.connect(
    host="localhost",
    database=os.getenv('postgres'),
    user=os.getenv('postgres'),
    password=os.getenv('DB_PASSWORD')
)

db_cursor = conn.cursor(cursor_factory=RealDictCursor)
from SpotifyProject import filters
from SpotifyProject.blueprints.routes import Music

app.register_blueprint(Music)