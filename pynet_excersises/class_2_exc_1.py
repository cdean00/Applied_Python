#!/usr/bin/env python

"""Using SNMPv3 create a script that detects changes to the running configuration.  If the running configuration is changed, then send an email notification to yourself identifying the router that changed and the time that it changed.
"""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from snmp_helper import snmp_get_oid_v3,snmp_extract
import os.path

#Global variables
running_systime = str
running_systime_previous = file

#pynet-rtr1 device information
snmp_device_pynet_rtr1 = ('50.242.94.227', 7961)
snmp_user_pynet_rtr1 = ('pysnmp', 'galileo1', 'galileo1')

#OIDs
OID_RUNNING_LAST_CHANGED = '1.3.6.1.4.1.9.9.43.1.1.1.0'
OID_SYSTIME = '1.3.6.1.2.1.1.3.0'

#Check if systime_previous file exists and creates systime file if doesn't exist to store systime each time script is ran
if os.path.isfile("running_systime_previous.txt"):
    try:
        print "Opening file."
        running_systime_previous = open("running_systime_previous.txt", "r+")
    except:
        print "Error opening or creating running_systime_previous file."
else:
    try:
        print "Filed does not exists. Creating file."
        running_systime_previous = open("running_systime_previous.txt", "w+")
    except:
        print "Error opening or creating running_systime_previous file."

running_systime = snmp_get_oid_v3(snmp_device_pynet_rtr1, snmp_user_pynet_rtr1, OID_RUNNING_LAST_CHANGED)
print type(str(running_systime[0][1]))
running_systime_previous_line = running_systime_previous.readline()

if running_systime[0][1] > running_systime_previous_line:
    print "Running config has changed!"

    running_systime_previous.write(str(running_systime[0][1]))
    running_systime_previous.close()

elif running_systime[0][1] == running_systime_previous_line:
    print "The running config has not changed"
    running_systime_previous.write("test")
    running_systime_previous.close()
elif running_systime[0][1] < running_systime_previous_line:
    print "Switch has been restarted. Resetting previous runnning config change systime."
    running_systime_previous.write(str(running_systime[0][1]))