from mysettings.settings import MySettings


if __name__ == '__main__':
   settings= {
  "watchdirectory": "ciao",
  "file_match_dict_path": "file_matching.json"
}
   sett=MySettings(settings)


   sett.createinitfile()
   print("LOAD SETTINGS")
  # print(sett.load_settings_loop())

  # print(sett.load_specific_settings_loop("watchdirectory"))
   var_lists=sett.load_specific_settings("watchdirectory",'file_match_dict_path')
   #print(sett.load_specific_settings_loop_multi("watchdirectory",'file_match_dict_path'))
   print(var_lists[1])
