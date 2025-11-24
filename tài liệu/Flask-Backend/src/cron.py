from .models import Ddns
from . import db
from flask import Flask
from src.utils.ddns import ddnsDynu

def list_to_dict(data):
    list_connect = {}
    for ppp in data:
        list_connect[ppp.get("name")] = ppp.get("address")
    return list_connect

def ddns_dynu(app:Flask):
    with app.app_context():
        all_query = Ddns.query.all()
        for first in all_query:
            resp = ddnsDynu(first).update_ip()
            if resp:
                print(first.name,"update ip",resp.text)