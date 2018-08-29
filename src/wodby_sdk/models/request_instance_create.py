# coding: utf-8

"""
    Wodby API Reference

    # Introduction  The Wodby API is organized around REST. Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors. We use built-in HTTP features, like HTTP authentication and HTTP verbs, which are understood by off-the-shelf HTTP clients.  JSON is returned by all API responses, including errors.  # Authentication  Authenticate your account by including your secret key in API requests. You can manage your API keys in the Dashboard. Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, and so forth.  All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests without authentication will also fail.  Example of authenticated request: ``` curl https://api.wodby.com/api/v3/user -H 'X-API-KEY: <MY API TOKEN>' ```   # noqa: E501

    OpenAPI spec version: 3.x
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wodby_sdk.models.instance_type import InstanceType  # noqa: F401,E501
from wodby_sdk.models.request_instance_create_git import RequestInstanceCreateGit  # noqa: F401,E501
from wodby_sdk.models.uuid import Uuid  # noqa: F401,E501


class RequestInstanceCreate(object):
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
        'app_id': 'Uuid',
        'git': 'RequestInstanceCreateGit',
        'name': 'str',
        'post_deployment': 'bool',
        'server_id': 'Uuid',
        'title': 'str',
        'type': 'InstanceType'
    }

    attribute_map = {
        'app_id': 'app_id',
        'git': 'git',
        'name': 'name',
        'post_deployment': 'post_deployment',
        'server_id': 'server_id',
        'title': 'title',
        'type': 'type'
    }

    def __init__(self, app_id=None, git=None, name=None, post_deployment=None, server_id=None, title=None, type=None):  # noqa: E501
        """RequestInstanceCreate - a model defined in Swagger"""  # noqa: E501

        self._app_id = None
        self._git = None
        self._name = None
        self._post_deployment = None
        self._server_id = None
        self._title = None
        self._type = None
        self.discriminator = None

        self.app_id = app_id
        if git is not None:
            self.git = git
        self.name = name
        if post_deployment is not None:
            self.post_deployment = post_deployment
        self.server_id = server_id
        if title is not None:
            self.title = title
        self.type = type

    @property
    def app_id(self):
        """Gets the app_id of this RequestInstanceCreate.  # noqa: E501


        :return: The app_id of this RequestInstanceCreate.  # noqa: E501
        :rtype: Uuid
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this RequestInstanceCreate.


        :param app_id: The app_id of this RequestInstanceCreate.  # noqa: E501
        :type: Uuid
        """
        if app_id is None:
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def git(self):
        """Gets the git of this RequestInstanceCreate.  # noqa: E501


        :return: The git of this RequestInstanceCreate.  # noqa: E501
        :rtype: RequestInstanceCreateGit
        """
        return self._git

    @git.setter
    def git(self, git):
        """Sets the git of this RequestInstanceCreate.


        :param git: The git of this RequestInstanceCreate.  # noqa: E501
        :type: RequestInstanceCreateGit
        """

        self._git = git

    @property
    def name(self):
        """Gets the name of this RequestInstanceCreate.  # noqa: E501


        :return: The name of this RequestInstanceCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RequestInstanceCreate.


        :param name: The name of this RequestInstanceCreate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and not re.search('^[a-z0-9][a-z0-9-]{0,18}[a-z0-9]$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[a-z0-9][a-z0-9-]{0,18}[a-z0-9]$/`")  # noqa: E501

        self._name = name

    @property
    def post_deployment(self):
        """Gets the post_deployment of this RequestInstanceCreate.  # noqa: E501


        :return: The post_deployment of this RequestInstanceCreate.  # noqa: E501
        :rtype: bool
        """
        return self._post_deployment

    @post_deployment.setter
    def post_deployment(self, post_deployment):
        """Sets the post_deployment of this RequestInstanceCreate.


        :param post_deployment: The post_deployment of this RequestInstanceCreate.  # noqa: E501
        :type: bool
        """

        self._post_deployment = post_deployment

    @property
    def server_id(self):
        """Gets the server_id of this RequestInstanceCreate.  # noqa: E501


        :return: The server_id of this RequestInstanceCreate.  # noqa: E501
        :rtype: Uuid
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this RequestInstanceCreate.


        :param server_id: The server_id of this RequestInstanceCreate.  # noqa: E501
        :type: Uuid
        """
        if server_id is None:
            raise ValueError("Invalid value for `server_id`, must not be `None`")  # noqa: E501

        self._server_id = server_id

    @property
    def title(self):
        """Gets the title of this RequestInstanceCreate.  # noqa: E501


        :return: The title of this RequestInstanceCreate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this RequestInstanceCreate.


        :param title: The title of this RequestInstanceCreate.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this RequestInstanceCreate.  # noqa: E501


        :return: The type of this RequestInstanceCreate.  # noqa: E501
        :rtype: InstanceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RequestInstanceCreate.


        :param type: The type of this RequestInstanceCreate.  # noqa: E501
        :type: InstanceType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, RequestInstanceCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
