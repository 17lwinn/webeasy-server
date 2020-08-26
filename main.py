#!/usr/bin/env python

# ProTech WebEasy Server project
# copyright, 2020. All rights reserved

import os
import time
import argparse
import webserver_config as config


parser = argparse.ArgumentParser(prog='python3 main.py', description='EasyWeb server, serve your files easily')
parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + config.version, help='view the CLI version')
parser.add_argument('-c', '--customfile', metavar='<filename>.html', help='Serve a specific html file (must be located inside templates folder)');

args = parser.parse_args()


# run server (python main.py -c hello.html):
#
# This is ran when command line params are specified, you'll still need to set your
# variables in webserver_config.py!!!
# specific files must be in the templates folder, or flask will start spewing errors
#-------------------------------------------------


if args.customfile:
  file = args.customfile
  print("Attempting to serve the file specified by you")
  def run_specific():

      from flask import Flask
      from flask import render_template
      from webserver_config import urls_blueprint

      server = Flask(__name__)
      server.register_blueprint(urls_blueprint)
    
      @server.route("/")
      def hello():
          return render_template(file)
        
      @server.errorhandler(404) 
      def not_found(e): 
        return render_template(".404.html")
        
  # run the application
      print("starting server via flask...")
      server.run(host=config.host, port=config.port)
      
  run_specific()

#-------------------------------------------------


# run server (python main.py):
#
# This is ran when no command line params are specified, you'll still need to set your
# variables in webserver_config.py!!!
#-------------------------------------------------

def run_plain():

    from flask import Flask
    from flask import render_template
    from flask import request
    
    server = Flask(__name__)
  
    @server.route("/")
    def hello():
        return render_template('welcome.html')
      
    @server.route("/service")
    def status():
        import platform
        systemos = platform.platform()
        version = config.version
        network = config.port, config.host
        pyversion = platform.python_version()
        return render_template('.service.html', os=systemos, version=version, network=network, pyversion=pyversion)
    
    
    @server.errorhandler(404) 
    def not_found(e): 
        return render_template(".404.html")
        

# run the application
    print("starting server via flask...")
    server.run(host=config.host, port=config.port)
    
#--------------------------------------------------

if __name__ == "__main__":
  run_plain()