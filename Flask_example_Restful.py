#Importing the Flask package
from flask import Flask, request, jsonify 
from flask_restful import Api, Resource

#Instantiating the Flask app
app = Flask(__name__)
api = Api(app)

class TestGet(Resource):

	#Defining the 'GET' method
	def get(self):
		return "Welcome to test code"

class TestPost(Resource):

	#Defining the route with 'POST' method
	def post(self):
	
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

api.add_resource(TestGet, '/')
api.add_resource(TestPost, '/cal')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)