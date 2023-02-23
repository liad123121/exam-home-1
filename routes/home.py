from flask import Blueprint, request, make_response
from database.mysql import mydb
import datetime
import socket


bp = Blueprint('homeRoute', __name__)

@bp.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        cur = mydb.cursor()
        clientip = request.remote_addr
        hostname = socket.gethostname()
        internalIP = socket.gethostbyname(hostname)
        
        cur.execute(f"INSERT INTO access_log (date, clientIP, internalIP) VALUES ('{datetime.datetime.now()}', '{clientip}', '{internalIP}')")
        mydb.commit()
        cur.close()


        expires = datetime.datetime.now() + datetime.timedelta(minutes=5)
        res = make_response(internalIP)
        res.set_cookie('internalIP',internalIP,expires=expires)

        return res

