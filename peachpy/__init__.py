
import sys

def quickstart(app):
	'App launcher'
	if len(sys.argv) <= 1:
		if app.index.exposed:
			print app.index()
	else:
		target = app.__getattribute__(sys.argv[1])
		if hasattr(target, "exposed"):
			print target.__call__(*sys.argv[2:])
		elif hasattr(target.index, "exposed"):
			print target.index()
		else:
			raise Exception("Unknown action")

def expose(method):
	'@peachpy.expose decorator'
	method.exposed = True
	return method