

from flask import Flask
from flask import jsonify


app = Flask(__name__)



def calculator(num):
    if str(num).isnumeric():
        return (True,int(num)*2)
    else:
        return (False,"please give me a number!")
    


@app.route('/calculator/<number>')
def hello(number):
    res=calculator (number)
    if res[0]:
        return jsonify({ "message":"ok" , "calculation_result" : res[1] })
    return jsonify({ "message":"Err" , "calculation_result" : str(res[1]) })
    
        
@app.route('/test')
def test():
    return "Works!"
    
