# coding: utf-8

"""
    Wodby API Client

    Wodby Developer Documentation https://wodby.com/docs/dev  # noqa: E501

    OpenAPI spec version: 3.0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RequestStacksUpdate(object):
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
        'stacks': 'list[str]'
    }

    attribute_map = {
        'stacks': 'stacks'
    }

    def __init__(self, stacks=None):  # noqa: E501
        """RequestStacksUpdate - a model defined in Swagger"""  # noqa: E501

        self._stacks = None
        self.discriminator = None

        self.stacks = stacks

    @property
    def stacks(self):
        """Gets the stacks of this RequestStacksUpdate.  # noqa: E501


        :return: The stacks of this RequestStacksUpdate.  # noqa: E501
        :rtype: list[str]
        """
        return self._stacks

    @stacks.setter
    def stacks(self, stacks):
        """Sets the stacks of this RequestStacksUpdate.


        :param stacks: The stacks of this RequestStacksUpdate.  # noqa: E501
        :type: list[str]
        """
        if stacks is None:
            raise ValueError("Invalid value for `stacks`, must not be `None`")  # noqa: E501

        self._stacks = stacks

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
        if not isinstance(other, RequestStacksUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
