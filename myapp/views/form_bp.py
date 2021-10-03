from flask import Blueprint, render_template, request, url_for



qr_main = Blueprint('qr_main',__name__)


@qr_main.route('/')
def index_page():

