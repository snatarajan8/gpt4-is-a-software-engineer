import tkinter as tk
from tkinter import messagebox
import requests

class AppUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Rich UI with Python")

        # Create a frame for buttons
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        # Placeholder buttons
        self.button1 = tk.Button(self.frame, text="Button 1", command=self.placeholder_function)
        self.button1.pack(side="left", padx=10)

        self.button2 = tk.Button(self.frame, text="Button 2", command=self.placeholder_function)
        self.button2.pack(side="left", padx=10)

        # API button
        self.api_button = tk.Button(self.root, text="Fetch Interesting Data", command=self.hit_api)
        self.api_button.pack(pady=20)

        # Label to display API data
        self.api_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.api_label.pack(pady=20)

    def placeholder_function(self):
        # Placeholder function for demo
        messagebox.showinfo("Info", "Placeholder function activated!")

    def hit_api(self):
        # Here, I'm using a random user API for demonstration. Replace with any API of your choice.
        response = requests.get("https://randomuser.me/api/")
        if response.status_code == 200:
            data = response.json()
            name = data["results"][0]["name"]
            formatted_name = f"{name['title']} {name['first']} {name['last']}"
            self.api_label.config(text=f"Random User's Name: {formatted_name}")
        else:
            messagebox.showerror("Error", "Failed to fetch data from the API!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppUI(root)
    root.mainloop()
