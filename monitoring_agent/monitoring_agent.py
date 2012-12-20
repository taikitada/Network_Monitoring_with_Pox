#
#  python monitoring_agent.py -ms server_IP:port -pm server:port -sw openvswitch_switch_name -nd netperf_dir
#
#
#

from get_rtt import get_rtt
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import sys
from get_datapath_id import datapath_id_for_pox
import xmlrpclib
import argparse

parser = argparse.ArgumentParser(description='sample argument')
parser.add_argument('-ma', type=str, dest='monitoring_agent', required=True, help='server_IP:port_num')
parser.add_argument('-pm', type=str, dest='performance_manager', required=True, help='server_IP:port_num')
parser.add_argument('-sw', type=str, dest='switch', required=True, help='switch_name')
parser.add_argument('-nd', type=str, dest='netperf_dir', required=True, help='write your netperf directory')
args = parser.parse_args()

argvs = sys.argv
#ip_addr, port_num
server_info = ()

class monitoring_agent:
	def __init__(self, server_ip_addr, server_port, switch_dpid):
		monitoring_server = xmlrpclib.ServerProxy("http://"+args.performance_manager)
		print server_ip_addr, server_port, switch_dpid
		print monitoring_server.register_agent(server_ip_addr, server_port, switch_dpid)

	def sample(self):
		return 1111

	def show_slices(self):
		return monitoring_server.show_registerd_slices()

	def add_slice(self, slice_name):
		monitoring_server.register_slice(slice_name)

	def add_mac_to_slice(self, mac_addr, slice_name):
		monitoring_server(mac_addr, slice_name)


class RequestHandler(SimpleXMLRPCRequestHandler):
	def __init__(self, request, client_address, server):
		print client_address# do what you need to do with client_address here
		SimpleXMLRPCRequestHandler.__init__(self, request, client_address, server)

if __name__ == '__main__':
	server_ip_addr = (args.monitoring_agent.split(":"))[0]
	server_port = (args.monitoring_agent.split(":"))[1]
	manager_ip_addr = (args.performance_manager.split(":"))[0]
	manager_port = (args.performance_manager.split(":"))[1]
	switch_dpid = datapath_id_for_pox(args.switch)
	server = SimpleXMLRPCServer((server_ip_addr,int(server_port)),RequestHandler)
	server.register_introspection_functions()
	server.register_instance(monitoring_agent(server_ip_addr, server_port, switch_dpid))
	server.register_function(get_rtt)
	server.serve_forever()
