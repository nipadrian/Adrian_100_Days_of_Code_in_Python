from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style = "text-align: center">Hello, World!<h1>'\
           '<p>This is a paragraph.</p>'\
           '<img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fgiphy.com%2Fexplore%2Fcat-and-kitten&psig=AOvVaw0dIeH7mJgH4dVtHFMFZc4o&ust=1734642791362000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCICO1o6esooDFQAAAAAdAAAAABAE" width=200>'

#Different routes using the app.route decorator
@app.route('/bye')
@make_bold
@make_underlined
def bye():

    return "Bye!"

@app.route('/username/<name>/<int:number>')
def greet(name,number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)


### Python Decorator Function
# import time
#
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#
#     return wrapper_function
#
# @delay_decorator
# def say_hello():
#     print("Hello")
#
# @delay_decorator
# def say_bye():
#     print("Bye")
#
#
# def say_greeting():
#     print("How are you?")
#
# say_bye()