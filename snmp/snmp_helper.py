from pysnmp.entity.rfc3413.oneliner import cmdgen


def snmp_get_oid(a_device, oid='.1.3.6.1.2.1.1.1.0', display_errors=False):
    '''
    Retrieve the given OID

    Default OID is MIB2, sysDescr

    a_device is a tuple = (a_host, community_string, snmp_port)
    '''

    a_host, community_string, snmp_port = a_device
    snmp_target = (a_host, snmp_port)

    # Create a PYSNMP cmdgen object
    cmd_gen = cmdgen.CommandGenerator()

    (error_detected, error_status, error_index, snmp_data) = cmd_gen.getCmd(
        cmdgen.CommunityData(community_string),
        cmdgen.UdpTransportTarget(snmp_target),
        oid,
        lookupNames=True, lookupValues=True
    )

    if not error_detected:
        return snmp_data
    else:
        if display_errors:
            print 'ERROR DETECTED: '
            print '    %-16s %-60s' % ('error_message', error_detected)
            print '    %-16s %-60s' % ('error_status', error_status)
            print '    %-16s %-60s' % ('error_index', error_index)
        return None


def snmp_extract(snmp_data):
    '''
    Unwrap the SNMP response data and return in a readable format

    Assumes only a single list element is returned
    '''

    if len(snmp_data) > 1:
        raise ValueError("snmp_extract only allows a single element")

    if len(snmp_data) == 0:
        return None
    else:
        # Unwrap the data which is returned as a tuple wrapped in a list
        return snmp_data[0][1].prettyPrint()
