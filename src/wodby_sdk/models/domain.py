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


class Domain(object):
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
        'enabled': 'bool',
        'hsts': 'bool',
        'hsts_subdomains': 'bool',
        'id': 'str',
        'indexed': 'bool',
        'instance_id': 'str',
        'name': 'str',
        'org_id': 'str',
        'primary': 'bool',
        'protected': 'bool',
        'redirect_to_non_www': 'bool',
        'redirect_to_www': 'bool',
        'ssl': 'bool',
        'ssl_custom': 'bool',
        'ssl_required': 'bool',
        'status': 'str',
        'type': 'str',
        'updated': 'int'
    }

    attribute_map = {
        'created': 'created',
        'enabled': 'enabled',
        'hsts': 'hsts',
        'hsts_subdomains': 'hsts_subdomains',
        'id': 'id',
        'indexed': 'indexed',
        'instance_id': 'instance_id',
        'name': 'name',
        'org_id': 'org_id',
        'primary': 'primary',
        'protected': 'protected',
        'redirect_to_non_www': 'redirect_to_non_www',
        'redirect_to_www': 'redirect_to_www',
        'ssl': 'ssl',
        'ssl_custom': 'ssl_custom',
        'ssl_required': 'ssl_required',
        'status': 'status',
        'type': 'type',
        'updated': 'updated'
    }

    def __init__(self, created=None, enabled=None, hsts=None, hsts_subdomains=None, id=None, indexed=None, instance_id=None, name=None, org_id=None, primary=None, protected=None, redirect_to_non_www=None, redirect_to_www=None, ssl=None, ssl_custom=None, ssl_required=None, status=None, type=None, updated=None):  # noqa: E501
        """Domain - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._enabled = None
        self._hsts = None
        self._hsts_subdomains = None
        self._id = None
        self._indexed = None
        self._instance_id = None
        self._name = None
        self._org_id = None
        self._primary = None
        self._protected = None
        self._redirect_to_non_www = None
        self._redirect_to_www = None
        self._ssl = None
        self._ssl_custom = None
        self._ssl_required = None
        self._status = None
        self._type = None
        self._updated = None
        self.discriminator = None

        self.created = created
        if enabled is not None:
            self.enabled = enabled
        if hsts is not None:
            self.hsts = hsts
        if hsts_subdomains is not None:
            self.hsts_subdomains = hsts_subdomains
        self.id = id
        if indexed is not None:
            self.indexed = indexed
        self.instance_id = instance_id
        self.name = name
        self.org_id = org_id
        if primary is not None:
            self.primary = primary
        if protected is not None:
            self.protected = protected
        if redirect_to_non_www is not None:
            self.redirect_to_non_www = redirect_to_non_www
        if redirect_to_www is not None:
            self.redirect_to_www = redirect_to_www
        if ssl is not None:
            self.ssl = ssl
        if ssl_custom is not None:
            self.ssl_custom = ssl_custom
        if ssl_required is not None:
            self.ssl_required = ssl_required
        self.status = status
        self.type = type
        self.updated = updated

    @property
    def created(self):
        """Gets the created of this Domain.  # noqa: E501


        :return: The created of this Domain.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Domain.


        :param created: The created of this Domain.  # noqa: E501
        :type: int
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def enabled(self):
        """Gets the enabled of this Domain.  # noqa: E501


        :return: The enabled of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Domain.


        :param enabled: The enabled of this Domain.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def hsts(self):
        """Gets the hsts of this Domain.  # noqa: E501


        :return: The hsts of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._hsts

    @hsts.setter
    def hsts(self, hsts):
        """Sets the hsts of this Domain.


        :param hsts: The hsts of this Domain.  # noqa: E501
        :type: bool
        """

        self._hsts = hsts

    @property
    def hsts_subdomains(self):
        """Gets the hsts_subdomains of this Domain.  # noqa: E501


        :return: The hsts_subdomains of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._hsts_subdomains

    @hsts_subdomains.setter
    def hsts_subdomains(self, hsts_subdomains):
        """Sets the hsts_subdomains of this Domain.


        :param hsts_subdomains: The hsts_subdomains of this Domain.  # noqa: E501
        :type: bool
        """

        self._hsts_subdomains = hsts_subdomains

    @property
    def id(self):
        """Gets the id of this Domain.  # noqa: E501


        :return: The id of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Domain.


        :param id: The id of this Domain.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def indexed(self):
        """Gets the indexed of this Domain.  # noqa: E501


        :return: The indexed of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._indexed

    @indexed.setter
    def indexed(self, indexed):
        """Sets the indexed of this Domain.


        :param indexed: The indexed of this Domain.  # noqa: E501
        :type: bool
        """

        self._indexed = indexed

    @property
    def instance_id(self):
        """Gets the instance_id of this Domain.  # noqa: E501


        :return: The instance_id of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this Domain.


        :param instance_id: The instance_id of this Domain.  # noqa: E501
        :type: str
        """
        if instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def name(self):
        """Gets the name of this Domain.  # noqa: E501


        :return: The name of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Domain.


        :param name: The name of this Domain.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def org_id(self):
        """Gets the org_id of this Domain.  # noqa: E501


        :return: The org_id of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this Domain.


        :param org_id: The org_id of this Domain.  # noqa: E501
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def primary(self):
        """Gets the primary of this Domain.  # noqa: E501


        :return: The primary of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this Domain.


        :param primary: The primary of this Domain.  # noqa: E501
        :type: bool
        """

        self._primary = primary

    @property
    def protected(self):
        """Gets the protected of this Domain.  # noqa: E501


        :return: The protected of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        """Sets the protected of this Domain.


        :param protected: The protected of this Domain.  # noqa: E501
        :type: bool
        """

        self._protected = protected

    @property
    def redirect_to_non_www(self):
        """Gets the redirect_to_non_www of this Domain.  # noqa: E501


        :return: The redirect_to_non_www of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._redirect_to_non_www

    @redirect_to_non_www.setter
    def redirect_to_non_www(self, redirect_to_non_www):
        """Sets the redirect_to_non_www of this Domain.


        :param redirect_to_non_www: The redirect_to_non_www of this Domain.  # noqa: E501
        :type: bool
        """

        self._redirect_to_non_www = redirect_to_non_www

    @property
    def redirect_to_www(self):
        """Gets the redirect_to_www of this Domain.  # noqa: E501


        :return: The redirect_to_www of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._redirect_to_www

    @redirect_to_www.setter
    def redirect_to_www(self, redirect_to_www):
        """Sets the redirect_to_www of this Domain.


        :param redirect_to_www: The redirect_to_www of this Domain.  # noqa: E501
        :type: bool
        """

        self._redirect_to_www = redirect_to_www

    @property
    def ssl(self):
        """Gets the ssl of this Domain.  # noqa: E501


        :return: The ssl of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        """Sets the ssl of this Domain.


        :param ssl: The ssl of this Domain.  # noqa: E501
        :type: bool
        """

        self._ssl = ssl

    @property
    def ssl_custom(self):
        """Gets the ssl_custom of this Domain.  # noqa: E501


        :return: The ssl_custom of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._ssl_custom

    @ssl_custom.setter
    def ssl_custom(self, ssl_custom):
        """Sets the ssl_custom of this Domain.


        :param ssl_custom: The ssl_custom of this Domain.  # noqa: E501
        :type: bool
        """

        self._ssl_custom = ssl_custom

    @property
    def ssl_required(self):
        """Gets the ssl_required of this Domain.  # noqa: E501


        :return: The ssl_required of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._ssl_required

    @ssl_required.setter
    def ssl_required(self, ssl_required):
        """Sets the ssl_required of this Domain.


        :param ssl_required: The ssl_required of this Domain.  # noqa: E501
        :type: bool
        """

        self._ssl_required = ssl_required

    @property
    def status(self):
        """Gets the status of this Domain.  # noqa: E501


        :return: The status of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Domain.


        :param status: The status of this Domain.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["ok", "error", "creating", "deleting", "updating", "disabled"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def type(self):
        """Gets the type of this Domain.  # noqa: E501


        :return: The type of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Domain.


        :param type: The type of this Domain.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["technical", "user"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def updated(self):
        """Gets the updated of this Domain.  # noqa: E501


        :return: The updated of this Domain.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Domain.


        :param updated: The updated of this Domain.  # noqa: E501
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
        if not isinstance(other, Domain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
