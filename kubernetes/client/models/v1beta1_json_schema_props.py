# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.13.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1JSONSchemaProps(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'ref': 'str',
        'schema': 'str',
        'additional_items': 'object',
        'additional_properties': 'object',
        'all_of': 'list[V1beta1JSONSchemaProps]',
        'any_of': 'list[V1beta1JSONSchemaProps]',
        'default': 'object',
        'definitions': 'dict(str, V1beta1JSONSchemaProps)',
        'dependencies': 'dict(str, object)',
        'description': 'str',
        'enum': 'list[object]',
        'example': 'object',
        'exclusive_maximum': 'bool',
        'exclusive_minimum': 'bool',
        'external_docs': 'V1beta1ExternalDocumentation',
        'format': 'str',
        'id': 'str',
        'items': 'object',
        'max_items': 'int',
        'max_length': 'int',
        'max_properties': 'int',
        'maximum': 'float',
        'min_items': 'int',
        'min_length': 'int',
        'min_properties': 'int',
        'minimum': 'float',
        'multiple_of': 'float',
        '_not': 'V1beta1JSONSchemaProps',
        'one_of': 'list[V1beta1JSONSchemaProps]',
        'pattern': 'str',
        'pattern_properties': 'dict(str, V1beta1JSONSchemaProps)',
        'properties': 'dict(str, V1beta1JSONSchemaProps)',
        'required': 'list[str]',
        'title': 'str',
        'type': 'str',
        'unique_items': 'bool'
    }

    attribute_map = {
        'ref': '$ref',
        'schema': '$schema',
        'additional_items': 'additionalItems',
        'additional_properties': 'additionalProperties',
        'all_of': 'allOf',
        'any_of': 'anyOf',
        'default': 'default',
        'definitions': 'definitions',
        'dependencies': 'dependencies',
        'description': 'description',
        'enum': 'enum',
        'example': 'example',
        'exclusive_maximum': 'exclusiveMaximum',
        'exclusive_minimum': 'exclusiveMinimum',
        'external_docs': 'externalDocs',
        'format': 'format',
        'id': 'id',
        'items': 'items',
        'max_items': 'maxItems',
        'max_length': 'maxLength',
        'max_properties': 'maxProperties',
        'maximum': 'maximum',
        'min_items': 'minItems',
        'min_length': 'minLength',
        'min_properties': 'minProperties',
        'minimum': 'minimum',
        'multiple_of': 'multipleOf',
        '_not': 'not',
        'one_of': 'oneOf',
        'pattern': 'pattern',
        'pattern_properties': 'patternProperties',
        'properties': 'properties',
        'required': 'required',
        'title': 'title',
        'type': 'type',
        'unique_items': 'uniqueItems'
    }

    def __init__(self, ref=None, schema=None, additional_items=None, additional_properties=None, all_of=None, any_of=None, default=None, definitions=None, dependencies=None, description=None, enum=None, example=None, exclusive_maximum=None, exclusive_minimum=None, external_docs=None, format=None, id=None, items=None, max_items=None, max_length=None, max_properties=None, maximum=None, min_items=None, min_length=None, min_properties=None, minimum=None, multiple_of=None, _not=None, one_of=None, pattern=None, pattern_properties=None, properties=None, required=None, title=None, type=None, unique_items=None):
        """
        V1beta1JSONSchemaProps - a model defined in Swagger
        """

        self._ref = None
        self._schema = None
        self._additional_items = None
        self._additional_properties = None
        self._all_of = None
        self._any_of = None
        self._default = None
        self._definitions = None
        self._dependencies = None
        self._description = None
        self._enum = None
        self._example = None
        self._exclusive_maximum = None
        self._exclusive_minimum = None
        self._external_docs = None
        self._format = None
        self._id = None
        self._items = None
        self._max_items = None
        self._max_length = None
        self._max_properties = None
        self._maximum = None
        self._min_items = None
        self._min_length = None
        self._min_properties = None
        self._minimum = None
        self._multiple_of = None
        self.__not = None
        self._one_of = None
        self._pattern = None
        self._pattern_properties = None
        self._properties = None
        self._required = None
        self._title = None
        self._type = None
        self._unique_items = None
        self.discriminator = None

        if ref is not None:
          self.ref = ref
        if schema is not None:
          self.schema = schema
        if additional_items is not None:
          self.additional_items = additional_items
        if additional_properties is not None:
          self.additional_properties = additional_properties
        if all_of is not None:
          self.all_of = all_of
        if any_of is not None:
          self.any_of = any_of
        if default is not None:
          self.default = default
        if definitions is not None:
          self.definitions = definitions
        if dependencies is not None:
          self.dependencies = dependencies
        if description is not None:
          self.description = description
        if enum is not None:
          self.enum = enum
        if example is not None:
          self.example = example
        if exclusive_maximum is not None:
          self.exclusive_maximum = exclusive_maximum
        if exclusive_minimum is not None:
          self.exclusive_minimum = exclusive_minimum
        if external_docs is not None:
          self.external_docs = external_docs
        if format is not None:
          self.format = format
        if id is not None:
          self.id = id
        if items is not None:
          self.items = items
        if max_items is not None:
          self.max_items = max_items
        if max_length is not None:
          self.max_length = max_length
        if max_properties is not None:
          self.max_properties = max_properties
        if maximum is not None:
          self.maximum = maximum
        if min_items is not None:
          self.min_items = min_items
        if min_length is not None:
          self.min_length = min_length
        if min_properties is not None:
          self.min_properties = min_properties
        if minimum is not None:
          self.minimum = minimum
        if multiple_of is not None:
          self.multiple_of = multiple_of
        if _not is not None:
          self._not = _not
        if one_of is not None:
          self.one_of = one_of
        if pattern is not None:
          self.pattern = pattern
        if pattern_properties is not None:
          self.pattern_properties = pattern_properties
        if properties is not None:
          self.properties = properties
        if required is not None:
          self.required = required
        if title is not None:
          self.title = title
        if type is not None:
          self.type = type
        if unique_items is not None:
          self.unique_items = unique_items

    @property
    def ref(self):
        """
        Gets the ref of this V1beta1JSONSchemaProps.

        :return: The ref of this V1beta1JSONSchemaProps.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this V1beta1JSONSchemaProps.

        :param ref: The ref of this V1beta1JSONSchemaProps.
        :type: str
        """

        self._ref = ref

    @property
    def schema(self):
        """
        Gets the schema of this V1beta1JSONSchemaProps.

        :return: The schema of this V1beta1JSONSchemaProps.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this V1beta1JSONSchemaProps.

        :param schema: The schema of this V1beta1JSONSchemaProps.
        :type: str
        """

        self._schema = schema

    @property
    def additional_items(self):
        """
        Gets the additional_items of this V1beta1JSONSchemaProps.
        JSONSchemaPropsOrBool represents JSONSchemaProps or a boolean value. Defaults to true for the boolean property.

        :return: The additional_items of this V1beta1JSONSchemaProps.
        :rtype: object
        """
        return self._additional_items

    @additional_items.setter
    def additional_items(self, additional_items):
        """
        Sets the additional_items of this V1beta1JSONSchemaProps.
        JSONSchemaPropsOrBool represents JSONSchemaProps or a boolean value. Defaults to true for the boolean property.

        :param additional_items: The additional_items of this V1beta1JSONSchemaProps.
        :type: object
        """

        self._additional_items = additional_items

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this V1beta1JSONSchemaProps.
        JSONSchemaPropsOrBool represents JSONSchemaProps or a boolean value. Defaults to true for the boolean property.

        :return: The additional_properties of this V1beta1JSONSchemaProps.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this V1beta1JSONSchemaProps.
        JSONSchemaPropsOrBool represents JSONSchemaProps or a boolean value. Defaults to true for the boolean property.

        :param additional_properties: The additional_properties of this V1beta1JSONSchemaProps.
        :type: object
        """

        self._additional_properties = additional_properties

    @property
    def all_of(self):
        """
        Gets the all_of of this V1beta1JSONSchemaProps.

        :return: The all_of of this V1beta1JSONSchemaProps.
        :rtype: list[V1beta1JSONSchemaProps]
        """
        return self._all_of

    @all_of.setter
    def all_of(self, all_of):
        """
        Sets the all_of of this V1beta1JSONSchemaProps.

        :param all_of: The all_of of this V1beta1JSONSchemaProps.
        :type: list[V1beta1JSONSchemaProps]
        """

        self._all_of = all_of

    @property
    def any_of(self):
        """
        Gets the any_of of this V1beta1JSONSchemaProps.

        :return: The any_of of this V1beta1JSONSchemaProps.
        :rtype: list[V1beta1JSONSchemaProps]
        """
        return self._any_of

    @any_of.setter
    def any_of(self, any_of):
        """
        Sets the any_of of this V1beta1JSONSchemaProps.

        :param any_of: The any_of of this V1beta1JSONSchemaProps.
        :type: list[V1beta1JSONSchemaProps]
        """

        self._any_of = any_of

    @property
    def default(self):
        """
        Gets the default of this V1beta1JSONSchemaProps.
        JSON represents any valid JSON value. These types are supported: bool, int64, float64, string, []interface{}, map[string]interface{} and nil.

        :return: The default of this V1beta1JSONSchemaProps.
        :rtype: object
        """
        return self._default

    @default.setter
    def default(self, default):
        """
        Sets the default of this V1beta1JSONSchemaProps.
        JSON represents any valid JSON value. These types are supported: bool, int64, float64, string, []interface{}, map[string]interface{} and nil.

        :param default: The default of this V1beta1JSONSchemaProps.
        :type: object
        """

        self._default = default

    @property
    def definitions(self):
        """
        Gets the definitions of this V1beta1JSONSchemaProps.

        :return: The definitions of this V1beta1JSONSchemaProps.
        :rtype: dict(str, V1beta1JSONSchemaProps)
        """
        return self._definitions

    @definitions.setter
    def definitions(self, definitions):
        """
        Sets the definitions of this V1beta1JSONSchemaProps.

        :param definitions: The definitions of this V1beta1JSONSchemaProps.
        :type: dict(str, V1beta1JSONSchemaProps)
        """

        self._definitions = definitions

    @property
    def dependencies(self):
        """
        Gets the dependencies of this V1beta1JSONSchemaProps.

        :return: The dependencies of this V1beta1JSONSchemaProps.
        :rtype: dict(str, object)
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """
        Sets the dependencies of this V1beta1JSONSchemaProps.

        :param dependencies: The dependencies of this V1beta1JSONSchemaProps.
        :type: dict(str, object)
        """

        self._dependencies = dependencies

    @property
    def description(self):
        """
        Gets the description of this V1beta1JSONSchemaProps.

        :return: The description of this V1beta1JSONSchemaProps.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this V1beta1JSONSchemaProps.

        :param description: The description of this V1beta1JSONSchemaProps.
        :type: str
        """

        self._description = description

    @property
    def enum(self):
        """
        Gets the enum of this V1beta1JSONSchemaProps.

        :return: The enum of this V1beta1JSONSchemaProps.
        :rtype: list[object]
        """
        return self._enum

    @enum.setter
    def enum(self, enum):
        """
        Sets the enum of this V1beta1JSONSchemaProps.

        :param enum: The enum of this V1beta1JSONSchemaProps.
        :type: list[object]
        """

        self._enum = enum

    @property
    def example(self):
        """
        Gets the example of this V1beta1JSONSchemaProps.
        JSON represents any valid JSON value. These types are supported: bool, int64, float64, string, []interface{}, map[string]interface{} and nil.

        :return: The example of this V1beta1JSONSchemaProps.
        :rtype: object
        """
        return self._example

    @example.setter
    def example(self, example):
        """
        Sets the example of this V1beta1JSONSchemaProps.
        JSON represents any valid JSON value. These types are supported: bool, int64, float64, string, []interface{}, map[string]interface{} and nil.

        :param example: The example of this V1beta1JSONSchemaProps.
        :type: object
        """

        self._example = example

    @property
    def exclusive_maximum(self):
        """
        Gets the exclusive_maximum of this V1beta1JSONSchemaProps.

        :return: The exclusive_maximum of this V1beta1JSONSchemaProps.
        :rtype: bool
        """
        return self._exclusive_maximum

    @exclusive_maximum.setter
    def exclusive_maximum(self, exclusive_maximum):
        """
        Sets the exclusive_maximum of this V1beta1JSONSchemaProps.

        :param exclusive_maximum: The exclusive_maximum of this V1beta1JSONSchemaProps.
        :type: bool
        """

        self._exclusive_maximum = exclusive_maximum

    @property
    def exclusive_minimum(self):
        """
        Gets the exclusive_minimum of this V1beta1JSONSchemaProps.

        :return: The exclusive_minimum of this V1beta1JSONSchemaProps.
        :rtype: bool
        """
        return self._exclusive_minimum

    @exclusive_minimum.setter
    def exclusive_minimum(self, exclusive_minimum):
        """
        Sets the exclusive_minimum of this V1beta1JSONSchemaProps.

        :param exclusive_minimum: The exclusive_minimum of this V1beta1JSONSchemaProps.
        :type: bool
        """

        self._exclusive_minimum = exclusive_minimum

    @property
    def external_docs(self):
        """
        Gets the external_docs of this V1beta1JSONSchemaProps.

        :return: The external_docs of this V1beta1JSONSchemaProps.
        :rtype: V1beta1ExternalDocumentation
        """
        return self._external_docs

    @external_docs.setter
    def external_docs(self, external_docs):
        """
        Sets the external_docs of this V1beta1JSONSchemaProps.

        :param external_docs: The external_docs of this V1beta1JSONSchemaProps.
        :type: V1beta1ExternalDocumentation
        """

        self._external_docs = external_docs

    @property
    def format(self):
        """
        Gets the format of this V1beta1JSONSchemaProps.

        :return: The format of this V1beta1JSONSchemaProps.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this V1beta1JSONSchemaProps.

        :param format: The format of this V1beta1JSONSchemaProps.
        :type: str
        """

        self._format = format

    @property
    def id(self):
        """
        Gets the id of this V1beta1JSONSchemaProps.

        :return: The id of this V1beta1JSONSchemaProps.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this V1beta1JSONSchemaProps.

        :param id: The id of this V1beta1JSONSchemaProps.
        :type: str
        """

        self._id = id

    @property
    def items(self):
        """
        Gets the items of this V1beta1JSONSchemaProps.
        JSONSchemaPropsOrArray represents a value that can either be a JSONSchemaProps or an array of JSONSchemaProps. Mainly here for serialization purposes.

        :return: The items of this V1beta1JSONSchemaProps.
        :rtype: object
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this V1beta1JSONSchemaProps.
        JSONSchemaPropsOrArray represents a value that can either be a JSONSchemaProps or an array of JSONSchemaProps. Mainly here for serialization purposes.

        :param items: The items of this V1beta1JSONSchemaProps.
        :type: object
        """

        self._items = items

    @property
    def max_items(self):
        """
        Gets the max_items of this V1beta1JSONSchemaProps.

        :return: The max_items of this V1beta1JSONSchemaProps.
        :rtype: int
        """
        return self._max_items

    @max_items.setter
    def max_items(self, max_items):
        """
        Sets the max_items of this V1beta1JSONSchemaProps.

        :param max_items: The max_items of this V1beta1JSONSchemaProps.
        :type: int
        """

        self._max_items = max_items

    @property
    def max_length(self):
        """
        Gets the max_length of this V1beta1JSONSchemaProps.

        :return: The max_length of this V1beta1JSONSchemaProps.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """
        Sets the max_length of this V1beta1JSONSchemaProps.

        :param max_length: The max_length of this V1beta1JSONSchemaProps.
        :type: int
        """

        self._max_length = max_length

    @property
    def max_properties(self):
        """
        Gets the max_properties of this V1beta1JSONSchemaProps.

        :return: The max_properties of this V1beta1JSONSchemaProps.
        :rtype: int
        """
        return self._max_properties

    @max_properties.setter
    def max_properties(self, max_properties):
        """
        Sets the max_properties of this V1beta1JSONSchemaProps.

        :param max_properties: The max_properties of this V1beta1JSONSchemaProps.
        :type: int
        """

        self._max_properties = max_properties

    @property
    def maximum(self):
        """
        Gets the maximum of this V1beta1JSONSchemaProps.

        :return: The maximum of this V1beta1JSONSchemaProps.
        :rtype: float
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """
        Sets the maximum of this V1beta1JSONSchemaProps.

        :param maximum: The maximum of this V1beta1JSONSchemaProps.
        :type: float
        """

        self._maximum = maximum

    @property
    def min_items(self):
        """
        Gets the min_items of this V1beta1JSONSchemaProps.

        :return: The min_items of this V1beta1JSONSchemaProps.
        :rtype: int
        """
        return self._min_items

    @min_items.setter
    def min_items(self, min_items):
        """
        Sets the min_items of this V1beta1JSONSchemaProps.

        :param min_items: The min_items of this V1beta1JSONSchemaProps.
        :type: int
        """

        self._min_items = min_items

    @property
    def min_length(self):
        """
        Gets the min_length of this V1beta1JSONSchemaProps.

        :return: The min_length of this V1beta1JSONSchemaProps.
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """
        Sets the min_length of this V1beta1JSONSchemaProps.

        :param min_length: The min_length of this V1beta1JSONSchemaProps.
        :type: int
        """

        self._min_length = min_length

    @property
    def min_properties(self):
        """
        Gets the min_properties of this V1beta1JSONSchemaProps.

        :return: The min_properties of this V1beta1JSONSchemaProps.
        :rtype: int
        """
        return self._min_properties

    @min_properties.setter
    def min_properties(self, min_properties):
        """
        Sets the min_properties of this V1beta1JSONSchemaProps.

        :param min_properties: The min_properties of this V1beta1JSONSchemaProps.
        :type: int
        """

        self._min_properties = min_properties

    @property
    def minimum(self):
        """
        Gets the minimum of this V1beta1JSONSchemaProps.

        :return: The minimum of this V1beta1JSONSchemaProps.
        :rtype: float
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """
        Sets the minimum of this V1beta1JSONSchemaProps.

        :param minimum: The minimum of this V1beta1JSONSchemaProps.
        :type: float
        """

        self._minimum = minimum

    @property
    def multiple_of(self):
        """
        Gets the multiple_of of this V1beta1JSONSchemaProps.

        :return: The multiple_of of this V1beta1JSONSchemaProps.
        :rtype: float
        """
        return self._multiple_of

    @multiple_of.setter
    def multiple_of(self, multiple_of):
        """
        Sets the multiple_of of this V1beta1JSONSchemaProps.

        :param multiple_of: The multiple_of of this V1beta1JSONSchemaProps.
        :type: float
        """

        self._multiple_of = multiple_of

    @property
    def _not(self):
        """
        Gets the _not of this V1beta1JSONSchemaProps.

        :return: The _not of this V1beta1JSONSchemaProps.
        :rtype: V1beta1JSONSchemaProps
        """
        return self.__not

    @_not.setter
    def _not(self, _not):
        """
        Sets the _not of this V1beta1JSONSchemaProps.

        :param _not: The _not of this V1beta1JSONSchemaProps.
        :type: V1beta1JSONSchemaProps
        """

        self.__not = _not

    @property
    def one_of(self):
        """
        Gets the one_of of this V1beta1JSONSchemaProps.

        :return: The one_of of this V1beta1JSONSchemaProps.
        :rtype: list[V1beta1JSONSchemaProps]
        """
        return self._one_of

    @one_of.setter
    def one_of(self, one_of):
        """
        Sets the one_of of this V1beta1JSONSchemaProps.

        :param one_of: The one_of of this V1beta1JSONSchemaProps.
        :type: list[V1beta1JSONSchemaProps]
        """

        self._one_of = one_of

    @property
    def pattern(self):
        """
        Gets the pattern of this V1beta1JSONSchemaProps.

        :return: The pattern of this V1beta1JSONSchemaProps.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """
        Sets the pattern of this V1beta1JSONSchemaProps.

        :param pattern: The pattern of this V1beta1JSONSchemaProps.
        :type: str
        """

        self._pattern = pattern

    @property
    def pattern_properties(self):
        """
        Gets the pattern_properties of this V1beta1JSONSchemaProps.

        :return: The pattern_properties of this V1beta1JSONSchemaProps.
        :rtype: dict(str, V1beta1JSONSchemaProps)
        """
        return self._pattern_properties

    @pattern_properties.setter
    def pattern_properties(self, pattern_properties):
        """
        Sets the pattern_properties of this V1beta1JSONSchemaProps.

        :param pattern_properties: The pattern_properties of this V1beta1JSONSchemaProps.
        :type: dict(str, V1beta1JSONSchemaProps)
        """

        self._pattern_properties = pattern_properties

    @property
    def properties(self):
        """
        Gets the properties of this V1beta1JSONSchemaProps.

        :return: The properties of this V1beta1JSONSchemaProps.
        :rtype: dict(str, V1beta1JSONSchemaProps)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this V1beta1JSONSchemaProps.

        :param properties: The properties of this V1beta1JSONSchemaProps.
        :type: dict(str, V1beta1JSONSchemaProps)
        """

        self._properties = properties

    @property
    def required(self):
        """
        Gets the required of this V1beta1JSONSchemaProps.

        :return: The required of this V1beta1JSONSchemaProps.
        :rtype: list[str]
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this V1beta1JSONSchemaProps.

        :param required: The required of this V1beta1JSONSchemaProps.
        :type: list[str]
        """

        self._required = required

    @property
    def title(self):
        """
        Gets the title of this V1beta1JSONSchemaProps.

        :return: The title of this V1beta1JSONSchemaProps.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this V1beta1JSONSchemaProps.

        :param title: The title of this V1beta1JSONSchemaProps.
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """
        Gets the type of this V1beta1JSONSchemaProps.

        :return: The type of this V1beta1JSONSchemaProps.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1beta1JSONSchemaProps.

        :param type: The type of this V1beta1JSONSchemaProps.
        :type: str
        """

        self._type = type

    @property
    def unique_items(self):
        """
        Gets the unique_items of this V1beta1JSONSchemaProps.

        :return: The unique_items of this V1beta1JSONSchemaProps.
        :rtype: bool
        """
        return self._unique_items

    @unique_items.setter
    def unique_items(self, unique_items):
        """
        Sets the unique_items of this V1beta1JSONSchemaProps.

        :param unique_items: The unique_items of this V1beta1JSONSchemaProps.
        :type: bool
        """

        self._unique_items = unique_items

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta1JSONSchemaProps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
