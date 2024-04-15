import customtkinter as ctk
import ctk_color_picker_widget as CTkColorPicker

root = ctk.CTk()

cp = CTkColorPicker.CTkColorPicker(root)
cp.pack(expand=True, fill="both")


root.mainloop()
