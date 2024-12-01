import tkinter as tk
from tkinter import messagebox
import webbrowser
import socket

# Function to visit a local webpage
def visit_page():
    url = entry_url.get()
    if url:
        webbrowser.open(f"http://{url}")
    else:
        messagebox.showwarning("Input Error", "Please enter a valid URL.")

# Function to check port connectivity
def check_port(port):
    url = entry_url.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a valid URL.")
        return
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((url, port))
        messagebox.showinfo("Port Check", f"Port {port} is open.")
    except socket.error:
        messagebox.showwarning("Port Check", f"Port {port} is closed.")
    finally:
        sock.close()

# Function to handle port checking buttons
def check_port_21():
    check_port(21)

def check_port_22():
    check_port(22)

def check_port_80():
    check_port(80)

def check_port_443():
    check_port(443)

def check_port_3306():
    check_port(3306)

# Create the main window
root = tk.Tk()
root.title("Local Website Visitor and Port Checker")

# Create and place the components
label_url = tk.Label(root, text="Enter URL:")
label_url.grid(row=0, column=0, padx=5, pady=5)

entry_url = tk.Entry(root, width=50)
entry_url.grid(row=0, column=1, padx=5, pady=5)

button_visit = tk.Button(root, text="Visit Page", command=visit_page)
button_visit.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

label_ports = tk.Label(root, text="Check Port Connectivity:")
label_ports.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

button_port_21 = tk.Button(root, text="Port 21", command=check_port_21)
button_port_21.grid(row=3, column=0, padx=5, pady=5)

button_port_22 = tk.Button(root, text="Port 22", command=check_port_22)
button_port_22.grid(row=3, column=1, padx=5, pady=5)

button_port_80 = tk.Button(root, text="Port 80", command=check_port_80)
button_port_80.grid(row=4, column=0, padx=5, pady=5)

button_port_443 = tk.Button(root, text="Port 443", command=check_port_443)
button_port_443.grid(row=4, column=1, padx=5, pady=5)

button_port_3306 = tk.Button(root, text="Port 3306", command=check_port_3306)
button_port_3306.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
