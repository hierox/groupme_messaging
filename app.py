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
    
    # it probably would be better design to read this in from a file or database, but i'm lazy
    scotch_list = []
    scotch_list.append("1792 Full Proof Total Wine Barrel Pick (Jar 1/A)")
    scotch_list.append("Clyde May's Special Reserve (Jar 2/B)")
    scotch_list.append("Bunnahabhain 12 (Jar 3/C)")
    scotch_list.append("New Richmond Rye (Jar 4/D)")
    scotch_list.append("Port Charlotte 10 year (Jar 5/E)")
    scotch_list.append("Glenmorangie 14 yr Quinta Ruban (Jar 6/F)")
    scotch_list.append("Willet Straight Rye Whiskey (Jar 7/G)")
    scotch_list.append("Tattersall Straight Wheat Whiskey (Jar 8/H)")
    scotch_list.append("Barrell Whiskey Private Release  (Jar 9/I)")
    scotch_list.append("Loonshine whiskey  (Jar 10/J)")
    scotch_list.append("Tomatin Cu Bocan (Jar 11/K)")
    scotch_list.append("n/a (Rest Day #1)")
    scotch_list.append("Glenglassaugh Portsoy (Jar 13/M)")
    scotch_list.append("Dampfwerk American Single Malt Whiskey (Jar 14/N)")
    scotch_list.append("Noah's Mill Bourbon Whiskey (Jar 15/O)")
    scotch_list.append("Wild Turkey Rare Breed barrel proof (Jar 16/P)")
    scotch_list.append("Alex Murray Highland 10yr 2011 (Jar 17/Q)")
    scotch_list.append("jura seven wood  (Jar 18/R)")
    scotch_list.append("Surprise Whiskey!!!!!!!!! Super Blind Taste test! (Jar 19/S)")
    scotch_list.append("n/a (Rest Day #2)")
    scotch_list.append("Driftless Glen single barrel rye (Jar 21/U)")
    scotch_list.append("Glengoyne 12 (Jar 22/V)")
    scotch_list.append("The balvenie doublewood (Jar 23/W)")
    scotch_list.append("Shieldaig 12 Rum Cask Finish (Jar 24/X)")

    # get todays date - US central is 6 hours behind UTC
    today = datetime.datetime.today() - datetime.timedelta(hours=6)
    print("Date: ", today)

    # only output when we want the advent calendar to run
    if (today.year != 2023): # we don't want this running next year
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