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
    scotch_list.append("Lagavulin 8 (Jar 1/A)")
    scotch_list.append("Talisker Storm (Jar 2/B)")
    scotch_list.append("Glenlivet 12 (Jar 3/C)")
    scotch_list.append("Oban Little Bay (Jar 4/D)")
    scotch_list.append("Monkey Shoulder Batch 27 (Jar 5/E)")
    scotch_list.append("Tullibardine 12 (Jar 6/F)")
    scotch_list.append("Aucentoshan 3 wood (Jar 7/G)")
    scotch_list.append("Glenfiddich 12 (Jar 8/H)")
    scotch_list.append("Ardbeg Corryvreckan (Jar 9/I)")
    scotch_list.append("Ardbeg Uigeadail (Jar 10/J)")
    scotch_list.append("Smokehead High Voltage (Jar 11/K)")
    scotch_list.append("Glenmorangie 10 (Jar 12/L)")
    scotch_list.append("Springbank 15 (Jar 13/M)")
    scotch_list.append("Aberfeldy 12 (Jar 14/N)")
    scotch_list.append("Auchentoshan Single 12 (Jar 15/O)")
    scotch_list.append("Creag Isle 12 Single Malt (Jar 16/P)")
    scotch_list.append("Macallan 12 Double Cask (Jar 17/Q)")
    scotch_list.append("Kilchoman (Jar 18/R)")
    scotch_list.append("Edradour 10 (Jar 19/S)")
    scotch_list.append("Lagavulin 9 (Jar 20/T)")
    scotch_list.append("Glen Fohdry 12 (Jar 21/U)")
    scotch_list.append("Grangestone Bourbon Cask Finish (Jar 22/V)")
    scotch_list.append("Jura 10 (Jar 23/W)")
    scotch_list.append("Redbreast (Jar 24/X)")

    # get todays date - US central is 6 hours behind UTC
    today = datetime.datetime.today() - datetime.timedelta(hours=6)
    print("Date: ", today)

    # only output when we want the advent calendar to run
    if (today.year != 2022): # we don't want this running next year
        return
    # if (today.month != 12): # start in december
    #    return
    if (today.day < 1):
        return
    if (today.day > len(scotch_list)):
        return

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