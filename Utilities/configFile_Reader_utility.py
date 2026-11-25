'''here we will read the config.ini file so that we can use the configuration in our program and ese hi ye script likh ke ham apne
main program me config.ini ka data use kr skte ha and kal ko kuch change hua to program me change krne ki need nahi
just config.ini file me change kre'''
from configparser import ConfigParser

config = ConfigParser() #initilze the configparser class
config.read('D:/study/automation/PHASE 5/Appium - Mobile App Automation in Python/liveProject/configurationFile/conf.ini')#here we read the config file
print(config.get("App_related_data","appActivity")) #read the appActivity you can store in a variable to use in PG
print(config.get("Server_URL","remote_url"))

'''syntax->
config.get("section_name","keys") 
'''