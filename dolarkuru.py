import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

# Dolar/TL kurunu çekme fonksiyonu
def get_dollar_to_tl():
    try:
        url = "https://bigpara.hurriyet.com.tr/doviz/dolar/"
        response = requests.get(url)
        response.raise_for_status()  # HTTP hataları için kontrol
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Kurun HTML içerisindeki yeri
        rate = soup.find("span", {"class": "value"}).text
        return rate
    except Exception as e:
        return f"Hata: {e}"

# Butona tıklandığında kur bilgisi gösterme
def show_dollar_rate():
    rate = get_dollar_to_tl()
    messagebox.showinfo("Dolar/TL Kuru", f"Güncel Dolar/TL Kuru: {rate}")

# Tkinter arayüzü
root = tk.Tk()
root.title("Dolar/TL Kuru Gösterici")
root.geometry("300x150")

label = tk.Label(root, text="Güncel Dolar/TL Kurunu Göster", font=("Arial", 12))
label.pack(pady=20)

button = tk.Button(root, text="Göster", command=show_dollar_rate, font=("Arial", 10))
button.pack(pady=10)

root.mainloop()
