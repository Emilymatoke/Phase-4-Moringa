from flask import Flask

#tag
app = Flask(__name__)

#define routes using route decorators
@app.route('/')
def hello_world() :
    return 'Hello, world!'

@app.route('/welcome')
def welcome_message():
    return 'Welcome to my app. Need a tour?'


if __name__ == '__main__' :
    app.run()



'''HOW FLASK WORKS UNDER THE HOOD
1. Routing- defines url routes and associate them with functions
-creates MVT(Models- data holders, Views- functions to work on the data, Templates- (views))= software architecture pattern
2. Request handling- matching url requests and executing corresponding
3. Template- Flask allows generation of HTML elements
4. Extensions- add additional functionality

TODOLIST
1. Restful API app
2. Ecommerce store
3. Blog app '''