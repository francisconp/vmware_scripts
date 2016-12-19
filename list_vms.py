#!/usr/bin/python

from pysphere import VIServer
import ssl


vCenter = {
			'VCENTER01': {'host': '<IP_OR_HOSTNAME>', 'user': '<USER>','pass':'<PASS>' },
			'VCENTER02': {'host': '<IP_OR_HOSTNAME>', 'user': '<USER>','pass':'<PASS>' },
			}

try:
	default_context = ssl._create_default_https_context
	ssl._create_default_https_context = ssl._create_unverified_context
except:
	print "[v] Python version ok."

def get_vms():
	"""
	Output example:
	VM_NAME   SO
	MYVM01    Microsoft Windows Server 2003 Standard (32-bit)
	"""
	server = VIServer()
	vmlist = {}
	for Env in vCenter.keys():
		try:
			server.connect(vCenter[Env]['host'],vCenter[Env]['user'],vCenter[Env]['pass'])
		except:
			print "[x] Error connecting to vCernter server. "
			return 1

		vm_list = server.get_registered_vms()
		for disk_path in vm_list:
			vm = server.get_vm_by_path(disk_path)
			print('%s %s' % (vm.get_property('name'),vm.get_property('guest_full_name')))

get_vms()

