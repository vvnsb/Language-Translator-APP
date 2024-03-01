from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

root = tk.Tk()
root.title('Bhargav Language Translator')
root.geometry('530x330')
root.maxsize(530, 330)
root.minsize(530, 330)


Label(root, text="Project Bhargav", font="arial 20 bold", bg='white smoke').pack()

def translate():
    language_1 = t1.get("1.0", "end-1c")
    c1 = choose_language.get()

    if language_1 == '':
        messagebox.showerror('Language Translator', 'Please fill the box')
    else:
        translator = Translator()
        translation = translator.translate(language_1, dest=c1)
        
        t2.delete(1.0, 'end')
        t2.insert('end', translation.text)

def clear_text():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')

a = tk.StringVar()
auto_detect = ttk.Combobox(root, width=20, textvariable=a, state='readonly', font=('verdana', 10, 'bold'),)

auto_detect['values'] = ('Auto Detect',)
auto_detect.place(x=30, y=70)
auto_detect.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(root, width=20, textvariable=1, state='readonly', font=('verdana', 10, 'bold'),)

choose_language['values'] = (
    'Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali',
    'Bosnian', 'Bulgarian', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese (Simplified and Traditional)', 'Corsican',
    'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Filipino', 'Finnish', 'French',
    'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew',
    'Hindi', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese',
    'Kannada', 'Kazakh', 'Khmer', 'Kinyarwanda', 'Korean', 'Kurdish', 'Kyrgyz', 'Lao', 'Latin', 'Latvian',
    'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi',
    'Mongolian', 'Myanmar (Burmese)', 'Nepali', 'Norwegian', 'Odia (Oriya)', 'Pashto', 'Persian', 'Polish',
    'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi',
    'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tajik', 'Tamil',
    'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba',
    'Zulu',
)

choose_language.place(x=290, y=70)
choose_language.current(0)

t1 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
t1.place(x=10, y=100)

t2 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
t2.place(x=260, y=100)

button = Button(root, text="Translate", relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'), cursor="hand2",
                command=translate)
button.place(x=280, y=280)

clear_button = Button(root, text="Clear", relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'), cursor="hand2",
                      command=clear_text)
clear_button.place(x=380, y=280)

root.mainloop()
