from flask import Blueprint, render_template, request, abort, redirect, url_for, flash, current_app, session, jsonify, send_from_directory, make_response
import requests
import json
from flask import Markup
from bson.json_util import dumps
from bson.objectid import ObjectId
import htmlmin
import sass
import random
import datetime


user_pages = Blueprint('user_pages', __name__)


@user_pages.route('/video/android/')
def video_android():
    return render_template("dash.html")


@user_pages.route('/video/ios/')
def video_ios():
    return render_template("hls.html")
