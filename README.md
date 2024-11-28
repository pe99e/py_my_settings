# Readme
## Initilise the class MySettings with:
 1. a dictionary contaning the name of the setting as key and the value
 2. setting version number

use the createinitfile() method to create the init file that will contain all the settings

use load_setting(setting_name) to load a single setting and load_all_settings() to load all the settings  (it will return a list containing the value of the settings) 



## Example Code

from mysettings.settings import MySettings


if __name__ == '__main__':
   settings= {
  "watchdirectory": "ciao",
  "file_match_dict_path": "file_matching.json"
}
   sett=MySettings(settings)


   sett.createinitfile()
   print("LOAD SETTINGS")
   var_lists=sett.load_specific_settings("watchdirectory",'file_match_dict_path')
   #print(sett.load_specific_settings_loop_multi("watchdirectory",'file_match_dict_path'))
   print(var_lists[1])
