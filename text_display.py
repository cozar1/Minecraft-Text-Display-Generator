import tkinter as tk
from tkinter import Toplevel, PhotoImage
from tkcolorpicker import askcolor
import tkinter.font as tkFont
import pyperclip

# New color codes and their respective names
color_codes = [
    ("#AA0000", ""),
    ("#FF5555", ""),
    ("#FFAA00", ""),
    ("#FFFF55", ""),
    ("#00AA00", ""),
    ("#55FF55", ""),
    ("#55FFFF", ""),
    ("#00AAAA", ""),
    ("#0000AA", ""),
    ("#5555FF", ""),
    ("#FF55FF", ""),
    ("#AA00AA", ""),
    ("#FFFFFF", ""),
    ("#AAAAAA", ""),
    ("#555555", ""),
    ("#000000", ""),
]

# Initialize scale variable
scale = 1

def open_emoji_window():
    emoji_window = Toplevel(root)
    emoji_window.title("Emoji Selector")
    emoji_window.geometry("400x400")
    emoji_window.config(bg="#121221")
    
    emojis = ["😊", "😂", "❤️", "👍", "👏", "🎉", "🌟", "🔥", "✨", "🌈", "🚀", "🍕", "🎸", "⚽", "📚"]
    
    def insert_emoji(emoji):
        text_entry.insert(tk.END, emoji)
        emoji_window.destroy()
        update_generated_command()

    for i, emoji in enumerate(emojis):
        emoji_button = tk.Button(emoji_window, text=emoji, font=("Segoe UI Emoji", 16), command=lambda e=emoji: insert_emoji(e), bg="#4c4c66", relief="raised", border="10", fg="#FFFFFF")
        emoji_button.grid(row=i // 4, column=i % 4, padx=5, pady=5)


# Function to update the generated command and title
def update_generated_command(event=None):
    global scale  # Declare scale as a global variable
    selected_color = color_entry.get()
    is_bold = bold_var.get()
    
    font = tkFont.Font(family='F77 Minecraft', size=int(16 * scale), weight=tkFont.BOLD if is_bold else tkFont.NORMAL)
    text_entry.configure(foreground=selected_color, font=font)
    
    generated_text = text_entry.get('1.0', 'end-1c')
    str;scale
    generated_command = f'/summon minecraft:text_display ~ ~1 ~ {{text:\'{{"text":"{generated_text}","color":"{selected_color}","bold":{str(is_bold).lower()}}}\',CustomNameVisible:1,billboard:"center",transformation:{{scale:[{scale}.0,{scale}.0,{scale}.0]}}}}'

    generated_command_text.delete(1.0, tk.END)
    generated_command_text.insert(tk.END, generated_command)
    generated_title.config(text="Generated Command")

# Function to set the selected color when a square button is clicked
def set_color(hex_color):
    color_entry.delete(0, tk.END)
    color_entry.insert(0, hex_color)
    update_generated_command()

# Function to open color picker and update the color entry box
def choose_color():
    color = askcolor(color_entry.get(), root)
    if color:
        color_entry.delete(0, tk.END)
        color_entry.insert(0, color[1])  # Set the selected color
        update_generated_command()

# Function to copy the generated command to clipboard
def copy_to_clipboard():
    generated_command = generated_command_text.get(1.0, tk.END)
    pyperclip.copy(generated_command)

# Create the main window
root = tk.Tk()
root.title("Generator")
root.geometry("800x600")
root.configure(bg="#121221")

# Create a title box
title_frame = tk.Frame(root, bg="#4c4c66",  )
title_frame.pack( padx=10)

title_label = tk.Label(title_frame, text="Text Display Entity Generator", fg="white", font=("F77 Minecraft", 24, "bold"), bg="#4c4c66", relief="raised" ,border="10",  )
title_label.pack()

# Create a frame for the color and bold options
options_frame = tk.Frame(root, bg="#4c4c66")
options_frame.pack()

# Color options
color_label = tk.Label(options_frame, text="Text Color (Hex):", bg="#4c4c66", fg="white", font=("F77 Minecraft", 18))
color_label.grid(row=0, column=0)

color_entry = tk.Entry(options_frame, width=12, font=("F77 Minecraft", 16), relief="raised" ,border="10",  )
color_entry.insert(0, "#FFFFFF")  # Default color is black
color_entry.grid(row=0, column=1)
color_entry.bind("<KeyRelease>", update_generated_command)  # Update on key release

#emojis
emoji_icon_path = "smiley_face_icon.png"  # Replace with the actual path to your icon
emoji_icon = PhotoImage(file=emoji_icon_path).subsample(18, 18)  # Adjust the subsample factor as needed
emoji_button = tk.Button(options_frame, image=emoji_icon, command=open_emoji_window, bg="#4c4c66", relief="raised", border="10")
emoji_button.grid(row=0, column=5, padx=5)

# Color wheel button
color_wheel_button = tk.Button(options_frame, text="Color Wheel", command=choose_color, bg="#4c4c66", fg="white", font=("F77 Minecraft", 18), relief="raised" ,border="10",  )
color_wheel_button.grid(row=0, column=2, padx=5)

# Bold option
bold_var = tk.BooleanVar()
bold_var.set(False)

bold_checkbutton = tk.Checkbutton(options_frame, text="Bold", variable=bold_var, bg="#29283a", fg="white", font=("F77 Minecraft", 18), command=update_generated_command, relief="raised" ,border="10",  )
bold_checkbutton.grid(row=0, column=3, padx=5)

# Square buttons for color selection
square_buttons_frame = tk.Frame(options_frame, bg="#29283a", relief="raised" ,border="10",  )
square_buttons_frame.grid(row=0, column=4, padx=5)

for i, (hex_color, _) in enumerate(color_codes):
    square_button = tk.Button(square_buttons_frame, width=4, height=2, bg=hex_color, command=lambda hc=hex_color: set_color(hc), relief="raised" ,border="10",  )
    square_button.grid(row=0, column=i, padx=2)

# Create the text entry box for the generated command
text_entry = tk.Text(root, height=8, width=60, wrap=tk.WORD, relief="raised" ,border="10",  )
text_entry.configure(font=("F77 Minecraft", 16, "normal"), foreground="black",background="#232339", fg="#FFFFFF")
text_entry.pack()
text_entry.bind("<KeyRelease>", update_generated_command)  # Update on key release

# Create a label for the generated command
generated_title = tk.Label(root, text="Generated Command", font=("F77 Minecraft", 16, "bold"), bg="#4c4c66", fg="#FFFFFF", relief="raised" ,border="10",  )
generated_title.pack()

# Create the text box for the generated command
generated_command_text = tk.Text(root, height=8, width=60, wrap=tk.WORD, relief="raised" ,border="10",  )
generated_command_text.configure(font=("F77 Minecraft", 16, "normal"),background="#232339", fg="#FFFFFF")
generated_command_text.pack()

# Copy button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#4c4c66", fg="white", font=("F77 Minecraft", 18), relief=tk.RAISED,border="10", )
copy_button.pack()

root.mainloop()

