#/usr/bin/python

# How to Use
# 
#
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-s', type=str, dest='slice_name')
parser.add_argument('-m', type=str, dest='mac_addr')
args = parser.parse_args()

import sqlite3
conn = sqlite3.connect("slice.db", isolation_level=None)
sql = "insert into vc_slice values('" + args.slice_name + "', '" + args.mac_addr + "')"
conn.execute(sql)
conn.close()
