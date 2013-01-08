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


class Monitoring_Agent:
	def __init__(self):
		self.sshctx = SshContext(ConfigDict['Monitoring_Server']['host'],
							ConfigDict['Monitoring_Server']['user'],
							port = None,
							ConfigDict['Monitoring_Server']['keyfile'])
		self.conn = rpyc.ssh_connect(self.sshctx, ConfigDict['Monitoring_Server']['port'])
		(self.conn).root.register_agent()
	def ():
		pass

if __name__ == '__main__':



