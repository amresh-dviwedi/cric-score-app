import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

DATA_FILE = "cricket_data.json"

class CricketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cricket Stats Tracker")
        self.data = self.load_data()

        # UI Layout
        tk.Label(root, text="Player Profiles", font=('Arial', 16, 'bold')).pack(pady=10)
        
        self.profile_frame = tk.Frame(root)
        self.profile_frame.pack()

        self.update_ui()

        # Add Match Button
        tk.Button(root, text="+ Add Match Score", command=self.add_match, bg="green", fg="white").pack(pady=20)

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f: return json.load(f)
        return {"Aditya": [], "Lakshya": [], "Amresh": []}

    def save_data(self):
        with open(DATA_FILE, 'w') as f: json.dump(self.data, f)

    def update_ui(self):
        for widget in self.profile_frame.winfo_children(): widget.destroy()
        for player in self.data:
            btn = tk.Button(self.profile_frame, text=player, width=20, 
                            command=lambda p=player: self.show_profile(p))
            btn.pack(pady=5)

    def add_match(self):
        match_no = len(next(iter(self.data.values()))) + 1
        for player in self.data:
            score = simpledialog.askinteger("Input", f"Match {match_no}: Enter score for {player}")
            if score is not None:
                self.data[player].append(score)
        self.save_data()
        messagebox.showinfo("Success", f"Match {match_no} scores added!")

    def show_profile(self, name):
        scores = self.data[name]
        if not scores:
            messagebox.showinfo(name, "No matches played yet.")
            return
        total = sum(scores)
        avg = total / len(scores)
        highest = max(scores)
        msg = f"Total Matches: {len(scores)}\nTotal Runs: {total}\nAverage: {avg:.2f}\nHighest Score: {highest}"
        messagebox.showinfo(f"{name}'s Profile", msg)

if __name__ == "__main__":
    root = tk.Tk()
    app = CricketApp(root)
    root.mainloop()
