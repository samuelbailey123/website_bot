import webbrowser #functions to open browsers 
import time #delay timer to make bot seem more real
import subprocess #close application

number = 0 #counter
while(number != 10): 
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s' #set the path to open chrome | for some reason it dones't open by the default
    webbrowser.get(chrome_path).open("https://www.decimamedia.com") #opens chrome to the link
    time.sleep(5) 
    subprocess.call(['osascript', '-e', 'tell application "chrome" to quit'])
    number += 1
print("Finished!")