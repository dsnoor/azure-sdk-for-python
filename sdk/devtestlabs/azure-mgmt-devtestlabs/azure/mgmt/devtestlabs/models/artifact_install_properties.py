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


class ArtifactInstallProperties(Model):
    """Properties of an artifact.

    :param artifact_id: The artifact's identifier.
    :type artifact_id: str
    :param artifact_title: The artifact's title.
    :type artifact_title: str
    :param parameters: The parameters of the artifact.
    :type parameters:
     list[~azure.mgmt.devtestlabs.models.ArtifactParameterProperties]
    :param status: The status of the artifact.
    :type status: str
    :param deployment_status_message: The status message from the deployment.
    :type deployment_status_message: str
    :param vm_extension_status_message: The status message from the virtual
     machine extension.
    :type vm_extension_status_message: str
    :param install_time: The time that the artifact starts to install on the
     virtual machine.
    :type install_time: datetime
    """

    _attribute_map = {
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'artifact_title': {'key': 'artifactTitle', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '[ArtifactParameterProperties]'},
        'status': {'key': 'status', 'type': 'str'},
        'deployment_status_message': {'key': 'deploymentStatusMessage', 'type': 'str'},
        'vm_extension_status_message': {'key': 'vmExtensionStatusMessage', 'type': 'str'},
        'install_time': {'key': 'installTime', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(ArtifactInstallProperties, self).__init__(**kwargs)
        self.artifact_id = kwargs.get('artifact_id', None)
        self.artifact_title = kwargs.get('artifact_title', None)
        self.parameters = kwargs.get('parameters', None)
        self.status = kwargs.get('status', None)
        self.deployment_status_message = kwargs.get('deployment_status_message', None)
        self.vm_extension_status_message = kwargs.get('vm_extension_status_message', None)
        self.install_time = kwargs.get('install_time', None)