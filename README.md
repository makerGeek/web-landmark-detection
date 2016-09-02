# Web Landmark Detector
## DEMO
	http://codepen.io/anon/pen/BzmRZv
	this was plotted using an output from the web service I created (plotted with plotly.js)

## HOW TO RUN
resolve dependencies:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; see [dependencies.txt](https://github.com/makerGeek/web-landmark-detection/blob/master/dependencies.txt)

cmd:

	cd /path/to/app/root
	python -m CGIHTTPServer 8000
browser:

	http://localhost:8000/cgi-bin/upload.py

#### TO DO:

	the JSON data have been printed manually.
	to have a better and easier to maintain code, it is better to create custom serializable classes for the face that have as attributes the detected points (check out http://www.diveintopython3.net/serializing.html#json-dump)
