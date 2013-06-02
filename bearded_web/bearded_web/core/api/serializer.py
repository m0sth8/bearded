# -*- coding: utf-8 -*-
import re
import json

import django
from django.core.serializers import json as django_json

from tastypie.serializers import Serializer


def underscoreToCamel(match):
    return match.group()[0] + match.group()[2].upper()


def camelize(data):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            new_key = re.sub(r"[a-z]_[a-z]", underscoreToCamel, key)
            new_dict[new_key] = camelize(value)
        return new_dict
    if isinstance(data, (list, tuple)):
        for i in range(len(data)):
            data[i] = camelize(data[i])
        return data
    return data


def camelToUnderscore(match):
    return match.group()[0] + "_" + match.group()[1].lower()


def underscorize(data):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            new_key = re.sub(r"[a-z][A-Z]", camelToUnderscore, key)
            new_dict[new_key] = underscorize(value)
        return new_dict
    if isinstance(data, (list, tuple)):
        for i in range(len(data)):
            data[i] = underscorize(data[i])
        return data
    return data


class CamelCaseJSONSerializer(Serializer):
    formats = ['json']
    content_types = {
        'json': 'application/json',
    }

    def to_json(self, data, options=None):
        # Changes underscore_separated names to camelCase names to go from python convention to javacsript convention
        options = options or {}
        data = self.to_simple(data, options)
        camelized_data = camelize(data)
        if django.get_version() >= '1.5':
            return django_json.json.dumps(data, cls=django_json.DjangoJSONEncoder, sort_keys=True, ensure_ascii=False)
        else:
            return json.dumps(data, cls=django_json.DjangoJSONEncoder, sort_keys=True, ensure_ascii=False)

    def from_json(self, content):
        # Changes camelCase names to underscore_separated names to go from javascript convention to python convention
        data = json.loads(content)
        underscored_data = underscorize(data)
        return underscored_data