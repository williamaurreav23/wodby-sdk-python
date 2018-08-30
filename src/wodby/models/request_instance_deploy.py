# coding: utf-8

"""
    Wodby API Client

    Wodby Developer Documentation https://wodby.com/docs/dev  # noqa: E501

    OpenAPI spec version: 3.0.2
    Contact: hello@wodby.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RequestInstanceDeploy(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'post_deployment': 'bool'
    }

    attribute_map = {
        'post_deployment': 'post_deployment'
    }

    def __init__(self, post_deployment=None):  # noqa: E501
        """RequestInstanceDeploy - a model defined in Swagger"""  # noqa: E501

        self._post_deployment = None
        self.discriminator = None

        if post_deployment is not None:
            self.post_deployment = post_deployment

    @property
    def post_deployment(self):
        """Gets the post_deployment of this RequestInstanceDeploy.  # noqa: E501


        :return: The post_deployment of this RequestInstanceDeploy.  # noqa: E501
        :rtype: bool
        """
        return self._post_deployment

    @post_deployment.setter
    def post_deployment(self, post_deployment):
        """Sets the post_deployment of this RequestInstanceDeploy.


        :param post_deployment: The post_deployment of this RequestInstanceDeploy.  # noqa: E501
        :type: bool
        """

        self._post_deployment = post_deployment

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RequestInstanceDeploy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
