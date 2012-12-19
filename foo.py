from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
import xmlprclib

dpidToIP = {}


class Received_message (Event):
	def __init__ (self, exam):
		Event.__init__(self)
		self.exam = exam
		print "test" + self.exam
		
		"""
		from SimpleXMLRPCServer import SimpleXMLRPCServer
		server = SimpleXMLRPCServer(("localhost", 8000))
		server.register_function(show_data)
		"""

class Sample_Switch (EventMixin):
	
	_eventMixin_events = set ([
		Received_message,
		])
	
	def __init__ (self):
		#self.listenTo(core.openflow, priority=0)
		print "Initialize Sample Switch"
		
class Agent_Monitor (Event):
	def __init__ (self):
		from SimpleXMLRPCServer import SimpleXMLRPCServer
		server = SimpleXMLRPCServer(("localhost", 8000))
		server.register_function




def launch ():
	core.registerNew(Sample_Switch)
	print "Registered Sample_Switch"
	core.registerNew(Agent_Monitor)
	core.Sample_Switch.raiseEvent(Received_message("aaa"))