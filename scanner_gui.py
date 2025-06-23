import socket
import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime

# Function to scan a single port
def scan_port(host, port, output_box):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        if result == 0:
            output_box.insert(tk.END, f"✅ Port {port} is OPEN\n", 'open')
        else:
            output_box.insert(tk.END, f"❌ Port {port} is CLOSED\n", 'closed')
        sock.close()
    except Exception as e:
        output_box.insert(tk.END, f"⚠️ Error scanning port {port}: {e}\n", 'error')

# Main scan function
def start_scan():
    host = entry_ip.get()
    start = entry_start_port.get()
    end = entry_end_port.get()

    if not host or not start or not end:
        messagebox.showerror("Input Error", "Please fill all fields.")
        return

    try:
        start = int(start)
        end = int(end)
        if start > end:
            raise ValueError
    except:
        messagebox.showerror("Input Error", "Please enter valid port numbers.")
        return

    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, f"🎯 Scanning: {host}\n", 'info')
    output_box.insert(tk.END, f"🕒 Started at: {datetime.now()}\n\n", 'info')

    for port in range(start, end + 1):
        thread = threading.Thread(target=scan_port, args=(host, port, output_box))
        thread.start()

# Build the GUI
root = tk.Tk()
root.title("🧠  Port Scanner")
root.geometry("650x580")
root.config(bg="#2a003f")  # dark violet

# Title
title = tk.Label(root, text="🛡️  PORT SCANNER", font=("Consolas", 20, "bold"),
                 fg="#39ff14", bg="#2a003f")
title.pack(pady=15)

# Input frame
frame = tk.Frame(root, bg="#2a003f")
frame.pack(pady=10)

label_style = {"font": ("Consolas", 12), "bg": "#2a003f", "fg": "#ffffff"}

tk.Label(frame, text="🌐 IP / Domain:", **label_style).grid(row=0, column=0, sticky="e")
entry_ip = tk.Entry(frame, width=30, font=("Consolas", 12), bg="#1e0030", fg="#39ff14", insertbackground='white')
entry_ip.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="🔢 Start Port:", **label_style).grid(row=1, column=0, sticky="e")
entry_start_port = tk.Entry(frame, width=30, font=("Consolas", 12), bg="#1e0030", fg="#39ff14", insertbackground='white')
entry_start_port.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="🔢 End Port:", **label_style).grid(row=2, column=0, sticky="e")
entry_end_port = tk.Entry(frame, width=30, font=("Consolas", 12), bg="#1e0030", fg="#39ff14", insertbackground='white')
entry_end_port.grid(row=2, column=1, padx=10, pady=5)

# Scan button
scan_button = tk.Button(root, text="⚡ START SCAN", command=start_scan,
                        bg="#8a2be2", fg="white", font=("Consolas", 14, "bold"), width=25)
scan_button.pack(pady=20)

# Output box
output_box = scrolledtext.ScrolledText(root, width=75, height=15,
                                       font=("Courier New", 11), bg="#0f001a", fg="#00ffcc", insertbackground='white')
output_box.pack(pady=10)

# Add custom tags for color
output_box.tag_config('open', foreground='#00ff00')
output_box.tag_config('closed', foreground='#ff0055')
output_box.tag_config('info', foreground='#66ccff')
output_box.tag_config('error', foreground='orange')

# Footer
footer = tk.Label(root, text="🧬 Made by B. Manya Shetty", font=("Consolas", 10), bg="#2a003f", fg="#999999")
footer.pack(pady=8)

root.mainloop()
