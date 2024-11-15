#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Prints the string in the console
    return parameter  # Returns the string to display in the browser

@app.route('/count/<int:parameter>')
def count(parameter):
    # Generate a list of numbers formatted with newlines
    numbers = map(str, range(parameter))
    return '\n'.join(numbers) + '\n', 200, {'Content-Type': 'text/plain'}


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1,operation,num2):
    if operation=="+":
        result= num1+num2
    elif operation=="-":
        result= num1-num2
    elif operation=="*":
        result =num1*num2
    elif operation =="div":
       if num2!=0:
           result=num1/num2
       else:
           return "num1 cant be 0"

    elif operation =="%":
        if num1!=0:
            result= num1%num2
        else:
            return"num1 can't be 0"  
    else: 
        return "error"  
    return str(result)  
           

    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
