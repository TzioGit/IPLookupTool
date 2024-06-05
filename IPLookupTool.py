import tkinter as tk
from tkinter import messagebox
import requests

def get_ip():
    try:
        response = requests.get('https://httpbin.org/ip')
        ip = response.json()['origin']
        messagebox.showinfo("IP Address", f"Your IP Address is: {ip}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get IP address: {e}")

app = tk.Tk()
app.title("IP Lookup Tool")
app.geometry("300x100")

button = tk.Button(app, text="Get My IP", command=get_ip)
button.pack(pady=20)

app.mainloop()
