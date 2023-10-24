# https://github.com/daryshtaev/properties_reader
# version 1.0.0

import jproperties
import os
from pathlib import Path


def initProperties(file='app.properties',directory=os.path.dirname(os.path.realpath(__file__))):
    configs_file = Path(os.path.join(directory, file))
    configs = jproperties.Properties()
    with open(configs_file, 'rb') as read_prop:
        configs.load(read_prop, "utf-8")
    return configs