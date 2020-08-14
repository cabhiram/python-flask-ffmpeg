import sys, os, json
sys.path.append('../')
sys.path.append('../../')
sys.path.append('../lib/')

from flask import Flask, session, current_app
from flaskext.markdown import Markdown
from flask_mobility import Mobility
from flask_session import Session
from flask_mobility.decorators import mobile_template
from pymongo import MongoClient
from .user_pages import user_pages


def create_app():
    flaskapp = Flask("flask-video-stream")
    client = MongoClient('mongodb://localhost:27017/')
    flaskapp.db = client.flaskvideostream
    flaskapp.debug = True
    
    flaskapp.register_blueprint(user_pages)

    return flaskapp



flask_video_stream = create_app()
