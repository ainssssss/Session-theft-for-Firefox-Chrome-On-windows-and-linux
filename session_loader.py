import platform
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import pickle

def get_patch():
    global file_path
    file_path = filedialog.askopenfilename()
    if len(file_path) > 2:
        ###
        global path_info
        if os.name == 'nt':
            path_info = Label(root, text="{}".format("PATH LOADED"))
            path_info.config(text="PATH LOADED")
            path_info.config(font=("Arial", 10), border=0, bg="#1E1E1E", fg="green", width=20)
            path_info.place(x=75, y=350)

        elif os.name == 'posix':
            path_info = Label(root, text="{}".format("PATH LOADED"))
            path_info.config(font=("Arial", 10), border=0, bg="#1E1E1E", fg="green", width=20)
            path_info.place(x=74, y=300)


def GetLinkText():
    usr_input_link = str((inputtxt.get("1.0", END)))
    if len(usr_input_link) != 0:
        if "http://" in usr_input_link or "https://" in usr_input_link:
            url = usr_input_link
            url_link_others.destroy()
            LoadOtherWebisteSesionCookies(url, cookies)
        else:
            messagebox.showinfo(
                message="You need to put the complete url, an example would be:\n\nhttps://instagram.com \n\nIt is important to include the https or https",
                title="BAD URL FORMAT")


def open_url_link_input_usr():
    global url_link_others
    url_link_others = tk.Toplevel()
    url_link_others.geometry('400x120+100+200')
    url_link_others.config(background="#1E1E1E")

    url_label = Label(url_link_others, text="{}".format("URL"))
    url_label.config(font=("Arial", 10), border=0, bg="#1E1E1E", fg="white")
    url_label.place(x=180, y=5)

    global inputtxt
    inputtxt = tk.Text(url_link_others,
                       height=1,
                       width=30)

    inputtxt.place(x=80, y=40)

    button = tk.Button(url_link_others, text="Load Cookies")
    button.config(background="white", foreground="black", width=25, border=0, command=GetLinkText)
    button.place(x=90, y=75)


def get_selected_option():
    try:
        global cookies
        cookies = pickle.load(open(file_path, "rb"))

        if selected_option.get() == "youtube":
            # Youtube
            LoadYoutubeSesionCookies(cookies)
        elif selected_option.get() == "twitter":
            # Twitter
            LoadTwitterSesionCookies(cookies)
        elif selected_option.get() == "instagram":
            # Instagram
            LoadInstagramSesionCookies(cookies)
        elif selected_option.get() == "tictok":
            # TicTok
            LoadTicToklSesionCookies(cookies)

        elif selected_option.get() == "twitch":
            # Twitch
            LoadTwitchSesionCookies(cookies)

        elif selected_option.get() == "steam":
            # Twitch
            LoadSteamSesionCookies(cookies)

        elif selected_option.get() == "others":
            open_url_link_input_usr()

    except Exception as e:
        messagebox.showinfo(message=e, title="ERROR INFO")



def LoadTwitterSesionCookies():
    driver = webdriver.Firefox()
    driver.get("https://twitter.com/home")
    while True:
        try:
            looking_for_button = driver.find_element(By.CSS_SELECTOR, 'div.css-18t94o4:nth-child(1)').click()
            time.sleep(3)
            break
        except:
            None

    driver.delete_all_cookies()
    tw_cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in tw_cookies:
        driver.add_cookie(cookie)
    time.sleep(1)
    driver.refresh()

def LoadYoutubeSesionCookies(yt_cookies):
    driver = webdriver.Firefox()
    driver.get("https://www.youtube.com/channel/UC5il9pfohgXSZmjGKjefKSg")
    while True:
        try:
            looking_for_button = driver.find_element(By.XPATH, '/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]').click()
            time.sleep(3)
            break
        except:
            None

    driver.delete_all_cookies()
    for cookie in yt_cookies:
        driver.add_cookie(cookie)
    time.sleep(1)
    driver.refresh()

def LoadTwitterSesionCookies(twitter_cookies):
    driver = webdriver.Firefox()
    driver.get("https://www.twitter.com/")
    time.sleep(3)
    driver.delete_all_cookies()
    for cookie in twitter_cookies:
        driver.add_cookie(cookie)
    time.sleep(1)
    driver.refresh()

