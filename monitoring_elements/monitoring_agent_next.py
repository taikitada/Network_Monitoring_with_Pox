import rpyc
from rpyc.utils.ssh import SshContext
import ConfigParser
import sys,os
from os import path

CURRENT_DIR=path.dirname(os.path.abspath(__file__))
sys.path.append(CURRENT_DIR + '/' + "../")

from lib.get_datapath_id import datapath_id_for_pox
from lib.get_rtt import get_rtt
from lib.ConfigParserExtend import *
CP = ConfigParserExtend("server.conf")
ConfigDict = CP.ReturnConfigDict()

class Monitoring_Agent(rpyc.Service):
	def on_connect(self):
		print "made a connection with Monitoring_Server"

	def on_disconnect(self):
		print "A connection is dropped."

	def exposed_get_rtt(self, dest_host):
		return get_rtt(dest_host)


if __name__ == '__main__':
	switch_dpid = datapath_id_for_pox(ConfigDict['Switch']['switch'])
	sshctx = SshContext(ConfigDict['Monitoring_Server']['host'],
							ConfigDict['Monitoring_Server']['user'],
							port = None,
							keyfile = ConfigDict['Monitoring_Server']['keyfile'])
	print self.sshctx
	conn = rpyc.ssh_connect(sshctx, int(ConfigDict['Monitoring_Server']['port']))
	print (conn).root.register_agent(ConfigDict['Monitoring_Agent']['host'],
										ConfigDict['Monitoring_Agent']['port'], switch_dpid)
	from rpyc.utils.server import ThreadedServer
	s = ThreadedServer(Monitoring_Agent, port = int(ConfigDict['Monitoring_Agent']['port']))
	s.start()

