from flask import Flask 
app = flask(__name__)

class Config(object)
    DEBUG = True
    
app.config.from_object(Config)

@app.route('/')
def index()
    return '我的第一个flask程序'
if __name__ == '__main':
    app.run()