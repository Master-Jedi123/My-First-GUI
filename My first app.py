import customtkinter
from CTkMenuBar import *

root = customtkinter.CTk()
root.geometry("500x500")
root.title("Coolpad")
root.iconbitmap('emoji-4.ico')


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


menu = CTkMenuBar(root)
button_1 = menu.add_cascade("File")
button_2 = menu.add_cascade("Edit")

dropdown1 = CustomDropdownMenu(widget=button_1)
dropdown1.add_option(option="Open", command=lambda: print("Open"))
dropdown1.add_option(option="Save")

dropdown1.add_separator()

sub_menu = dropdown1.add_submenu("Export As")
sub_menu.add_option(option=".TXT")
sub_menu.add_option(option=".PDF")

dropdown2 = CustomDropdownMenu(widget=button_2)
dropdown2.add_option(option="Cut")
dropdown2.add_option(option="Copy")
dropdown2.add_option(option="Paste")
dropdown2.add_separator()
dropdown2.add_option(option="Undo")

entry = customtkinter.CTkTextbox(root, width=10000, height=10000, corner_radius=0, font=('Arial', 18), activate_scrollbars=True)
entry.pack()

scrollbar = customtkinter.CTkScrollbar(root, command=entry.yview, hover=True)
scrollbar.pack()


root.mainloop()