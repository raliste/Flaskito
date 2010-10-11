from flask import Module
from flask import request, session, g, render_template, redirect, abort, url_for

front = Module(__name__)

@front.route('/')
def index():
    return 'Hi world :)'
