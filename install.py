# installer for weewx-pwd driver
# Copyright 2022 Carsten Günther
# based on the driver for the Vaisala WXT5xx by Matthew Wall
# https://github.com/matthewwall/weewx-wxt5x0

from weecfg.extension import ExtensionInstaller

def loader():
    return PWDInstaller()

class PWDInstaller(ExtensionInstaller):
    def __init__(self):
        super(PWDInstaller, self).__init__(
            version="0.1",
            name='pwd',
            description='Collect data from Vaisala PWD hardware',
            author="Carsten Guenther",
            author_email="cguenther@users.sourceforge.net",
            files=[('bin/user', ['bin/user/pwd.py'])]
        )