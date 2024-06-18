# app/__init__.py
from flask import Flask, flash
from flask_minify import minify 
from flask_compress import Compress
from datetime import timedelta
from flask_caching import Cache

app = Flask(__name__)
Compress(app)

# Konfigurasi Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
minify(app=app, html=True, js=True, cssless=True, static=True) 

# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
from app import routes, github_stats, page_speed
