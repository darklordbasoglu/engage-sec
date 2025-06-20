import tkinter as tk
from tkinter import ttk, messagebox
import smtplib
from email.mime.text import MIMEText

def send_email():
    sender = entry_from.get()
    password = entry_password.get()
    target = entry_to.get()
    link = entry_link.get()
    platform = combo_platform.get()

    if platform == "Instagram":
        subject = "Instagram Güvenlik Uyarısı"
        body = "Sayın kullanıcı,\n\nInstagram hesabınızda olağandışı bir giriş tespit edildi.\nHesabınız geçici olarak kilitlenmiştir.\n\nLütfen aşağıdaki bağlantıya tıklayarak şifrenizi yenileyin:\n" + link
    elif platform == "Twitter":
        subject = "Twitter Hesap Güvenliği"
        body = "Sayın kullanıcı,\n\nTwitter hesabınızda olağandışı bir etkinlik gözlemlendi.\nHesabınızın güvenliği için aşağıdaki bağlantıya tıklayıp giriş yapın:\n" + link
    elif platform == "Facebook":
        subject = "Facebook Güvenlik Bildirimi"
        body = "Sayın kullanıcı,\n\nFacebook hesabınızda şüpheli bir işlem algılandı.\nGiriş doğrulaması yapmanız gerekmektedir:\n" + link

    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = target

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)

        messagebox.showinfo("Başarılı", "Sahte e-posta gönderildi.")

    except Exception as e:
        messagebox.showerror("Hata", f"E-posta gönderilemedi:\n{e}")

root = tk.Tk()
root.title("Sosyal Mühendislik Farkındalık - Mail Gönderici")
root.geometry("600x400")

tk.Label(root, text="Sosyal Mühendislik E-Posta Simülatörü", font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Gönderen Gmail Adresi:").grid(row=0, column=0, sticky="e")
entry_from = tk.Entry(frame, width=40)
entry_from.grid(row=0, column=1)

tk.Label(frame, text="Gmail Uygulama Şifresi:").grid(row=1, column=0, sticky="e")
entry_password = tk.Entry(frame, width=40, show="*")
entry_password.grid(row=1, column=1)

tk.Label(frame, text="Hedef E-posta Adresi:").grid(row=2, column=0, sticky="e")
entry_to = tk.Entry(frame, width=40)
entry_to.grid(row=2, column=1)

tk.Label(frame, text="Phishing Linki:").grid(row=3, column=0, sticky="e")
entry_link = tk.Entry(frame, width=40)
entry_link.grid(row=3, column=1)

tk.Label(frame, text="Platform Seçin:").grid(row=4, column=0, sticky="e")
combo_platform = ttk.Combobox(frame, values=["Instagram", "Twitter", "Facebook"])
combo_platform.grid(row=4, column=1)
combo_platform.set("Instagram")

tk.Button(root, text="Sahte E-posta Gönder", command=send_email).pack(pady=20)

tk.Label(root, text="© 2025 Siber Güvenlik Farkındalık Projesi", font=("Arial", 8)).pack(side="bottom", pady=5)

root.mainloop()
