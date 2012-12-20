import subprocess
import sys

def get_datapath_id(bridge):

        cmd="sudo ovs-ofctl show " + bridge
        svr_ps = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
        stdouterr = svr_ps.stdout

        return_code = svr_ps.wait()
        if return_code == 1:
                print bridge + " is not found or Faild sudo authentication"
                sys.exit()
        else: # sucessfull execute command
                output_data = []
                while True:
                        line = stdouterr.readline()
                        # print line
                        if not line:
                                break
                        elif line[0]=="ovs-ofctl" :
                                return bridge + " is not found"
                        output_data.append(line.split())
                datapath_id = (output_data[0][3]).split(":")
                return datapath_id[1]


def datapath_id_for_pox(bridge):
        datapath_ID = get_datapath_id(bridge)
	return datapath_ID[4:]

if __name__=='__main__':
        print get_datapath_id("bridge_name")
