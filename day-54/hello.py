from flask import Flask
app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
# 
# #hello_world()
#
# if __name__ == "__main__":
#     app.run()


### Python Decorator Function
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()

    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")


def say_greeting():
    print("How are you?")

say_bye()