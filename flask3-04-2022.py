from flask import  Flask , request , jsonify

app= Flask(__name__)

@app.route('/x',methods=['GET','POST'])
def test():
    if (request.method=='POST'):
        a = request.json['num3']
        b = request.json['num4']
        result = a+b
        return jsonify(str(result))

@app.route('/y',methods=['GET'])
def test1_sum():
    if (request.method=='GET'):
        c=request.json['num3']
        d=request.json['num4']
        b=request.json['num5']
        result1 =c-(d+b)
        return jsonify(str(result1))
@app.route('/prash',methods=['GET','POST'])
def interest():
    if (request.method=='POST'):
        p=request.json['P']
        r=request.json['R']
        t=request.json['T']
        result=((p*r*t)/100)
        return jsonify(str(result))
@app.route('/compound',methods=['GET','POST'])
def compound_interest():
    if (request.method=='POST'):
        p=request.json['P']
        r=request.json['R']
        t=request.json['t']
        rest=(p*(1+r/100)**t)
        return jsonify(str(rest))
@app.route('/area',methods=['GET'])
def area_circle():
    if (request.method=='GET'):
        PI=request.json['PI']
        R=request.json['R']
        area=PI*R**2
        return jsonify(str(area))

if __name__ =='__main__':
    app.run(port=8000)