import webbrowser #import browser to open website
import time #time to sleep to keep it looping
import subprocess #close the browser to save ram and not overload computer 

number = 0
while(number != 10):   
    webbrowser.open("https://www.decimamedia.com")
    time.sleep(4)
    subprocess.call(['osascript', '-e', 'tell application "safari" to quit'])
    number += 1
print("Finished!")
