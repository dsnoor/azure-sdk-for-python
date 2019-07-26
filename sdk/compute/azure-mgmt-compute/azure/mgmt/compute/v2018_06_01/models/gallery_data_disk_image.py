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

from .gallery_disk_image import GalleryDiskImage


class GalleryDataDiskImage(GalleryDiskImage):
    """This is the data disk image.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar size_in_gb: This property indicates the size of the VHD to be
     created.
    :vartype size_in_gb: int
    :ivar host_caching: The host caching of the disk. Valid values are 'None',
     'ReadOnly', and 'ReadWrite'. Possible values include: 'None', 'ReadOnly',
     'ReadWrite'
    :vartype host_caching: str or
     ~azure.mgmt.compute.v2018_06_01.models.HostCaching
    :ivar lun: This property specifies the logical unit number of the data
     disk. This value is used to identify data disks within the Virtual Machine
     and therefore must be unique for each data disk attached to the Virtual
     Machine.
    :vartype lun: int
    """

    _validation = {
        'size_in_gb': {'readonly': True},
        'host_caching': {'readonly': True},
        'lun': {'readonly': True},
    }

    _attribute_map = {
        'size_in_gb': {'key': 'sizeInGB', 'type': 'int'},
        'host_caching': {'key': 'hostCaching', 'type': 'HostCaching'},
        'lun': {'key': 'lun', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(GalleryDataDiskImage, self).__init__(**kwargs)
        self.lun = None