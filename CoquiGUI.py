# Python GUI program for CoquiTTS

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
from playsound import playsound
from configparser import ConfigParser
import os

def bugExit(code):
    return 1, code

cfg = ConfigParser()
app_directory = os.path.dirname(__file__)

cfg.read('%s/config.ini'%(app_directory))

# Sythesize text to speech with CoquiTTS.
def synthesize():
    playsound('%s/Sounds/MyClick.wav'%(app_directory))
    file_path = filedialog.askdirectory()
    file_name = simpledialog.askstring('Name File', 'Input a name for the file')
    if file_name == 'None' or file_name == None:
        return "Error: No file name"
    text_tts = text_entry.get(1.0, "end-1c")
    model_name = cfg.get('MAIN', 'modelName')
    cmd = 'tts --text "%s" --model_name "%s" --out_path %s/%s.wav'%(text_tts, model_name, file_path, file_name)
    os.system('echo "Running CoquiTTS!"')
    os.system('echo '+cmd)
    os.system(cmd)
    playsound('%s/Sounds/jobs_done.mp3'%(app_directory))
    pass

# App settings.
def settings_screen():

    def apply_settings():
        current_voice = voice_settings.get()
        cfg.set('MAIN','modelName','%s'%(current_voice))
        pass

    settings_window = Toplevel()
    settings_window.geometry("400x500")
    settings_rframe = Frame(settings_window)
    settings_rframe.pack(side=LEFT)

    settings_label = Label(settings_window, text="Settings for the app.")
    settings_label.pack()
    settings_about = Label(settings_window, text="Currently a work in progress")
    settings_about.pack(pady = 10)

    voice_settings = ttk.Combobox(
        settings_window,
        state="readonly",
        values=["tts_models/en/jenny/jenny","tts_models/en/ljspeech/glow-tts","tts_models/en/ljspeech/tacotron2-DDC_ph","tts_models/en/ljspeech/fast_pitch"]
    )
    voice_settings.pack(pady=5)

    apply_button = Button(settings_window, text="Apply Settings", command= apply_settings)
    apply_button.pack()
    pass

# The About Screen.
def about_screen():
    about_window = Toplevel()
    about_window.geometry("200x200")

    about_version = Label(about_window, text="CoquiGUI v0.1.0")
    about_version.pack()

    about_text = Label(about_window, text="I wanted a GUI frontend to CoquiTTS but I couldn't really find any, so I decided to make my own.", wraplength=170)
    about_text.pack()
    pass

root = Tk()
root.geometry("400x400")

frame = Frame(root)
frame.pack()

# Add menubar. Cascades used for compatibility with MacOS.
menubar = Menu(root, tearoff=0)
filemenu = Menu(menubar)
menubar.add_cascade(label="CoquiGUI", menu=filemenu)
# Menu buttons.
filemenu.add_command(label="About", command= about_screen)
filemenu.add_command(label="Prefrences", command= settings_screen)
filemenu.add_separator()
filemenu.add_command(label="Exit", command= quit)

# Text label.
label = Label(frame, text="GUI interface for CoquiTTS.")
label.pack(pady=10)

# Text entry.
text_entry = Text(frame, width= 40, height= 15, wrap=WORD)
text_entry.pack(pady=20)

# Sythesize button.
synth_button = Button(frame, text="Synthesize", command= synthesize)
synth_button.pack()

root.config(menu = menubar)
root.title("CoquiGUI")
root.mainloop()
