# Spike-triggered average in the H1 neuron
Assignment for Computational Neuroscience class by University of Washington

##Characterizing coding in the H1 neuron
The data set provided with is recorded from the blowfly H1 neuron. In this experiment, an electrode is placed in the fly’s brain– in a region called the lobula plate– where there is a set of large neurons that encode information about wide-field motion, motion of the entire visual field. We are recording from one of these neurons, H1, which encodes horizontal motion.
![alt text](docs/1.png)

##Reverse correlation: the spike-triggered average
This code calculates the spike-triggered average.The spike-triggered average is the average stimulus that precedes a spike. To calculate it, you need to know the spike times, aligned with the stimulus. Link to the data can be found in the file_link.txt
![alt text](docs/2.png)

##What do we learn from the spike-triggered average?
What is the spike-triggered average useful for? We can use it to predict the times of spikes given a new random piece of stimulus.


![alt text](docs/3.png)
![alt text](docs/4.png)
