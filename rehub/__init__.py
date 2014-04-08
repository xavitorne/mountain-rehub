from flask import Flask

app = Flask(__name__)
from rehub import views
