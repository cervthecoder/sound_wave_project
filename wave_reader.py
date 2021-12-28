import matplotlib.pyplot as plt
import numpy as np
import wave, sys

plt.rcParams['axes.facecolor'] = 'black'

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
    plt.figure(1)
    plt.plot(time, signal, color="white")
    path = path.replace(".wav", "")
    plt.savefig(path+'.png')
# mai# main
if __name__ == "__main__":
    
    # gets the command line Value
    path = sys.argv[1]
  
    visualize(path)

