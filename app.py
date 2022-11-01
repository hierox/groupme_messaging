#!/usr/bin/env python
import json
import os
import requests
import time

from flask import Flask
app = Flask(__name__)

@app.route('/', methods=["GET"])
def get_hello():
    return ("Hello, Get", 200)

@app.route("/", methods=["POST"])
def post_hello():
    return ("Hello, Post", 200)

@app.route("/Scotch", methods=["GET"])
def scotch_hello_get():
    return ("Hello, Scotch Get", 200)

@app.route("/Scotch", methods=["POST"])
def scotch_hello_post():
    return ("Hello, Scotch Post", 200)

@app.route("/Trivia", methods=["GET"])
def trivia_hello_get():
    return ("Hello, Trivia Get", 200)

@app.route("/Trivia", methods=["POST"])
def trivia_hello_post():
    return ("Hello, Trivia Post", 200)
