
import sys

def quickstart(app):
	if len(sys.argv) <= 1:
		print app.index()
	else:
		print app.__getattr__(sys.argv[1])
