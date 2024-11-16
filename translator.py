from tkinter import *
from googletrans import Translator, LANGUAGES

# Initialize the Translator
translator = Translator()

# Initialize the main window
root = Tk()
root.title("Google Translator")
root.geometry("800x450")
root.config(bg="#f0f0f5")

# Function to translate the text
def translate_text():
    source_text = text_input.get("1.0", END).strip()
    src_lang = src_lang_var.get()
    dest_lang = dest_lang_var.get()
    
    if src_lang == "Auto Detect":
        translation = translator.translate(source_text, dest=dest_lang)
    else:
        translation = translator.translate(source_text, src=src_lang, dest=dest_lang)
    
    text_output.delete("1.0", END)
    text_output.insert(END, translation.text)
    text_output.tag_configure("center", justify="center")
    text_output.tag_add("center", "1.0", "end")

# Language options
languages = ["Auto Detect"] + list(LANGUAGES.values())

# Source language selection
src_lang_var = StringVar()
src_lang_var.set("english")
src_lang_menu = OptionMenu(root, src_lang_var, *languages)
src_lang_menu.config(width=20, bg="#ffdddd", font=("Arial", 12, "bold"), highlightthickness=1)
src_lang_menu.grid(row=0, column=0, padx=20, pady=10)

# Swap Button
swap_button = Button(root, text="⇄", command=lambda: swap_languages(), font=("Arial", 16), bg="#ffe4b5", relief=FLAT)
swap_button.grid(row=0, column=1, padx=10)

# Destination language selection
dest_lang_var = StringVar()
dest_lang_var.set("hindi")  # Default to Hindi
dest_lang_menu = OptionMenu(root, dest_lang_var, *languages)
dest_lang_menu.config(width=20, bg="#c6e2ff", font=("Arial", 12, "bold"), highlightthickness=1)
dest_lang_menu.grid(row=0, column=2, padx=20, pady=10)

# Text input area
text_input_label = Label(root, text="Enter Text", bg="#f0f0f5", font=("Arial", 14, "bold"), fg="#333333")
text_input_label.grid(row=1, column=0, sticky="w", padx=20)
text_input = Text(root, height=8, width=40, font=("Arial", 14), wrap=WORD, borderwidth=2, relief="solid")
text_input.grid(row=2, column=0, padx=20, pady=10)

# Translate button
translate_button = Button(root, text="Translate", command=translate_text, bg="#32cd32", fg="white", font=("Arial", 14, "bold"), padx=10, pady=5)
translate_button.grid(row=2, column=1, pady=10)

# Text output area
text_output_label = Label(root, text="Translation", bg="#f0f0f5", font=("Arial", 14, "bold"), fg="#333333")
text_output_label.grid(row=1, column=2, sticky="w", padx=20)
text_output = Text(root, height=8, width=40, font=("Arial", 14), wrap=WORD, borderwidth=2, relief="solid", bg="#e8f4ff")
text_output.grid(row=2, column=2, padx=20, pady=10)
text_output.tag_configure("center", justify="center")

# Swap languages function
def swap_languages():
    src_lang = src_lang_var.get()
    dest_lang = dest_lang_var.get()
    src_lang_var.set(dest_lang)
    dest_lang_var.set(src_lang)
    text_input_content = text_input.get("1.0", END)
    text_input.delete("1.0", END)
    text_input.insert(END, text_output.get("1.0", END))
    text_output.delete("1.0", END)
    text_output.insert(END, text_input_content)

# Run the GUI loop
root.mainloop()
