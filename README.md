##DEMO
	http://goo.gl/j6iGMw
	http://codepen.io/anon/pen/BzmRZv
	this was plotted using an output from the web service I created (with plotly.js)

service accessible via :
	http://localhost:8000/cgi-bin/upload.py

## HOW TO RUN
cmd:
	cd /path/to/app/root
	python -m CGIHTTPServer 8000
browser:
	http://localhost:8000/cgi-bin/upload.py

the get_landmarks.py works as follows:
	./get_landmarks.py ../tmp

TO DO:
	the JSON data have been printed manually.
	to have a better and easier to maintain code, it is better to create custom serializable classes for the face that have as attributes the detected points (check out http://www.diveintopython3.net/serializing.html#json-dump)
