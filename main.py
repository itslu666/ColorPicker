import customtkinter as ctk
import CTkColorPicker

root = ctk.CTk()

cp = CTkColorPicker.CTkColorPicker(root)
cp.pack(expand=True, fill="both")

root.mainloop()
