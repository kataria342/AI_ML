"""
import pyttsx3
import matplotlib

engine = pyttsx3.init()
userText = input("Enter the text you want to say \n")
engine.say(userText)
engine.runAndWait()
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()