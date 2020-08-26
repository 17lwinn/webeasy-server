# the configuration file for the webserver

version = "1.0.0"

# networking options
# host: the IP address the server will run on, will default to your IP if left
# port: the port it will bind to, for glitch.com users we recommend using port 8000
host = "0.0.0.0"
port = "8000"

#-------------------------------------------

# Routes
# Routes written here will be added when the server is run with a specific file
# (-c flag)
# see manual.txt (part II)

from flask import Blueprint
from flask import render_template

urls_blueprint = Blueprint('urls', __name__,)
    
#@urls_blueprint.route('/hi')
#def index():
#  return render_template('welcome.html')
      
#------------------------------------------