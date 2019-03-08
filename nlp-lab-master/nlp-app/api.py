from __future__ import print_function
from EWS import main_ews, demos
import sys
import os
import csv
import zerorpc

class EwsApi(object):
    def ews(self, filepath):
        rows = []

        db = csv.reader(open(filepath, mode="rt"), delimiter=",")
        
        for row in db:
            rows.append(row[0])

        return main_ews(rows)

def parse_port():
    return 4242

def main():
    addr = 'tcp://127.0.0.1:' + str(parse_port())
    s = zerorpc.Server(EwsApi())
    s.bind(addr)
    print('start running on {}'.format(addr))
    s.run()

if __name__ == '__main__':
    main()
