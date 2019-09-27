# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualMachineScaleSetVMProfile(Model):
    """Describes a virtual machine scale set virtual machine profile.

    :param os_profile: The virtual machine scale set OS profile.
    :type os_profile:
     ~azure.mgmt.compute.v2016_03_30.models.VirtualMachineScaleSetOSProfile
    :param storage_profile: The virtual machine scale set storage profile.
    :type storage_profile:
     ~azure.mgmt.compute.v2016_03_30.models.VirtualMachineScaleSetStorageProfile
    :param network_profile: The virtual machine scale set network profile.
    :type network_profile:
     ~azure.mgmt.compute.v2016_03_30.models.VirtualMachineScaleSetNetworkProfile
    :param extension_profile: The virtual machine scale set extension profile.
    :type extension_profile:
     ~azure.mgmt.compute.v2016_03_30.models.VirtualMachineScaleSetExtensionProfile
    """

    _attribute_map = {
        'os_profile': {'key': 'osProfile', 'type': 'VirtualMachineScaleSetOSProfile'},
        'storage_profile': {'key': 'storageProfile', 'type': 'VirtualMachineScaleSetStorageProfile'},
        'network_profile': {'key': 'networkProfile', 'type': 'VirtualMachineScaleSetNetworkProfile'},
        'extension_profile': {'key': 'extensionProfile', 'type': 'VirtualMachineScaleSetExtensionProfile'},
    }

    def __init__(self, **kwargs):
        super(VirtualMachineScaleSetVMProfile, self).__init__(**kwargs)
        self.os_profile = kwargs.get('os_profile', None)
        self.storage_profile = kwargs.get('storage_profile', None)
        self.network_profile = kwargs.get('network_profile', None)
        self.extension_profile = kwargs.get('extension_profile', None)