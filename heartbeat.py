#!/bin/python3
import subprocess as sp
import socket as skt
import requests as rq

hostname = skt.gethostname()
IP = skt.gethostbyname(hostname)

def comm(arg1):
    '''issue commands to bash and get stdout'''
    stdout = sp.check_output(arg1, shell=True)
    stdout = stdout.decode('utf-8')
    return stdout

def ifttt(hostname, IP):
    report = {}
    report['value1'] = hostname
    report['value2'] = IP
    report['value3'] = ''
    rq.post("https://maker.ifttt.com/trigger/HEARTBEAT/json/with/key/ejMbNIprnOVzURmpIf_Sb", data=report)


#print('Hostname:{}\nIP Address:{}'.format(hostname, IP))
ifttt(hostname, IP)

