from flask import Flask,request
import datetime
import demjson

from DBConnection import Db
app = Flask(__name__)
db=Db()


@app.route('/a')
def a():
    return ("hiii")

@app.route('/login',methods=['post'])
def login():

    db=Db()
    usr=request.form['username']
    passwd=request.form['password']
    qry="SELECT * FROM login WHERE NAME='"+usr+"'AND passwd='"+passwd+"'"
    res=db.selectOne(qry)
    res1={}
    if res!=None:
        type=res['type']
        if type=="admin":
            res1['status']="none"
            return demjson.encode(res1)
        else:
            id=res['loginid']
            res1['status']='ok'
            res1['type']=type
            res1['lid']=id
            return demjson.encode(res1)
    else:
        res1['status'] = 'none'
        return demjson.encode(res1)



if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True,port=4000)