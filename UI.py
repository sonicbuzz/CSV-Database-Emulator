#code for UI
import tkinter as tk
from tkinter import filedialog,messagebox,ttk
class CSVQueryApp:
    def __init__(self,root):
        self.root = root
        self.root.title("CSV Query tool")
        self.root.geometry("800x600")

        #--file path section
        self.file_label = tk.Label(root, text="CSV File:")
        self.file_label.pack(pady=5)

        self.file_entry = tk.Entry(root, width=60)
        self.file_entry.pack(pady=5)

        self.browse_btn = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_btn.pack(pady=5)

         # --- Query Section ---
        self.query_label = tk.Label(root, text="Enter Query:")
        self.query_label.pack(pady=5)

        self.query_text = tk.Text(root, height=5, width=80)
        self.query_text.pack(pady=5)

        self.run_btn = tk.Button(root, text="Run Query", command=self.run_query)
        self.run_btn.pack(pady=5)

        # --- Result Table Section ---
        self.tree = ttk.Treeview(root, show="headings")
        self.tree.pack(fill="both", expand=True, pady=10)

    # GUI Logic Only (placeholders for functionality)
    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)
            messagebox.showinfo("Info", f"Selected file: {file_path}")

    def run_query(self):
        query = self.query_text.get("1.0", tk.END).strip()
        if not query:
            messagebox.showwarning("Warning", "Please enter a query!")
            return
        # Placeholder: later you’ll add CSV + SQL execution here
        messagebox.showinfo("Info", f"Query entered:\n{query}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CSVQueryApp(root)
    root.mainloop()
