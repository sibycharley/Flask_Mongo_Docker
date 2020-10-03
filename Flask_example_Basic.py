#Importing the Flask package
from flask import Flask, request, jsonify 

#Instantiating the Flask app
app = Flask(__name__)

#Defining the route with default 'GET' method
@app.route('/')
def test():
	return "Welcome to test code"

#Defining the route with 'POST' method
@app.route('/cal', methods=['POST'])
def math():
	
	#Parsing the arguments
	a = request.args.get("num1", 1)
	b = request.args.get("num2", 2)

	#Operation
	res_sum = a + b
	res_sub = a - b
	res_mul = a * b
	res_div = (a/b)

	#Json formatted return results
	return jsonify({"sum": res_sum, "sub": res_sub, "mul": res_mul, "div": res_div })	

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)