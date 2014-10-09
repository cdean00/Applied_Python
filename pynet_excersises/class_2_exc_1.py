#!/usr/bin/env python

"""Using SNMPv3 create a script that detects changes to the running configuration.  If the running configuration is changed, then send an email notification to yourself identifying the router that changed and the time that it changed.
"""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from snmp_helper import snmp_get_oid_v3,snmp_extract

#Global variables
systime = ''

#pynet-rtr1 device information
snmp_device_pynet_rtr1 = ('50.242.94.227', 7961)
snmp_user_pynet_rtr1 = ('pysnmp', 'galileo1', 'galileo1')

#OIDs
OID_RUNNING_LAST_CHANGED = '1.3.6.1.4.1.9.9.43.1.1.1.0'
OID_SYSTIME = '1.3.6.1.2.1.1.3.0'

#Check if systime_previous file exists and creates systime file if doesn't exist to store systime each time script is ran
try:
    systime_previous = open('systime_previous.txt', 'r+')
except:
    print "systime_previous.txt file does not exist. Creating file."
    systime_previous = open('systime_previous.txt', 'w+')

systime = snmp_get_oid_v3(snmp_device_pynet_rtr1, snmp_user_pynet_rtr1, OID_RUNNING_LAST_CHANGED)
print systime 
print systime[0][1]
if str(systime[1][0]) > systime_previous.readline():
    print "Running config has changed!"
    systime_previous.write(str(systime[1][0]))
    systime_previous.close()
    
elif str(systime[1][0]) <= systime_previous.readline():
    print "The running config has not changed"
    systime_previous.write(str(systime[1][0]))
    systime_previous.close()
