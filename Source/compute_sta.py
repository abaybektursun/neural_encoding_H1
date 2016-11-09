"""
Code to compute spike-triggered average.
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def compute_sta(stim, rho, num_timesteps):
    """Compute the spike-triggered average from a stimulus and spike-train.
    
    Args:
        stim: stimulus time-series
        rho: spike-train time-series
        num_timesteps: how many timesteps to use in STA
        
    Returns:
        spike-triggered average for num_timesteps timesteps before spike"""
    
    sta = np.zeros((num_timesteps,))

    # This command finds the indices of all of the spikes that occur
    # after 300 ms into the recording.
    spike_times = rho[num_timesteps:].nonzero()[0] + num_timesteps
    print(spike_times)
    print(rho[num_timesteps:].nonzero()[0])

    # Fill in this value. Note that you should not count spikes that occur
    # before 300 ms into the recording.
    num_spikes = len(spike_times)

    print("Number of spikes: ", num_spikes)
    
    # Compute the spike-triggered average of the spikes found.
    # Average of all of the vectors starting 300 ms (exclusive)
    # before a spike and ending at the time of the event (inclusive).
    # Each of these vectors defines a list of
    # samples that is contained within a window of 300 ms before each
    # spike. The average of these vectors should be completed in an
    # element-wise manner.

    for a_spikeIdx in spike_times:
        sta += stim[a_spikeIdx-num_timesteps:a_spikeIdx]

    sta /= num_spikes


    return sta