from flask import Flask , request,jsonify

app=Flask(__name__)
@app.route('/try', methods=['Get' , 'POST'])
def add():
    if (request.methods== 'POST'):
        a=request.json['num1']
        b=request.json['num2']
        sum=a+b
        return jsonify(str(sum))
@app.route('/sub',methods=['GET'])
def sub():
    if (request.methods=='GET'):
        s=request.json['num3']
        t=request.json['num4']
        subt=s-t
        return jsonify(str(subt))
if __name__=='__main__':
    app.run()
