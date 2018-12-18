# -*- coding:utf-8 -*-

import os, sys
import time, re

startime = time.clock()
print 'startime is %s', startime

v = raw_input('eg: xx.xx,xx.xx or xx.xx;xx.xx')
ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', str(v))
for i in ip:
    print '输入的IP地址为：%s' % (i)

ipfirewall = r'/Users/vicent/Documents/ipfirewall'
tmp = r'/Users/vicent/Documents/tmp'
fread = open(ipfirewall, mode='r')


def inser_rule():
    global x
    for x in ip:
        if not re.findall(r'-s.+x.+-p', srctext):
            srclist.insert(-23, 'iptables -I INPUT -s\t%s\t-p TCP --dport 8080 -j ACCEPT\n'.format(x))
    fwrite.writelines(srclist)


with open(tmp, mode='w') as fwrite:
    srclist = fread.readlines()
    fread.seek(0, 0)
    srctext = fread.read()
    tody = '#' + str(time.strftime('%Y-%m-%d', time.localtime()) + '\n')
    if tody in srclist:
        # add iptable rule into the file before ACCEPT ALL
        inser_rule()
    else:
        print 'Add date note'
        srclist.insert(-23, '#' + str(time.strftime('%Y-%m-%d', time.localtime())) + '\n')
        inser_rule()

fread.close()
#os.system()
print time.clock() - startime
