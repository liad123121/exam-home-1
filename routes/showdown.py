from flask import Blueprint, request
from database.mysql import mydb

bp = Blueprint('showdown', __name__)

@bp.route('/showdown', methods=['GET', 'POST'])
def showdown():
    if(request.method == 'GET'):
        cur = mydb.cursor()
        cur.execute('SELECT id FROM access_log ORDER BY id DESC LIMIT 1')
        count = cur.fetchone()
        cur.close()

        if count == None:
            return '0'        

        return f'{count[0]}'