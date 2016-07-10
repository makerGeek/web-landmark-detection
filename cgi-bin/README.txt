service accessible via :
	http://localhost:8000/cgi-bin/getDimensions.py?image=face.jpg
as of now it works with a single (hardcoded) image : face.jpg

## HOW TO RUN
cmd:
	cd /path/to/app/root
	python -m CGIHTTPServer 8000
browser:
	http://localhost:8000/cgi-bin/getDimensions.py?image=face.jpg