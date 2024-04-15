import customtkinter as ctk
import ctk_color_picker_widget as CTkColorPicker

root = ctk.CTk()
root.title("ColorPicker")
root.iconbitmap("C:/Users/Philipp/Downloads/pngwing.com.ico")

cp = CTkColorPicker.CTkColorPicker(root, orientation="horizontal")
cp.pack(expand=True, fill="both")


root.mainloop()
