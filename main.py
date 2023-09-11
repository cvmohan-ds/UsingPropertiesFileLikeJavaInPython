import project_config


def dev_configuration_information():
    dev_info = project_config.DevConfig().props
    print(dev_info)


def prod_configuration_information():
    prod_info = project_config.ProductionConfig().props
    print(prod_info)


if __name__ == "__main__":
    print("This is a standalone CLI showing dev config and prod config")
    print("Development configuration from dev.properties file")
    dev_configuration_information()
    print("Production Properties from file configured in environment variables")
    prod_configuration_information()
