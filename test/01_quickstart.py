
import peachpy

class Root(object):
	
	def index(self):
		return "Hello"
	index.exposed = True

peachpy.quickstart(Root())
