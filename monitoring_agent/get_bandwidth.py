import subprocess
import os
import sys
import ssh


def server_start(self):
	cmdline="./netserver"
	svr_ps = subprocess.Popen(cmdline, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
	(stdouterr, stdin) = (svr_ps.stdout, svr_ps.stdin)
	line = stdouterr.readline()
	ret = svr_ps.wait()
	return ret
#	def server_stop():

def client_start(self, dest_ip):
	cwd_tmp = "/Users/taikitada/local_work"
	cmdline = "./netperf -H  " + str(dest_ip)
	svr_ps = subprocess.Popen(cmdline, cwd=cwd_tmp, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
	(stdouterr, stdin) = (svr_ps.stdout, svr_ps.stdin)
	data_list = []
	while True:
		line = stdouterr.readline()
		if not line:
			break
		data_list.append(line.rsplit())
	bandwidth = data_list[-1][-1]
	ret = svr_ps.wait()
	return bandwidth, ret