import tkinter as tk
import requests

class CryptoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Курсы криптовалют")

        self.crypto_list = ["bitcoin", "ethereum", "ripple", "litecoin", "dogecoin"]
        self.labels = {}

        self.create_widgets()
        self.update_crypto_prices()

    def create_widgets(self):
        for crypto in self.crypto_list:
            label = tk.Label(self.root, text=crypto.capitalize() + ": ", font=("Helvetica", 16))
            label.pack()
            self.labels[crypto] = tk.Label(self.root, text="...", font=("Helvetica", 16))
            self.labels[crypto].pack()

        self.refresh_button = tk.Button(self.root, text="Обновить", command=self.update_crypto_prices)
        self.refresh_button.pack(pady=20)

    def update_crypto_prices(self):
        url = "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=usd".format(','.join(self.crypto_list))
        try:
            response = requests.get(url)
            data = response.json()
            for crypto in self.crypto_list:
                price = data[crypto]['usd']
                self.labels[crypto].config(text="${:,.2f}".format(price))
        except Exception as e:
            print("Ошибка:", e)
            for crypto in self.crypto_list:
                self.labels[crypto].config(text="Ошибка загрузки")

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoApp(root)
    root.mainloop()