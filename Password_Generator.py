import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("600x350")

        title_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold", "underline"), fg="blue")
        title_label.grid(row=0, column=0, columnspan=2, pady=(10, 10))

        tk.Label(root, text="Enter user name:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.user_entry = tk.Entry(root, font=("Arial", 12), width=25)
        self.user_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Enter password length:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.length_entry = tk.Entry(root, font=("Arial", 12), width=25)
        self.length_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Generated password:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = tk.Entry(root, font=("Arial", 12), width=25, fg="green")
        self.password_entry.grid(row=3, column=1, padx=10, pady=5)

        
        generate_btn = tk.Button(root, text="GENERATE PASSWORD", font=("Arial", 10, "bold"), command=self.generate_password, bg="blue", fg="white", width=20)
        generate_btn.grid(row=4, column=0, columnspan=2, pady=10)

        accept_btn = tk.Button(root, text="ACCEPT", font=("Arial", 10), command=self.accept_password, width=10)
        accept_btn.grid(row=5, column=0, columnspan=2, pady=5)

        reset_btn = tk.Button(root, text="RESET", font=("Arial", 10), command=self.reset_fields, width=10)
        reset_btn.grid(row=6, column=0, columnspan=2, pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choices(characters, k=length))
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
        except ValueError:
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, "Invalid length")

    def accept_password(self):
        print(f"User: {self.user_entry.get()}, Password: {self.password_entry.get()}")

    def reset_fields(self):
        self.user_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

root = tk.Tk()
app = PasswordGeneratorApp(root)
root.mainloop()
