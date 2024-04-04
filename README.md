# CoquiPyGUI
Tkinter/Python GUI for the CoquiTTS tool.

A graphical frontend for the Coqui Text to Speech synthesizer, which is usually accessed on the command line.

This depends on TTS and Playsound, which can be installed using these commands:

```
pip3 install TTS
pip3 install playsound
```

Note: You may need to run the program via the command line, using ```python3 /location/of/program.py```, or else it won't synthesize. Installing TTS will automatically install all of its dependencies, which is about 1.7GB, and when you first press "Synthesize", it will download the default mode I have preset, which is another 1.6GB.

To change the model, go into the config.ini file and change it. ( I do not have a GUI implenentation yet, I am working on it tho ).
