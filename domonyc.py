"""
	Project domoNYC
	---------------
	
	:copyright: (c) 2013 by Michael Lo
	:All Rights Reserved.
"""

import os
from flask import Flask
#from jinja2 import Environment, PackageLoader
#env = Environment(loader=PackageLoader('domoNYC','templates'))

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Let\'s see how long you have lived in days, minutes and seconds.<br /><iframe width=\'500\' height=\'300\' frameBorder=\'0\' src=\'http://a.tiles.mapbox.com/v3/michaeljlo.map-wlxizy2a.html#4/40.03918647233613/-96.61869964833944\'></iframe>'

@app.route('/map')
def hello():
    return '<iframe width=\'500\' height=\'300\' frameBorder=\'0\' src=\'http://a.tiles.mapbox.com/v3/michaeljlo.map-wlxizy2a.html#4/40.03918647233613/-96.61869964833944\'></iframe>'



if __name__ == '__main__':
	app.run(debug=False)