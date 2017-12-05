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


class VerificationCodeResponseProperties(Model):
    """VerificationCodeResponseProperties.

    :param verification_code: Verification code.
    :type verification_code: str
    :param subject: Certificate subject.
    :type subject: str
    :param expiry: Code expiry.
    :type expiry: str
    :param thumbprint: Certificate thumbprint.
    :type thumbprint: str
    :param is_verified: Indicate if the certificate is verified by owner of
     private key.
    :type is_verified: bool
    :param created: Certificate created time.
    :type created: str
    :param updated: Certificate updated time.
    :type updated: str
    """

    _attribute_map = {
        'verification_code': {'key': 'verificationCode', 'type': 'str'},
        'subject': {'key': 'subject', 'type': 'str'},
        'expiry': {'key': 'expiry', 'type': 'str'},
        'thumbprint': {'key': 'thumbprint', 'type': 'str'},
        'is_verified': {'key': 'isVerified', 'type': 'bool'},
        'created': {'key': 'created', 'type': 'str'},
        'updated': {'key': 'updated', 'type': 'str'},
    }

    def __init__(self, verification_code=None, subject=None, expiry=None, thumbprint=None, is_verified=None, created=None, updated=None):
        super(VerificationCodeResponseProperties, self).__init__()
        self.verification_code = verification_code
        self.subject = subject
        self.expiry = expiry
        self.thumbprint = thumbprint
        self.is_verified = is_verified
        self.created = created
        self.updated = updated
