from flask import Flask, request,jsonify
app=Flask(__name__)
@app.route('/n',methods =['GET','POST'])
def addition ():
    if (request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        sum=a+b
        return jsonify(str(sum))
if __name__=="__main__":
    app.run()


