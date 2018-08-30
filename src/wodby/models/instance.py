# coding: utf-8

"""
    Wodby API Client

    Wodby Developer Documentation https://wodby.com/docs/dev  # noqa: E501

    OpenAPI spec version: 3.0.1
    Contact: hello@wodby.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wodby.models.instance_type import InstanceType  # noqa: F401,E501


class Instance(object):
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
        'app_id': 'str',
        'created': 'int',
        'git_repo_id': 'str',
        'id': 'str',
        'name': 'str',
        'new_version': 'str',
        'org_id': 'str',
        'status': 'str',
        'title': 'str',
        'type': 'InstanceType',
        'updated': 'int'
    }

    attribute_map = {
        'app_id': 'app_id',
        'created': 'created',
        'git_repo_id': 'git_repo_id',
        'id': 'id',
        'name': 'name',
        'new_version': 'new_version',
        'org_id': 'org_id',
        'status': 'status',
        'title': 'title',
        'type': 'type',
        'updated': 'updated'
    }

    def __init__(self, app_id=None, created=None, git_repo_id=None, id=None, name=None, new_version=None, org_id=None, status=None, title=None, type=None, updated=None):  # noqa: E501
        """Instance - a model defined in Swagger"""  # noqa: E501

        self._app_id = None
        self._created = None
        self._git_repo_id = None
        self._id = None
        self._name = None
        self._new_version = None
        self._org_id = None
        self._status = None
        self._title = None
        self._type = None
        self._updated = None
        self.discriminator = None

        self.app_id = app_id
        self.created = created
        if git_repo_id is not None:
            self.git_repo_id = git_repo_id
        self.id = id
        self.name = name
        if new_version is not None:
            self.new_version = new_version
        self.org_id = org_id
        self.status = status
        self.title = title
        if type is not None:
            self.type = type
        self.updated = updated

    @property
    def app_id(self):
        """Gets the app_id of this Instance.  # noqa: E501


        :return: The app_id of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this Instance.


        :param app_id: The app_id of this Instance.  # noqa: E501
        :type: str
        """
        if app_id is None:
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def created(self):
        """Gets the created of this Instance.  # noqa: E501


        :return: The created of this Instance.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Instance.


        :param created: The created of this Instance.  # noqa: E501
        :type: int
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def git_repo_id(self):
        """Gets the git_repo_id of this Instance.  # noqa: E501


        :return: The git_repo_id of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._git_repo_id

    @git_repo_id.setter
    def git_repo_id(self, git_repo_id):
        """Sets the git_repo_id of this Instance.


        :param git_repo_id: The git_repo_id of this Instance.  # noqa: E501
        :type: str
        """

        self._git_repo_id = git_repo_id

    @property
    def id(self):
        """Gets the id of this Instance.  # noqa: E501


        :return: The id of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Instance.


        :param id: The id of this Instance.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Instance.  # noqa: E501


        :return: The name of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Instance.


        :param name: The name of this Instance.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_version(self):
        """Gets the new_version of this Instance.  # noqa: E501


        :return: The new_version of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._new_version

    @new_version.setter
    def new_version(self, new_version):
        """Sets the new_version of this Instance.


        :param new_version: The new_version of this Instance.  # noqa: E501
        :type: str
        """

        self._new_version = new_version

    @property
    def org_id(self):
        """Gets the org_id of this Instance.  # noqa: E501


        :return: The org_id of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this Instance.


        :param org_id: The org_id of this Instance.  # noqa: E501
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def status(self):
        """Gets the status of this Instance.  # noqa: E501


        :return: The status of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Instance.


        :param status: The status of this Instance.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["ok", "unreachable", "error", "creating", "updating", "deleting"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def title(self):
        """Gets the title of this Instance.  # noqa: E501


        :return: The title of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Instance.


        :param title: The title of this Instance.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def type(self):
        """Gets the type of this Instance.  # noqa: E501


        :return: The type of this Instance.  # noqa: E501
        :rtype: InstanceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Instance.


        :param type: The type of this Instance.  # noqa: E501
        :type: InstanceType
        """

        self._type = type

    @property
    def updated(self):
        """Gets the updated of this Instance.  # noqa: E501


        :return: The updated of this Instance.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Instance.


        :param updated: The updated of this Instance.  # noqa: E501
        :type: int
        """
        if updated is None:
            raise ValueError("Invalid value for `updated`, must not be `None`")  # noqa: E501

        self._updated = updated

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
        if not isinstance(other, Instance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other