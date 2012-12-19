import subprocess
import re


def get_rtt(dest_host):
	cmd = "ping " + dest_host
	svr_ps = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
	stdouterr = svr_ps.stdout
	#return_code = svr_ps.wait()
	return_code = 0
	if return_code == 1:
		return dest_host + "is not found"
	else:
		i = 0
		ping_result_list = []
		while True:
			output_data = []
			line = stdouterr.readline()
			#print line
			output_data.append(line.split())
			result = output_data[0][-2].strip("time=")
			#print type(result)
			if i != 0:
				ping_result_list.append(float(result))
				#print ping_result_list
			i += 1
			if i == 5:
				return sum(ping_result_list)/4
				

			if line[0] == "ping":
				break
# TODO expect rtt time from data-set

if __name__=='__main__':
	print get_rtt("localhost")
