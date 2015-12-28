#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
just test!!!
"""
__author__ = 'ITsystem'
__mtime__ = '2015/12/21'



import mysql.connector
import json
from flask import  Flask,request,render_template

app=Flask(__name__)
db=mysql.connector.connect(user='root',password='111111',host='192.168.95.14',database='falcon')
db.autocommit
cur=db.cursor()

@app.route("/",methods=["GET","POST"])
def hello():
    sql=''
    if request.method=="POST":
        data=request.json
        try:
            sql="INSERT INTO `stat` (`host`,`mem_free`,`mem_usage`,`mem_total`,`load_avg`,`time`) VALUES('%s', '%d', '%d', '%d', '%s', '%d')" % (data['Host'], data['MemFree'], data['MemUsage'], data['MemTotal'], data['LoadAvg'], int(data['Time']))
            ret=cur.execute(sql)
        except mysql.connector.IntegrityError:
            pass
        # finally:
        #     db.close()
        return "OK"
    else:
        return render_template("mon.html")

@app.route("/data",methods=["GET"])
def getdata():
    cur.execute("SELECT `time`,`mem_usage` FROM `stat`")
    ones= [[i[0]*1000, i[1]] for i in cur.fetchall()]
    # db.close()
    return "%s(%s);" % (request.args.get('callback'), json.dumps(ones))

if __name__=='__main__':
    app.run(host="0.0.0.0",port=8888,debug=True)
