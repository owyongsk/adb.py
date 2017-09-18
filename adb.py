#!/usr/local/bin/python3
import os,time,sys

class ADB():
    def connect(ip_addr):
        os.system("adb connect %s:5555" % ip_addr)

    def disconnect():
        os.system("adb disconnect")

    def tap(x,y):
        os.system("adb shell input tap %s %s" % (x,y))
        time.sleep(1)

    def power():
        print("Pressing the virtual power button...")
        os.system("adb shell input keyevent KEYCODE_POWER")

    def home():
        os.system("adb shell input keyevent KEYCODE_HOME")
        time.sleep(1)

    def type_text(text):
        print("Typing ... '%s'" % text)
        os.system("adb shell input text %s" % text.replace(" ","%s"))

    def screencap():
        os.system("adb shell screencap -p /sdcard/screen.png")
        os.system("adb pull /sdcard/screen.png")
        os.system("adb shell rm /sdcard/screen.png")

class WhatsApp():
    def launch():
        print("Launching WhatsApp...")
        ADB.home()
        ADB.home()
        ADB.tap(165,1375)
        ADB.tap(240,547)

    def chats_home():
        ADB.tap(100,155)         # Taps back on any chat
        ADB.tap(300,300)         # Taps 'CHATS'

    def message_contact(full_name):
        print("Searching for %s" % full_name)
        ADB.tap(890,129)         # Tap search icon top right
        ADB.type_text(full_name)
        ADB.tap(504,433)         # Select found contact

    def open_ancel():
        ADB.tap(677,493)

    def open_test():
        print("Opening my bitch account")
        ADB.tap(677,725)

    def press_send():
        ADB.tap(1004,1138)

class Jarvis():
    def confirm(dialog="Do you want to continue? [y/n]"):
        print("Capturing screencap...")
        ADB.screencap()
        os.system("open screen.png")

        if input(dialog) != "y":
            sys.exit()

    def say_to(contact,text):
        ADB.power()
        WhatsApp.launch()
        WhatsApp.chats_home()
        WhatsApp.message_contact(contact)
        ADB.type_text(text)
        Jarvis.confirm()
        WhatsApp.press_send()

# adb.connect("192.168.0.103")
# import pdb; pdb.set_trace()