def LoadTicToklSesionCookies(tictok_cookies):
    driver = webdriver.Firefox()
    driver.get("https://www.tiktok.com/")
    time.sleep(3)
    driver.delete_all_cookies()
    for cookie in tictok_cookies:
        driver.add_cookie(cookie)
    time.sleep(1)
    driver.refresh()

def LoadTwitchSesionCookies(twitch_cookies):
    driver = webdriver.Firefox()
    driver.get("https://www.twitch.tv/")
    time.sleep(3)
    driver.delete_all_cookies()
    for cookie in twitch_cookies:
        driver.add_cookie(cookie)
    time.sleep(1)
    driver.refresh()

def LoadSteamSesionCookies(steam_cookies):
    driver = webdriver.Firefox()
    driver.get("https://store.steampowered.com/")
    time.sleep(3)
    driver.delete_all_cookies()
    for cookie in steam_cookies:
        driver.add_cookie(cookie)
    time.sleep(1)
    driver.refresh()
def LoadOtherWebisteSesionCookies(url,cookies):
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(3)
    driver.delete_all_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)
    time.sleep(1)
    driver.refresh()


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x346+500+200')
    root.config(background="#1E1E1E")
    root.title('Session Loader')
    root.resizable(False, False)

    global file_path
    file_path = ""
    options = ["tictok", "twitter", "youtube", "twitch","steam","instagram","others"]


    global path_info
    if os.name == 'nt':
        path_info = Label(root, text="{}".format("NO PATH LOADED"))
        path_info.config(font=("Arial", 10), border=0, bg="#1E1E1E", fg="red")
        path_info.place(x=72, y=265)

        select_a_webiste_label = Label(root, text="{}".format("SELECT A WEBSITE"))
        select_a_webiste_label.config(font=("Arial", 10), border=0, bg="#1E1E1E", fg="white")
        select_a_webiste_label.place(x=67, y=9)

        Load_Session = Label(root, text="{}".format("LOAD SESSION"))
        Load_Session.config(font=("Arial", 10), border=0, bg="#1E1E1E", fg="white")
        Load_Session.place(x=145, y=75)

        Select_a_Path = Label(root, text="{}".format("SELECT A PATH"))
        Select_a_Path.config(font=("Arial", 10), border=0, bg="#1E1E1E", fg="white")
        Select_a_Path.place(x=70, y=210)

        selected_option = tk.StringVar(root)
        selected_option.set(options[0])
        option_menu = tk.OptionMenu(root, selected_option, *options)
        option_menu.config(background="white", foreground="black", width=25, border=0)
        option_menu.place(x=31, y=34)

        button = tk.Button(root, text="Load Path", command=get_patch)
        button.config(background="white", foreground="black", width=10, border=0, height=5)
        button.place(x=155, y=105)

        button = tk.Button(root, text="Load Cookies", command=get_selected_option)
        button.config(background="white", foreground="black", width=25, border=0)
        button.place(x=31, y=235)

    elif os.name == 'posix':
        path_info = Label(root, text="{}".format("NO PATH LOADED"))
        path_info.config(font=("Arial", 10), border=0, bg="#1E1E1E", fg="red")
        path_info.place(x=84, y=300)

        select_a_webiste_label = Label(root, text="{}".format("SELECT A WEBSITE"))
        select_a_webiste_label.config(font=("Arial", 10), border=0, bg="#1E1E1E", fg="white")
        select_a_webiste_label.place(x=80, y=9)

        Load_Session = Label(root, text="{}".format("LOAD SESSION"))
        Load_Session.config(font=("Arial", 10), border=0, bg="#1E1E1E", fg="white")
        Load_Session.place(x=145, y=75)

        Select_a_Path = Label(root, text="{}".format("SELECT A PATH"))
        Select_a_Path.config(font=("Arial", 10), border=0, bg="#1E1E1E", fg="white")
        Select_a_Path.place(x=93, y=230)

        selected_option = tk.StringVar(root)
        selected_option.set(options[0])
        option_menu = tk.OptionMenu(root, selected_option, *options)
        option_menu.config(background="white", foreground="black", width=25, border=0)
        option_menu.place(x=31, y=34)

        button = tk.Button(root, text="Load Path", command=get_patch)
        button.config(background="white", foreground="black", width=10, border=0, height=5)
        button.place(x=145, y=105)

        button = tk.Button(root, text="Load Cookies", command=get_selected_option)
        button.config(background="white", foreground="black", width=25, border=0)
        button.place(x=31, y=255)

    root.mainloop()



