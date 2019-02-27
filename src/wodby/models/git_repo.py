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


class GitRepo(object):
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
        'created': 'int',
        'id': 'str',
        'org_id': 'str',
        'status': 'str',
        'title': 'str',
        'updated': 'int',
        'url': 'str'
    }

    attribute_map = {
        'created': 'created',
        'id': 'id',
        'org_id': 'org_id',
        'status': 'status',
        'title': 'title',
        'updated': 'updated',
        'url': 'url'
    }

    def __init__(self, created=None, id=None, org_id=None, status=None, title=None, updated=None, url=None):  # noqa: E501
        """GitRepo - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._id = None
        self._org_id = None
        self._status = None
        self._title = None
        self._updated = None
        self._url = None
        self.discriminator = None

        self.created = created
        self.id = id
        self.org_id = org_id
        self.status = status
        self.title = title
        self.updated = updated
        if url is not None:
            self.url = url

    @property
    def created(self):
        """Gets the created of this GitRepo.  # noqa: E501


        :return: The created of this GitRepo.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GitRepo.


        :param created: The created of this GitRepo.  # noqa: E501
        :type: int
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def id(self):
        """Gets the id of this GitRepo.  # noqa: E501


        :return: The id of this GitRepo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GitRepo.


        :param id: The id of this GitRepo.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and not re.search('^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', id):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a follow pattern or equal to `/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/`")  # noqa: E501

        self._id = id

    @property
    def org_id(self):
        """Gets the org_id of this GitRepo.  # noqa: E501


        :return: The org_id of this GitRepo.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this GitRepo.


        :param org_id: The org_id of this GitRepo.  # noqa: E501
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def status(self):
        """Gets the status of this GitRepo.  # noqa: E501


        :return: The status of this GitRepo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GitRepo.


        :param status: The status of this GitRepo.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["ok", "error", "creating", "deleting"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def title(self):
        """Gets the title of this GitRepo.  # noqa: E501


        :return: The title of this GitRepo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GitRepo.


        :param title: The title of this GitRepo.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def updated(self):
        """Gets the updated of this GitRepo.  # noqa: E501


        :return: The updated of this GitRepo.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this GitRepo.


        :param updated: The updated of this GitRepo.  # noqa: E501
        :type: int
        """
        if updated is None:
            raise ValueError("Invalid value for `updated`, must not be `None`")  # noqa: E501

        self._updated = updated

    @property
    def url(self):
        """Gets the url of this GitRepo.  # noqa: E501


        :return: The url of this GitRepo.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GitRepo.


        :param url: The url of this GitRepo.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, GitRepo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
