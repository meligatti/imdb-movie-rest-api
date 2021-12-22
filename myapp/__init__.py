from flask import Flask

# Init app
app = Flask(__name__)

#import myapp.routes as routes
from myapp.routes import *
