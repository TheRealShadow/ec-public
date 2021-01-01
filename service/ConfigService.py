import configparser
import shutil

base_configfile_path = 'resources/empireconfig.cfg'
current_configfile_path = 'resources/current_empireconfig.cfg'


def init():
    shutil.copy2(base_configfile_path, current_configfile_path)


def get_string(section, parameter):
    config = get_config()
    try:
        return config.get(section, parameter)
    except:
        return None


def get_boolean(section, parameter):
    config = get_config()
    try:
        return config.getboolean(section, parameter)
    except:
        return None


def get_float(section, parameter):
    config = get_config()
    try:
        return config.getfloat(section, parameter)
    except:
        return None


def get_int(section, parameter):
    config = get_config()
    try:
        return config.getint(section, parameter)
    except:
        return None


def set(section, parameter, value):
    config = get_config()
    config.set(section, parameter, value)
    # Writing our configuration file to 'example.cfg'
    with open(current_configfile_path, 'w') as configfile:
        config.write(configfile)
    with open(base_configfile_path, 'w') as configfile:
        config.write(configfile)


def get_config():
    config = configparser.RawConfigParser()
    config.read(current_configfile_path)
    return config