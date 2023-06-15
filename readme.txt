A colored starfield to measure perception of time

This is a Python script that creates a starfield animation using the Tkinter library. It generates a fullscreen window with a canvas where stars of random colors move towards the viewer. After a certain time, the animation pauses and a separate window opens to ask the user questions on the colors displayed, and time judgment (Duration Estimation and Passing of Time Judgment)
This paradigm, widely inspired from Jording et al, 2022, allows to test the influence of low-level visual stimuli on the experience of passage and duration of time for 20s intervals. 
The starfield environment could enable us to study the effects of basic visual aspects of a scene (velocity and density of stars in the starfield) and the duration (20s, 40s and 60s for instance) of the situation, both embedded in a color tracking task. 

The color tracking task controls for the attention of the participant. He will be asked what color was predominant among the stars at the very end of the starfield before the questions. The color rate is always unbalanced and can be 90% pink, 10% yellow or 90% yellow, 10% pink. Every 4 seconds, the color composition changes a random choice determines whether it is a majority of pink stars or majority of yellow stars.

By concerns of time, I didn’t code a first page of explanations and instructions for the participant, and I didn’t make sure that the code was capable of creating of csv files with the answers of each participant. I focused on the stimulus, that is, the starfield illusion.
