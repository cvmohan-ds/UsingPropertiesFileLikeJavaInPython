from jproperties import Properties
import os


def get_config(configuration="dev.properties"):
    configs = Properties()
    with open(configuration, "rb") as config_file:
        configs.load(config_file)
    item_views = configs.items()
    config_dict = {}
    for item in item_views:
        config_dict[item[0]] = item[1].data
    return config_dict


class ProductionConfig:
    props = None

    def __init__(self):
        # This will be loaded from a production config file present in Env.
        prop_file = os.environ.get("PROD_PROPS")
        self.props = get_config(configuration=prop_file)


class DevConfig:
    props = None

    # This will get information from the dev.properties file
    def __init__(self):
        self.props = get_config()
