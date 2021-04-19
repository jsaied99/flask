import urllib.request
import flask
import json
from flask import request, jsonify
from flask import render_template, redirect
from linkedin import linkedin
from urllib.request import urlopen
import requests
from lxml import html
app = flask.Flask(__name__)
app.config["DEBUG"] = True

TOKEN = ""

@app.route('/', methods=['GET'])
def home():
    if 'code' in request.args:
        code = request.args['code']
        client_id = "78yuk1i7oafw90"
        client_secret = "UHo4QTDPugd9BdRH"
        redirect_uri = "http://localhost:5000"

        s = """https://www.linkedin.com/oauth/v2/accessToken?grant_type=authorization_code&client_id=%s&client_secret=%s&code=%s&redirect_uri=%s""" % (
            client_id, client_secret, code, redirect_uri)
        # return s
        # page = requests.get(s)
        TOKEN = requests.get(s).json()["access_token"]
        application = linkedin.LinkedInApplication(token=TOKEN)


        # linkedin_all()
        # print(application.get_profile())
        return application.get_profile()

    url = "https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=78yuk1i7oafw90&scope=r_liteprofile&state=123456&redirect_uri=http://localhost:5000"
    return redirect(url)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/code', methods=['GET'])
def linkedin_all():
    # code = request.args['code']
    # client_id = "78yuk1i7oafw90"
    # client_secret = "UHo4QTDPugd9BdRH"
    # redirect_uri = "http://localhost:5000/code"

    # s = """https://www.linkedin.com/oauth/v2/accessToken?grant_type=authorization_code&client_id=%s&client_secret=%s&code=%s&redirect_uri=%s""" % (
    #     client_id, client_secret, code, redirect_uri)
    # return data

    # application = linkedin.LinkedInApplication(token=TOKEN)

    # if 'code' in request.args:
    #     token = request.args['code']
    #     application = linkedin.LinkedInApplication(token=token)
    # return str(application.get_profile())
    return TOKEN


app.run()
