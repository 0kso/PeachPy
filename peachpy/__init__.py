
import sys

def quickstart(app):
	'App launcher'
	if len(sys.argv) <= 1:
		print app.index()
	else:
		print app.__getattr__(sys.argv[1])

def expose(method):
	'@peachpy.expose decorator'
	method.exposed = True
	return method