# https://github.com/daryshtaev/properties_reader
# version 1.0.1

import jproperties
from pathlib import Path


def get_property(property_name, property_default_value=None, file="app.properties", encoding="utf-8"):
    configs_file = Path(file)
    configs = jproperties.Properties()
    with open(configs_file, 'rb') as read_prop:
        configs.load(read_prop, encoding)
    property_value = configs.get(property_name)
    if property_value is not None:
        property_value = property_value.data
    else:
        property_value = property_default_value
    return property_value
