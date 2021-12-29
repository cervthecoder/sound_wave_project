import matplotlib.pyplot as plt
import numpy as np
import wave, sys

plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'

def visualize(path: str):

    # reads the audiofile
    raw = wave.open(path)

    # reads all the frames
    # -1 to indicate all of frames
    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype ="int16")
    
    # get the framerate
    f_rate = raw.getframerate()

    # Divide the framerate by size of the signal to get time (x-axis)
    time = np.linspace(
            0,
            len(signal)/f_rate,
            num= len(signal)
            )
    # Use matplolib to graph our signal
    plt.figure(figsize=(11.7,8.3))
    plt.plot(time, signal, color="black")
    path = path.replace(".wav", "")
    plt.savefig(path+'.png')
# mai# main
if __name__ == "__main__":
    
    # gets the command line Value
    path = sys.argv[1]
  
    visualize(path)

