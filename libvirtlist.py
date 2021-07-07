from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
    name: libvirtlist
    version_added: "0.1"
    short_description: parses a list from libvirt of VMs created
    description: Pattern matches a list of VMS from libvirt
    '''

import os

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils._text import to_bytes, to_native, to_text
from ansible.parsing.utils.addresses import parse_address
from ansible.plugins.inventory import BaseInventoryPlugin

class InventoryModule(BaseInventoryPlugin):

    NAME = 'libvirtlist'

    def verify_file(self, host_list):


    def parse(self, inventory, loader, host_list, cache=True):

