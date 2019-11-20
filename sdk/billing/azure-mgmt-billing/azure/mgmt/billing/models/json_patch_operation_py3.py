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


class JsonPatchOperation(Model):
    """The Json Patch definition.

    :param value: The value.
    :type value: object
    :param path: The target location.
    :type path: str
    :param op: The operation.
    :type op: str
    :param from_property: The source location.
    :type from_property: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'object'},
        'path': {'key': 'path', 'type': 'str'},
        'op': {'key': 'op', 'type': 'str'},
        'from_property': {'key': 'from', 'type': 'str'},
    }

    def __init__(self, *, value=None, path: str=None, op: str=None, from_property: str=None, **kwargs) -> None:
        super(JsonPatchOperation, self).__init__(**kwargs)
        self.value = value
        self.path = path
        self.op = op
        self.from_property = from_property
