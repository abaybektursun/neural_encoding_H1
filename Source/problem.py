from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

import pickle

from compute_sta import compute_sta


file_name = 'data_c1p8_py.pickle'

with open(file_name, 'rb') as f:
    data = pickle.load(f)

stim = data['stim']
rho  = data['rho']

# DEBUG ######################################################################### DEBUG #
print ("stim: ", len(stim))
print ("stim: ", type(stim))
print ("rho: ", len(rho))
print ("rho: ", type(rho))

vals = []
unique = [x for x in rho if x not in vals and (vals.append(x) or True)]

print ("rho vals: ", vals)

plt.hist(stim, bins='auto')
plt.title("Histogram with 'auto' bins")
plt.show()
# DEBUG ######################################################################### DEBUG #

time_widnow     = 300
sampling_period = 2
num_timesteps   = int(time_widnow/sampling_period)

sta = compute_sta(stim, rho, num_timesteps)

print("STA: ", sta)

time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')

plt.show()