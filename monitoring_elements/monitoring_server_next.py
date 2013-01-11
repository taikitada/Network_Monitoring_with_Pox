'''
monitoring_server_next

'''
import rpyc
from collections import defaultdict
import ConfigParser
import sys,os
from os import path

CURRENT_DIR=path.dirname(os.path.abspath(__file__))
sys.path.append(CURRENT_DIR + '/' + "../")

# [k.dpid][j.dpid]->distance
# overlapping is nothing
# [switchA][switchB] or [switchA][switchB] is included
link_distance = defaultdict(lambda:defaultdict(lambda:None))

# switch_dpid -> (agent_ip, agent_port)
agent_switch_map = {}

from lib.ConfigParserExtend import *
CP = ConfigParserExtend("server.conf")
ConfigDict = CP.ReturnConfigDict()

class Monitoring_Server(rpyc.Service):
	def exposed_register_agent(self, server_ip, server_port, switch_dpid):
		agent_switch_map[switch_dpid] = (server_ip, server_port)
		print agent_switch_map
		if switch_dpid not in link_distance.keys():
			if link_distance.keys() == []:
				link_distance[switch_dpid] = {}
			else:
				for registered_switch in link_distance.keys():
					distance = get_distance_rtt(switch_dpid, registered_switch)
					print switch_dpid, registered_switch, distance
					distance_for_pox = int(distance*1000)
					link_distance[switch_dpid][registered_switch] = distance_for_pox
					print link_distance
			return "Registerd you"

		else:
			return "You already registerd"

	def exposed_request_link_distance(self):
		changed_to_dict = {}
		for a in link_distance.keys():
			changed_to_dict[a]={}
			for b, c in link_distance[a].items():
				(changed_to_dict[a]).update({b:c})
		return changed_to_dict

	def on_connect(self):
		print "made a connection with Monitoring_Server"

	def on_disconnect(self):
		print "A connection is dropped."


if __name__ == '__main__':
	from rpyc.utils.server import ThreadedServer
	print int(ConfigDict['Monitoring_Server']['port'])
	s = ThreadedServer(Monitoring_Server, port = int(ConfigDict['Monitoring_Server']['port']))
	s.start()
