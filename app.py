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
    scotch_list.append("Tamnavulin Sherry Cask Single Malt Whisky (Jar 1/A)")
    scotch_list.append("Rough Rider The Big Stick Rye (Jar 2/B)")
    scotch_list.append("Aberlour 12 Year (Jar 3/C)")
    scotch_list.append("Laphroaig 10 Year (Jar 4/D)")
    scotch_list.append("Arran 10 Year (Jar 5/E)")
    scotch_list.append("Yamato Japanese Whisky Mizunara Cask (Jar 6/F)")
    scotch_list.append("Basil Hayden Small Batch (Jar 7/G)")
    scotch_list.append("Lagavulin 11 Year - Offerman Edition (Jar 8/H)")
    scotch_list.append("Del Bac Dorado (Jar 9/I)")
    scotch_list.append("Du Nord Mixed Blood Whiskey (Jar 10/J)")
    scotch_list.append("Keeper's Heart Irish Whiskey (Jar 11/K)")
    scotch_list.append("Benriach The Smoky 12 (Jar 12/L)")
    scotch_list.append("Vikre - Honor Brand Hay and Sunshine (Jar 13/M)")
    scotch_list.append("Craigellachie Single Malt Scotch Whisky (Jar 14/N)")
    scotch_list.append("Elijah Craig 8 Year Private Barrel (Jar 15/O)")
    scotch_list.append("Balvenie Doublewood 12 (Jar 16/P)")
    scotch_list.append("Connemara (Jar 17/Q)")
    scotch_list.append("Glinfiddich \"Solera\" 15 (Jar 18/R)")
    scotch_list.append("Lagavulin 8 Year (Jar 19/S)")
    scotch_list.append("Suntory Whisky Toki (Jar 20/T)")
    scotch_list.append("Nikka Coffey Grain (Jar 21/U)")
    scotch_list.append("Balcones Brimstone (Jar 22/V)")
    scotch_list.append("Chankaska Ranch Road Nut Brown (Jar 23/W)")
    scotch_list.append("Amrut Indian Single Malt (Jar 24/X)")

    # get todays date - US central is 6 hours behind UTC
    today = datetime.datetime.today() - datetime.timedelta(hours=6)
    print("Date: ", today)

    # only output when we want the advent calendar to run
    if (today.year != 2022): # we don't want this running next year
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