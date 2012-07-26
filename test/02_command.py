
import peachpy

class Root(object):
	
	def command(self):
		return "Command"
	command.exposed = True

peachpy.quickstart(Root())
