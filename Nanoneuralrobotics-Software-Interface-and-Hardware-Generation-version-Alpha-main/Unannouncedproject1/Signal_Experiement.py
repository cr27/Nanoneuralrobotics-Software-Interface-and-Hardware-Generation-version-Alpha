#Freitas Jr., Robert A. Nanomedicine, Volume I: Basic Capabilities.
# Landes Bioscience, 1999.

from typing import Dict
import random

import numpy as np
from matplotlib import pyplot as plt


class Signal():
    def __init__(self):
        MHzfrequency = v * 1000000

        # Period in seconds s
        T_Period = 1 / v_frequency # Period of oscillations

        # Frequency in Hz
        v_frequency = 1 / T_period # Frequency (v) represents the number of  oscillations per unit time (usually
        # measured in hertz,Hz) # A set of periods.

        # An electromagnetic wave passing through the human body declines in intensity as it heats tissues and is
        # attenuated approximately according to:
        # Intensity in watts per square meter (W/m^2)
        # Depth of tissue penetration in meters (m)
        # Attenuation factor in meters^-1 (m^-1)

        # Randomly generate the maximum safe incident intensity
        I_not = random.uniform(0, 100)  # watts/m^2

        # Calculate the power per unit area transmitted through the tissue
        I = I_not ** (2 * dx * ae)  # watts/m^2

        dx = random.randint(1, 10)  # dx is depth of tissue penetration (meters),

        ae = ae = random.randint(1, 5) # aE (meter-1) is the total attenuation factor including scattering and
        # absorption, the inverse of the mean

        bits_signal_intensity = random.uniform(0,10**6)# bit range for signal intensity



    def generate_signal(self):
        # Generate a non-physiological signal (a sine wave with added noise)
        #time = np.linspace(0, 1, 1000)
        # signal = np.sin(2 * 10 * time) + 0.5 * np.random.randn(1000)

        from scipy.signal import hilbert

        # # Apply the Hilbert Transform to extract the envelope (i.e., the amplitude)
        # self.envelope = np.abs(hilbert(signal))

        # Print the maximum amplitude value
        # self.amplitude = np.max(self.envelope)
        import random
        self.amplitude = random.uniform(0.3, 0.9)
        print(self.amplitude)

        # # Plot the raw signal
        # plt.plot(time, signal, label='Raw Signal')
        #
        # # Plot the extracted envelope
        # plt.plot(time, self.envelope, label='Envelope')
        #
        # # Set axis labels and legend
        # plt.xlabel('Time (s)')
        # plt.ylabel('Amplitude')
        # plt.legend()
        #
        # # Show the plot
        # plt.show()

    def set_amplitude(self):
        #self.amplitude = np.max(self.envelope)
        print("Your amplitude is:", self.amplitude)

    def get_amplitude(self):
        return self.amplitude
