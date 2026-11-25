'''creating a utility named as logs which generates the logs'''
import logging


def log():                                 #absolute path of folder with file name
    logging.basicConfig(filename="D:/study/automation/PHASE 5/Appium - Mobile App Automation in Python/liveProject/Logs/my_test.log",
                        format="%(asctime)s - %(levelname)s - %(message)s",#the written pattern of logs
                        level=logging.INFO) #it records normal execution information

    logger=logging.getLogger()
    return logger

'''now import this module in your program file and call the log function there to generate the logs '''
'''after calling this function , write variable.info("this is a new log") or if you want to report an error in log file then use 
-> varibale.error("this is an error message")'''

#TODO: CALL THIS FUNCTION HERE TO UNDERSTAND HOW THE LOG FILE IS GENERATED ?
#here we temporary call this function here to understand how log file will generate , although you will only call this in the program file where you need by importing
my_logger=log()
my_logger.info("this is an info message") #records the execution activity of a test case
my_logger.error("this is an error message")#if an error occurs during execution , then i
# t will record it