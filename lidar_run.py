import os

pswd = "imagineer"
path = os.getcwd() + r"//rplidar_sdk//output//Linux//Release//ultra_simple"
##path = r"//home//imagineer//Desktop//test//rplidar_sdk//output//Linux//Release//ultra_simple"

os.system("sudo " + path + " --channel --serial /dev/ttyUSB0 256000")
os.system(pswd)


print(f"Current dir:{os.getcwd()}")



