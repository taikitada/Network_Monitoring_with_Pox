# how to use
#
# for running this performance monitoing server
#
# $ python performance_monitor_server.py -pm 10.1.1.3:8000
# "-pm option" means Monitoring Server running on the IP and Port.
#

import xmlrpclib
import sys
from collections import defaultdict
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import logging
import logging.config

LEVELS = {'debug': logging.DEBUG,
		'info': logging.INFO,
		'warning': logging.WARNING,
		'error': logging.ERROR,
		'critical': logging.CRITICAL}

import argparse
parser = argparse.ArgumentParser(description='sample argument')
parser.add_argument('-pm', type=str, dest='perfomance_mamager')
args = parser.parse_args()

# [k.dpid][j.dpid]->distance
# overlapping is nothing
# [switchA][switchB] or [switchA][switchB] is included
link_distance = defaultdict(lambda:defaultdict(lambda:None))

# switch_dpid -> (agent_ip, agent_port)
agent_switch_map = {}


# get distance with datapath_id
def get_distance_rtt(dpid_1, dpid_2):
	agent_server = xmlrpclib.ServerProxy("http://" + agent_switch_map[dpid_2][0] + ":" + agent_switch_map[dpid_2][1])
	return agent_server.get_rtt(agent_switch_map[dpid_1][0])

def get_bandwidth(dpid_1, dpid_2):
	agent_server_1 = xmlrpclib.ServerProxy("http://" + agent_switch_map[dpid_1][0] + ":" + agent_switch_map[dpid_1][1])
	agent_server_2 = xmlrpclib.ServerProxy("http://" + agent_switch_map[dpid_2][0] + ":" + agent_switch_map[dpid_2][1])
	agent_server_2.start_server()
	return agent_server_1.get_bandwidth()

class Performance_Monotoring:
	def __init__(self):
		pass

	def register_agent(self, server_ip, server_port, switch_dpid):
		agent_switch_map[switch_dpid] = (server_ip,server_port)
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

	def request_distance(self, switchA, switchB):
		print switchA, switchB
		if link_distance[switchA][switchB] == None:
			print link_distance[switchB][switchA]
			return link_distance[switchB][switchA]
		print link_distance[switchA][switchB]
		return link_distance[switchA][switchB]

	def request_link_distance(self):
		changed_to_dict = {}
		for a in link_distance.keys():
			changed_to_dict[a]={}
			for b, c in link_distance[a].items():
				(changed_to_dict[a]).update({b:c})
		return changed_to_dict

	def show_registerd_slices(self):
		# return to list of keys
		return slice_map.keys()

"""
get client address

"""
class RequestHandler(SimpleXMLRPCRequestHandler):
	def __init__(self, request, client_address, server):
		print client_address# do what you need to do with client_address here
		SimpleXMLRPCRequestHandler.__init__(self, request, client_address, server)


if __name__ == '__main__':
	manager_ip_addr = (args.perfomance_mamager.split(":"))[0]
	manager_port = (args.perfomance_mamager.split(":"))[1]
	server = SimpleXMLRPCServer((manager_ip_addr, int(manager_port)), RequestHandler)
	PM = Performance_Monotoring()
	server.register_instance(PM)
	server.serve_forever()
