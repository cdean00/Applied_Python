from snmp_helper import snmp_get_oid,snmp_extract

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 8061 
IP = '50.242.94.227'
SYSNAME_OID = '1.3.6.1.2.1.1.5.0'
SYSDESCR_OID = '1.3.6.1.2.1.1.1.0'
a_device = (IP, COMMUNITY_STRING, SNMP_PORT)

snmp_sysdescr = snmp_get_oid(a_device, oid=SYSDESCR_OID)
snmp_sysname = snmp_get_oid(a_device, oid=SYSNAME_OID)

sysdescr_output = snmp_extract(snmp_sysdescr)
sysname_output = snmp_extract(snmp_sysname)
print sysdescr_output
print sysname_output
