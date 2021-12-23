from flask import Flask

# Init app
app = Flask(__name__)

from myapp.views import *
