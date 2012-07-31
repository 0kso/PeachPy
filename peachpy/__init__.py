
import sys

def quickstart(app):
	'App launcher'
	if len(sys.argv) <= 1:
		print app.index()
	else:
		target = app.__getattribute__(sys.argv[1])
		try:
			print target.__call__(*sys.argv[2:])
		except AttributeError, e:
			print target.index()

def expose(method):
	'@peachpy.expose decorator'
	method.exposed = True
	return method