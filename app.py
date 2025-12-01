#!/usr/bin/env python
import json
import os
import requests
import datetime
import time

from flask import Flask
app = Flask(__name__)

@app.route("/awaken", methods=["GET"])
def awaken_service():
    # for some reason render.com's dynos aren't very reliable
    # hit this endpoint a few minutes before using the others to make sure service is ready
    return ("ok", 200)

@app.route("/scotch", methods=["POST"])
def scotch_message():
    
    # it probably would be better design to read this in from a file or database
    scotch_list = []
    scotch_list.append("Lost Woods 80 (Jar 1/A)")
    scotch_list.append("Benromach 10 (Jar 2/B)")
    scotch_list.append("Henry McKenna 10 (Jar 3/C)")
    scotch_list.append("Hibiki Suntory Whisky (Jar 4/D)")
    scotch_list.append("Puni Italian Malt Whisky (Jar 5/E)")
    scotch_list.append("Mystery Whisky (Jar 6/F)")
    scotch_list.append("Rest Day 1")
    scotch_list.append("Kaigan Japanese Whisky (Jar 8/G)")
    scotch_list.append("Grangestone 12 (Jar 9/H)")
    scotch_list.append("Mellow Corn (Jar 10/I)")
    scotch_list.append("Toki Suntory Whisky (Jar 11/J)")
    scotch_list.append("First Call Double Oak (Jar 12/K)")
    scotch_list.append("WhistlePig Piggyback (Jar 13/L)")
    scotch_list.append("Lost Woods 80 (again) (Jar 14/M)")
    scotch_list.append("Rest Day 2")
    scotch_list.append("Rest Day 3")
    scotch_list.append("Elijah Craig Toasted Barrel (Jar 17/N)")
    scotch_list.append("Noah's Mill (Jar 18/O)")
    scotch_list.append("Rest Day 4")
    scotch_list.append("Rest Day 5")
    scotch_list.append("Rest Day 6")
    scotch_list.append("Rest Day 7")
    scotch_list.append("Bib Tucker Double Char Bourbon (Jar 23/P)")
    scotch_list.append("Bowmore 12 (Jar 24/Q)")
    scotch_list.append("Infinity Bottle (If not already consumed)")

    # get todays date - US central is 6 hours behind UTC
    today = datetime.datetime.today() - datetime.timedelta(hours=6)
    print("Date: ", today)

    # only output when we want the advent calendar to run
    if (today.year != 2025): # we don't want this running next year
        return ("ok", 200)
    if (today.month != 12): # start in december
        return ("ok", 200)
    if (today.day < 1):
        return ("error", 500)
    if (today.day > len(scotch_list)):
        return ("ok", 200)

    # python is 0 indexed
    scotch = scotch_list[today.day - 1]
    
    # send the message
    return send_message("Today's Scotch is: " + scotch, os.getenv("SCOTCH_GROUP_API_KEY")) 


@app.route("/trivia", methods=["POST"])
def trivia_hello_post():
    return send_message("Like for trivia tonight at 8 at Black Sheep Pizza (North Loop)", os.getenv("TRIVIA_GROUP_API_KEY"))


def send_message(msg, api_key):
    print("sending message: ", msg)

    url = "https://api.groupme.com/v3/bots/post"

    payload = {
        "bot_id": api_key,
        "text": msg
    }

    response = requests.post(url, json=payload)
    return (response.text, response.status_code, response.headers.items())