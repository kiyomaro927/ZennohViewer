import json
import urllib2

data = { 
    "cells":["ECT","VISC", "AAA"]
}

req = urllib2.Request('http://localhost:5000/api')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))