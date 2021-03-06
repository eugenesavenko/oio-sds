# Copyright (C) 2017 OpenIO SAS, as part of OpenIO SDS
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3.0 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library.

import math


def int_value(value, default):
    if value in (None, 'None'):
        return default
    try:
        value = int(value)
    except (TypeError, ValueError):
        raise
    return value


def float_value(value, default):
    if value in (None, 'None'):
        return default
    try:
        value = float(value)
    except (TypeError, ValueError):
        raise
    return value


TRUE_VALUES = set(('true', '1', 'yes', 'on', 't', 'y'))


def true_value(value):
    return value is True or \
        (isinstance(value, basestring) and value.lower() in TRUE_VALUES)


METRIC_SYMBOLS = ("", "K", "M", "G", "T", "P", "E", "Z", "Y")


def convert_size(size, unit=""):
    if size == 0:
        return "0%s" % unit
    i = int(math.log(size, 1000))
    if i != 0:
        p = math.pow(1000, i)
        size = round(size / p, 3)
    return "%s%s%s" % (size, METRIC_SYMBOLS[i], unit)
