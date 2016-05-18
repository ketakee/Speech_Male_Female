# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 18:19:48 2016
This program plots the output of the wav file of male and female voices saying goodbye.
The sound can be found at:
http://consumingfireartisticcreations.weebly.com/the-sound-effects-library.html
listed as :
_male_voice_goodbye_sound_effect
_female_voice_goodbye_sound_effect

@author: Ketakee Nimavat
"""
import scipy.io.wavfile
import scipy
#import wave
from matplotlib import pyplot as plt
rate1m, data1m = scipy.io.wavfile.read('D:\\Speech-Text-Speech\\male\\_male_voice_goodbye_sound_effect.wav')
rate2m,data2m=scipy.io.wavfile.read('D:\\Speech-Text-Speech\\female\\_female_voice_goodbye_sound_effect.wav')
print rate1m, rate2m
print data1m,data2m
plt.plot(data1m)
plt.plot(data2m)
plt.show()

print "/*****************************************************************/"
#
#rate1m, data1m = scipy.io.wavfile.read('D:\\Speech-Text-Speech\\female\\_female_voice_good_evening_sound_effect.wav')
#rate2m,data2m=scipy.io.wavfile.read('D:\\Speech-Text-Speech\\female\\_female_voice_goodbye_sound_effect.wav')
#print rate1m, rate2m
#print data1m,data2m
#z=plt.plot(data1m)
#plt.show()
#y=plt.plot(data2m)
#plt.show()
