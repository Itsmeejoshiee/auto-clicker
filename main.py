import pyautogui
import tkinter as tk
import keyboard
import threading

# Get the size of the primary monitor.
screenWidth, screenHeight = pyautogui.size()

# Get the XY position of the mouse.
currentMouseX, currentMouseY = pyautogui.position()

# Global switch to control clicking
switch = False

def Switchfunction(state):
    global switch
    switch = state
    if switch:
        threading.Thread(target=autoclickerfunction, daemon=True).start()  # Start clicking in a separate thread

# Register a hotkey to stop clicking
keyboard.add_hotkey('ctrl+`', lambda: Switchfunction(False))

#Register a hotkey to start clicking
keyboard.add_hotkey('+', lambda: Switchfunction(True))

#AutoClicker function
def autoclickerfunction():
    while switch:
        speed=slider.get()
        pyautogui.click()
        pyautogui.sleep(speed)  


# Create GUI window
root = tk.Tk()
root.title("Auto Clicker")
root.geometry("500x500")

label = tk.Label(root, text="Controls", font=("Arial", 24))
label.pack(padx=10, pady=10)
label = tk.Label(root, text="press + to start\npress ctrl+` to stop", font=("Arial", 16))
label.pack(padx=10, pady=10)
label = tk.Label(root, text="Adjust AutoClicker Speed Here:", font=("Arial", 16))
label.pack()
slider= tk.Scale(root, from_=0.1, to=1.0, resolution=0.1, orient="horizontal", length=200)
slider.set(0.5)
slider.pack(padx=5, pady=5)

button = tk.Button(root, 
                   text="Start", 
                   font=("Arial", 16), 
                   bg="green", fg="white",
                   command=lambda: Switchfunction(True)
                   )
button.pack(padx=10, pady=10)

stop_button = tk.Button(root, 
                        text="Stop", 
                        font=("Arial", 16), 
                        bg="red", fg="white",
                        command=lambda: Switchfunction(False))
stop_button.pack(padx=10, pady=10)

root.mainloop()
