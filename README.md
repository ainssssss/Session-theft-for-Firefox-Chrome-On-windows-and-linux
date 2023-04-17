#  Session-theft-for-Firefox-Chrome-On-windows-and-linux

This project is made for educational purposes and the creator is not responsible for the uses of the application.

## How does it work?

This stealer works with two .py files, one is in charge of obtaining the user's sessions and the other allows the attacker to load the sessions.

For this, the selenium library is used to load the user's profile from the previous browsers and it jumps between the chosen websites to obtain the sessions.

Once the sessions are obtained they are uploaded to mega so that the attacker can download the session and using the session loader you can get the session without the need to enter users or passwords and bypassing the two-factor authentication.


## Demo 
[![demo video](https://www.dsecctv.com/images/Demo%20clip%20icon%20md.png)](https://www.youtube.com/watch?v=vQ8_pBteLfM "Stealer Demo")


## ¿How to configure the Stealer?
To configure the stealer is very easy just go to the file stealer.py and look for the two variables that put email and password and modify it with your mega credentials, this is necessary so you can upload files to your personal mega by connecting to mega using mega.py.

```python
    global email
    email = "your mail"
    global password
    password = "your password "
```


## Installation

These two scripts have been written using Python 3.9.2 below I attach the pip command to install all the necessary libraries to run it.

```python
  pip install tkinter time pickle platform re mega.py

```
    


## Authors

- [@ainssssss](https://github.com/ainssssss)
