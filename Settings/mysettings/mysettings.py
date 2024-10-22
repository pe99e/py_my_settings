from configparser import ConfigParser
import os

SW_VERSION = 'v6'


class MySettings:

    def __init__(self, settings: dict, sw_version: str) -> None:
        self.settings = settings
        self.config_file = 'config_'+sw_version+'.ini'

    def create_init_file(self) -> None:
        if not os.path.isfile('config.ini'):
            self.load_and_save_settings('init')

    def load_and_save_settings(self, mode: str) -> None:

        """ the mode main is not necessary since I will change the value directly by opening the ini file
        """
        config = ConfigParser()
        config.read(self.config_file)

        for key in self.settings:

            if mode == 'init':
                if not config.has_section('default'):
                    config.add_section('default')

                config.set('default', key, self.settings[key])

                if not config.has_section('main'):
                    config.add_section('main')
                    # config.add_section('main')
                config.set('main', key, self.settings[key])

            elif mode == 'main':
                if not config.has_section('main'):
                    config.add_section('main')
                # config.add_section('main')

                config.set('main', key, self.settings[key])  # minutes

            with open(self.config_file, 'w') as f:
                config.write(f)

    def load_all_settings(self)->list:
        config = ConfigParser()
        config.read(self.config_file)
        #for each_section in config.sections():
      #  for (each_key, each_val) in config.items("main"):#each_section
        return [each_val for (each_key, each_val) in config.items("main")]

    def load_specific_settings(self, *key_setting: str) -> list:
        config = ConfigParser()
        config.read(self.config_file)
        return [each_val for (each_key, each_val) in config.items("main") if each_key in key_setting]

    def load_setting(self, key_setting: str) -> str:
        config = ConfigParser()
        config.read(self.config_file)
        return config.get('main', key_setting)
