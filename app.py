import tkinter as tk
from tkinter import messagebox
from logica import DoublyLinkedList

class AchievementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel de Logros Premium")
        self.root.geometry("650x550")
        self.root.configure(bg="#F8F9FA")

        self.dll = DoublyLinkedList()
        self.current_idx = 0
        
        self.p_title = "Título del Logro..."
        self.p_desc = "Descripción breve..."
        
        self.setup_ui()
        self.update_display()

    def setup_ui(self):
        self.header = tk.Frame(self.root, bg="#3F37C9", height=60)
        self.header.pack(fill="x", side="top")
        
        tk.Label(self.header, text="REGISTRO DE LOGROS PRO", bg="#3F37C9", fg="white", 
                 font=("Segoe UI", 14, "bold")).pack(pady=15)

        self.card = tk.Frame(self.root, bg="white", padx=40, pady=40, highlightbackground="#E9ECEF", highlightthickness=1)
        self.card.pack(pady=30, padx=50, fill="both", expand=True)

        self.title_label = tk.Label(self.card, text="", bg="white", fg="#2B2D42", font=("Segoe UI", 22, "bold"))
        self.title_label.pack(pady=(0, 10))

        self.line = tk.Frame(self.card, bg="#3F37C9", height=2, width=100)
        self.line.pack(pady=10)

        self.desc_label = tk.Label(self.card, text="", bg="white", fg="#8D99AE", font=("Segoe UI", 12), wraplength=400)
        self.desc_label.pack(pady=20)

        self.nav_frame = tk.Frame(self.root, bg="#F8F9FA")
        self.nav_frame.pack(pady=10)

        btn_style = {"bg": "#FFFFFF", "fg": "#3F37C9", "font": ("Segoe UI", 10, "bold"), "width": 12, "pady": 8, "border": 1, "activebackground": "#3F37C9", "activeforeground": "white"}
        
        self.prev_btn = tk.Button(self.nav_frame, text="ANTERIOR", command=self.prev_achievement, **btn_style)
        self.prev_btn.pack(side="left", padx=10)

        self.next_btn = tk.Button(self.nav_frame, text="SIGUIENTE", command=self.next_achievement, **btn_style)
        self.next_btn.pack(side="left", padx=10)

        self.del_btn = tk.Button(self.nav_frame, text="ELIMINAR", command=self.delete_achievement, bg="#EF233C", fg="white", font=("Segoe UI", 10, "bold"), width=12, pady=8, border=0)
        self.del_btn.pack(side="left", padx=10)

        self.add_section = tk.Frame(self.root, bg="#FFFFFF", padx=20, pady=20, highlightbackground="#E9ECEF", highlightthickness=1)
        self.add_section.pack(side="bottom", fill="x", padx=30, pady=(0, 20))

        tk.Label(self.add_section, text="DESBLOQUEAR NUEVO HITO", bg="white", fg="#ADB5BD", font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0, 10))

        self.entry_frame = tk.Frame(self.add_section, bg="white")
        self.entry_frame.pack(fill="x")

        self.entry_title = tk.Entry(self.entry_frame, font=("Segoe UI", 10), bg="#F8F9FA", border=0, highlightthickness=1, highlightbackground="#E9ECEF", fg="#ADB5BD")
        self.entry_title.insert(0, self.p_title)
        self.entry_title.bind("<FocusIn>", lambda e: self.on_focus_in(self.entry_title, self.p_title))
        self.entry_title.bind("<FocusOut>", lambda e: self.on_focus_out(self.entry_title, self.p_title))
        self.entry_title.pack(side="left", expand=True, fill="x", padx=5, ipady=5)

        self.entry_desc = tk.Entry(self.entry_frame, font=("Segoe UI", 10), bg="#F8F9FA", border=0, highlightthickness=1, highlightbackground="#E9ECEF", fg="#ADB5BD")
        self.entry_desc.insert(0, self.p_desc)
        self.entry_desc.bind("<FocusIn>", lambda e: self.on_focus_in(self.entry_desc, self.p_desc))
        self.entry_desc.bind("<FocusOut>", lambda e: self.on_focus_out(self.entry_desc, self.p_desc))
        self.entry_desc.pack(side="left", expand=True, fill="x", padx=5, ipady=5)

        self.add_btn = tk.Button(self.entry_frame, text="AGREGAR", command=self.add_achievement, bg="#4CC9F0", fg="white", font=("Segoe UI", 10, "bold"), border=0, padx=20)
        self.add_btn.pack(side="right", padx=5, ipady=3)

        self.status = tk.Label(self.root, text="0 / 0", bg="#F8F9FA", fg="#ADB5BD", font=("Segoe UI", 9))
        self.status.pack(side="bottom")

    def on_focus_in(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="#2B2D42")

    def on_focus_out(self, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="#ADB5BD")

    def update_display(self):
        if self.dll.length == 0:
            self.title_label.config(text="Panel Vacío")
            self.desc_label.config(text="Usa el formulario inferior para registrar tus hitos.")
            self.status.config(text="0 / 0")
            return

        node = self.dll.traverse_to_index(self.current_idx)
        val = node.value
        self.title_label.config(text=val["title"].upper())
        self.desc_label.config(text=val["description"])
        self.status.config(text=f"PASO {self.current_idx + 1} DE {self.dll.length}")

    def prev_achievement(self):
        if self.current_idx > 0:
            self.current_idx -= 1
            self.update_display()

    def next_achievement(self):
        if self.current_idx < self.dll.length - 1:
            self.current_idx += 1
            self.update_display()

    def add_achievement(self):
        t = self.entry_title.get()
        d = self.entry_desc.get()
        if t and d and t != self.p_title and d != self.p_desc:
            self.dll.append({"title": t, "description": d})
            self.on_focus_out(self.entry_title, self.p_title)
            self.on_focus_out(self.entry_desc, self.p_desc)
            self.entry_title.delete(0, tk.END)
            self.entry_title.insert(0, self.p_title)
            self.entry_title.config(fg="#ADB5BD")
            self.entry_desc.delete(0, tk.END)
            self.entry_desc.insert(0, self.p_desc)
            self.entry_desc.config(fg="#ADB5BD")
            if self.dll.length == 1: self.current_idx = 0
            self.update_display()
            self.root.focus_set()
        else:
            messagebox.showwarning("Error de Entrada", "Por favor completa todos los campos correctamente.")

    def delete_achievement(self):
        if self.dll.length > 0:
            self.dll.remove(self.current_idx)
            if self.current_idx >= self.dll.length and self.dll.length > 0:
                self.current_idx = self.dll.length - 1
            self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = AchievementApp(root)
    root.mainloop()
