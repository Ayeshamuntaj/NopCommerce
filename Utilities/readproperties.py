import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configuration\\config.ini')

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url=config.get('commonInfo',"baseurl")
        return url
    @staticmethod
    def getusername():
        username=config.get('commonInfo','username')
        return username
    @staticmethod
    def getpassword():
        password=config.get('commonInfo','password')
        return password