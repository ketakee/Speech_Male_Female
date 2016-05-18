# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:28:02 2016

@author: Ketakee Nimavat
"""
#import wave
from matplotlib import pyplot as plt
import scipy.io.wavfile as wavfile
import pylab as pl
import numpy as np
rate, data = wavfile.read('D:\\Speech-Text-Speech\\male\\_male_voice_goodbye_sound_effect.wav')
t = np.arange(len(data[:,0]))*1.0/rate
pl.plot(t, data[:,0])
pl.show() 
p = 20*np.log10(np.abs(np.fft.rfft(data[:2048, 0])))
f = np.linspace(0, rate/2.0, len(p))
plt.plot(f, p)
plt.xlabel("Frequency(Hz)")
plt.ylabel("Power(dB)")
plt.show()
