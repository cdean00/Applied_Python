'''
1. Using SNMPv3 create a script that detects changes to the running configuration.  If the running configuration is changed, then send an email notification to yourself identifying the router that changed and the time that it changed.
'''
from snmp_helper import snmp_get_oid_v3,snmp_extract

#pynet-rtr1 device information
snmp_device_pynet_rtr1 = ('50.242.94.227', 7961)
snmp_user_pynet_rtr1 = ('pysnmp', 'galileo1', 'galileo1')

#OIDs
OID_RUNNING_LAST_CHANGED = '1.3.6.1.4.1.9.9.43.1.1.1.0'
OID_SYSTIME = '1.3.6.1.2.1.1.3.0'

systime = snmp_get_oid_v3(snmp_device_pynet_rtr1, snmp_user_pynet_rtr1, OID_RUNNING_LAST_CHANGED) 

print systime
