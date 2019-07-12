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


class IoTSecurityAggregatedAlert(Model):
    """Security Solution Aggregated Alert information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :ivar alert_type: Name of the alert type
    :vartype alert_type: str
    :ivar alert_display_name: Display name of the alert type
    :vartype alert_display_name: str
    :ivar aggregated_date_utc: The date the incidents were detected by the
     vendor
    :vartype aggregated_date_utc: date
    :ivar vendor_name: Name of the vendor that discovered the incident
    :vartype vendor_name: str
    :ivar reported_severity: Estimated severity of this alert. Possible values
     include: 'Informational', 'Low', 'Medium', 'High'
    :vartype reported_severity: str or
     ~azure.mgmt.security.models.ReportedSeverity
    :ivar remediation_steps: Recommended steps for remediation
    :vartype remediation_steps: str
    :ivar description: Description of the incident and what it means
    :vartype description: str
    :ivar count: Occurrence number of the alert within the aggregated date
    :vartype count: int
    :ivar effected_resource_type: Azure resource ID of the resource that got
     the alerts
    :vartype effected_resource_type: str
    :ivar system_source: The type of the alerted resource (Azure, Non-Azure)
    :vartype system_source: str
    :ivar action_taken: The action that was taken as a response to the alert
     (Active, Blocked etc.)
    :vartype action_taken: str
    :ivar log_analytics_query: query in log analytics to get the list of
     affected devices/alerts
    :vartype log_analytics_query: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'alert_type': {'readonly': True},
        'alert_display_name': {'readonly': True},
        'aggregated_date_utc': {'readonly': True},
        'vendor_name': {'readonly': True},
        'reported_severity': {'readonly': True},
        'remediation_steps': {'readonly': True},
        'description': {'readonly': True},
        'count': {'readonly': True},
        'effected_resource_type': {'readonly': True},
        'system_source': {'readonly': True},
        'action_taken': {'readonly': True},
        'log_analytics_query': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'alert_type': {'key': 'properties.alertType', 'type': 'str'},
        'alert_display_name': {'key': 'properties.alertDisplayName', 'type': 'str'},
        'aggregated_date_utc': {'key': 'properties.aggregatedDateUtc', 'type': 'date'},
        'vendor_name': {'key': 'properties.vendorName', 'type': 'str'},
        'reported_severity': {'key': 'properties.reportedSeverity', 'type': 'str'},
        'remediation_steps': {'key': 'properties.remediationSteps', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'count': {'key': 'properties.count', 'type': 'int'},
        'effected_resource_type': {'key': 'properties.effectedResourceType', 'type': 'str'},
        'system_source': {'key': 'properties.systemSource', 'type': 'str'},
        'action_taken': {'key': 'properties.actionTaken', 'type': 'str'},
        'log_analytics_query': {'key': 'properties.logAnalyticsQuery', 'type': 'str'},
    }

    def __init__(self, *, tags=None, **kwargs) -> None:
        super(IoTSecurityAggregatedAlert, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.tags = tags
        self.alert_type = None
        self.alert_display_name = None
        self.aggregated_date_utc = None
        self.vendor_name = None
        self.reported_severity = None
        self.remediation_steps = None
        self.description = None
        self.count = None
        self.effected_resource_type = None
        self.system_source = None
        self.action_taken = None
        self.log_analytics_query = None
