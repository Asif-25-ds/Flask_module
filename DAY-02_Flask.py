from flask import Flask
from flask import request
app=Flask(__name__)

@app.route("/")
def helloworld():
    return "<h1>Hello,World !</h1>"

@app.route("/1")
def helloworld1():
    return "<h1>Hello,World Asif!</h1>"

@app.route("/2")
def helloworld2():
    return "Hello,World Asif Raza !"

@app.route("/test")
def test():
    data=request.args.get('x')
    return "Hii you inputted your data in browser url portion \nAfter route ?your data {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")