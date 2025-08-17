#code for UI
import tkinter as tk
from tkinter import filedialog,messagebox,ttk
from ReadCSV import QueryEngine
class CSVQueryApp:
    def __init__(self,root):
        self.root = root
        self.root.title("CSV Query tool")
        self.root.geometry("800x600")
        self.engine=QueryEngine()

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

         # Mode Switch
        self.sql_mode = tk.BooleanVar(value=True)
        self.sql_checkbox = tk.Checkbutton(root, text="Use SQL Mode", variable=self.sql_mode)
        self.sql_checkbox.pack(pady=5)

        self.run_btn = tk.Button(root, text="Run Query", command=self.run_query)
        self.run_btn.pack(pady=5)

        # --- Result Table Section ---
        self.tree = ttk.Treeview(root, show="headings")
        self.tree.pack(fill="both", expand=True, pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)
            try:
                df = self.engine.load_file(file_path)
                messagebox.showinfo("Info", f"Loaded file: {file_path}")
                self.display_dataframe(df)
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def run_query(self):
        query = self.query_text.get("1.0", tk.END).strip()
        if not query:
            messagebox.showwarning("Warning", "Please enter a query!")
            return
        try:
            result = self.engine.run_query(query, sql_mode=self.sql_mode.get())
            self.display_dataframe(result)
        except Exception as e:
            messagebox.showerror("Error", f"Query failed:\n{e}")

    def display_dataframe(self, df):
        # Clear existing table
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(df.columns)

        # Set headings
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center")

        # Insert rows
        for _, row in df.iterrows():
            self.tree.insert("", tk.END, values=list(row))

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVQueryApp(root)
    root.mainloop()
