'''
AIS stands for Axon Initial Segment. It is a specialized region located at the beginning of the axon, near the cell body
or soma of a neuron. The AIS plays a crucial role in the generation and propagation of action potentials, which are
electrical impulses that allow neurons to communicate with each other. The AIS contains a high concentration of
voltage-gated ion channels, such as sodium channels, that are responsible for initiating and shaping action potentials.
It serves as a critical site for integrating and initiating electrical signals in neurons.
The AIS is where the action potential is generated and then propagated along the axon to transmit information
to other neurons. In the context of the quote you provided, endoneurobots are described as nanorobots that interface
with all human-brain neurons at the AIS. This suggests that these nanorobots are designed to directly interact with
and influence the electrical activity of neurons at the point where action potentials are initiated.
########################################################################################################################
Active Propulsion: The nanobot may have its own propulsion system, such as tiny motors or flagella-like structures,
enabling it to actively navigate through the bloodstream and reach the target neuron.  This could involve swimming or
crawling motions propelled by chemical reactions or other energy sources.
########################################################################################################################
The manipulation and transmission of neural signals by nanodevices can involve various techniques depending on the
specific implementation and desired effects. Here are a few possibilities:

1. Electrical Stimulation: Nanodevices can generate electrical currents or voltages that directly interface with
neural tissue. By applying specific patterns or amplitudes of electrical stimulation, they can modulate the neural
activity and alter the perception of sensory signals.

2. Optogenetics: This technique involves the use of light-sensitive proteins (opsins) that can be expressed in neurons.
Nanodevices equipped with optogenetic tools can emit light pulses to activate or inhibit specific neural populations,
thereby modulating the sensory information processing.

3. Neural Encoding/Decoding: Nanodevices can interface with neural circuits to encode sensory information into specific
patterns of electrical stimulation or decode existing neural activity patterns. By modulating the patterns or timing
cues of these electrical signals, they can influence how sensory information is processed and perceived.

4. Chemical Manipulation: Some nanodevices may be designed to release specific molecules or neurotransmitters in the
vicinity of neural tissue. This can modulate neural activity by altering the chemical environment and neurotransmitter
balance, thereby affecting sensory processing.
########################################################################################################################
"The synaptobots would reside in the proper monitoring position within the neurons, in close proximity to presynaptic or
postsynaptic structures. Once in place, these neuralnanorobots would monitor the action potentials and the structural
changes initiated by the action-potential-based functional data. These data would be transferred from the synaptobots
to corresponding endoneurobots (in some cases, with communications and other support from nearby gliabots). Once the
data is received by the endoneurobots, it would proceed to the previously installed in vivo high-speed nanofiber-optic
network, for subsequent transfer to the central units that are responsible for transmitting data to an external
supercomputer. The auxiliary nanofiber-optic network system would provide essential support for the data that is
transmitted by the endoneurobots and synaptobots, thereby minimizing their onboard data storage capacity requirements.
The external supercomputer would communicate with the cloud and handle data post-processing."

"All three types of neuralnanorobots (endoneurobots, gliabots, and synaptobots) would monitor action potential-based
electrical information using the same types of FET-based nanosensors embedded in their surfaces"

The protocol for regularly updating the number of synaptobots in the brain (due to nanorobot damage(malfunctioning
software/hardware), synapse elimination, neuron death, new synaptic formation, etc.) would be initiated by endoneurobots

Facilitated and mediated by endoneurobots and gliabots, the synaptobots would subsequently transmit 5.52 × 1016 bits/sec
of continuous action potential data (Martins et al., 2012) via an in vivo nanofiber-optic network system.
########################################################################################################################
In the context of the quote you provided, the exact mechanism by which the nanobots know when they have arrived at the
Axon Initial Segment (AIS) is not specified. However, it can be assumed that the nanobots are designed with
sophisticated sensing capabilities and navigation systems to detect and identify the AIS.

There are several possible approaches the nanobots could use to locate the AIS:

1. Molecular cues: The nanobots may be programmed to recognize specific molecular markers or signals that are present
at the AIS. These markers could be unique to the AIS or specific to the type of neuron they are targeting.

2. Electrical signals: The nanobots may be equipped with sensors that can detect the electrical activity or voltage
changes associated with the AIS. They could be designed to respond to specific patterns or characteristics of electrical
signals to identify the AIS.

3. Imaging techniques: The nanobots could utilize imaging techniques, such as microscopy or nanoscale imaging
technologies, to visualize and locate the AIS. This could involve detecting structural features or specific protein
distributions that are indicative of the AIS.

4. Communication with external systems: The nanobots could communicate with external monitoring or control systems to
receive guidance or confirmation of their location. This could involve wireless communication or other means of data
exchange to provide real-time feedback on their position.

It's important to note that the specific mechanisms used by hypothetical nanobots to locate the AIS would depend on
their design and capabilities. The field of nanorobotics is still in its early stages, and practical implementations
and methods for precise targeting and navigation of nanobots within the human body are still being explored and
developed.

'''
import math

from nanoneuroantenna import Antenna
from abc import ABC, abstractmethod
import numpy as np
import random
intrinsic_voltage = random.uniform(-70, -55)
received_signal = random.uniform(1,10) # measured in MHz
class Endoneurobot(Antenna): # Inheriting functions from Antenna parent class
    apply_voltage = 0 # measured in millivolts
    def __init__(self, on_off, sense, apply_voltage):
        super().__init__(on_off, sense)
        self.required_receiver_voltage() # Invoke Inheritance
        self.required_transmitter_voltage() # Invoke Inheritance
        r = 10.0  # Distance from the antenna (in meters)
        k = 2.0  # Wavenumber (in radians per meter)
        theta = math.pi / 4  # Angle between radial direction and propagation direction (in radians)
        E_0 = 10 # the electric field strength at the antenna measured in volts per meter
        self.calculate_power_density(E_0,r,k,theta) # Invoke Inheritance
        self.apply_voltage = apply_voltage  # measured in millivolts




    @abstractmethod # Abstraction
    def movement(self):
        '''
        The length of the dendritic to axon initial segment (AIS) varies depending on the type of neuron.
        In general, the AIS is about 20-60 micrometers long. However, it can be shorter or longer, depending on the
        neuron.
        '''
        dendrite_axon_len = random.randint(19,61) # measured in micrometers
        def auto_position_status(self):  # initiated by hardware sensor
            print("Auto-position on Axon Initial Segment")
            return True

        # initialize the movement counters
        up_count = 0
        down_count = 0
        left_count = 0
        right_count = 0
        rotation_value = 0

        while True:
            if down_count == dendrite_axon_len:
                print("dendrite_axon_length:", dendrite_axon_len)
                print(auto_position_status(self))
                break

            # get user input in micrometers
            user_input = input("Enter a direction (Up, Down, Left, Right), or type 'Rotate' to rotate: ")

            # process user input
            if user_input == 'quit':
                break
            elif user_input == 'Up':
                up_count += 1
            elif user_input == 'Down':
                down_count += 1
            elif user_input == 'Left':
                left_count += 1
            elif user_input == 'Right':
                right_count += 1
            elif user_input == 'Rotate':

                def rotate() -> float:
                    trigValue = input("Enter θ")
                    while not trigValue.isdigit():
                        trigValue = input("Invalid input. Please enter theta, a numerical angle value")
                    theta = np.radians(float(trigValue))
                    c, s = np.cos(theta), np.sin(theta)
                    rotationValue = np.array(((c, -s), (s, c)))
                    print(f"Theta is: {trigValue} Rotation Value is: {rotationValue}")
                    return rotationValue

                rotation_value = rotate()
                rotation_value += 1
            else:
                print(
                    "Invalid input. Please enter a valid direction (Up, Down, Left, Right) or type 'Rotate' to rotate.")
                continue

        # print the final movement counts
        print(f"Total movements: Up - {up_count}, Down - {down_count}, Left - {left_count}, Right - {right_count}, "
              f"Rotate - {rotation_value}")
        return up_count, down_count,left_count,right_count,rotation_value


    def reactivity_status(self):
        '''
        Ion-selective field-effect transistors (ISFETs), a bionanosensor electrochemical
        transducer that can detect ionic current or the flow of ions. ISFETs would detect action potentials along the
        axon. # signal from nanoantenna via ISFET nano sensor hardware
        '''

        print("monitors the action potentials and the structural changes initiated by the action-potential-based "
              "functional data.")
        if intrinsic_voltage < -55:
            print("Resting Potential active")
        if intrinsic_voltage == -55:
            print("Action Potential initiated")
        if received_signal >= 1 and received_signal <= 10: # MHz frequency
            print("recieved_signal is of range 10-100 nanobot needs replacement")
            print("sensing for incoming signal power to detect damaged nanobot sensors..")
            '''
            The protocol for regularly updating the number of synaptobots in the brain 
            (due to nanorobot damage(malfunctioning
            software/hardware), synapse elimination, neuron death, new synaptic formation, etc.) would be initiated by 
            endoneurobots
            '''
            def nanobotreplacement(self): #iniated by hardware sensor
                '''
                reflect or reveal the specific characteristics of a radio signal being received from a
                nanobot transmitter (or any transmitter in general).
                r(t) = A_c * (1 + m * s(t)) * cos(2*pi*f_c t + φ)
                r(t) represents the received signal at time t
                '''
                pi = math.pi
                A_c = 1  # The amplitude of the carrier signal, in volts.
                m = 2  # The modulation index, dimensionless
                s_t = 0.1  # The message signal, in volts.
                f_c = 1000  # frequency in hertz
                t = 10 # seconds
                φ = 0  # radians
                r_t = A_c * (1 + m * s_t) * math.cos(2 * pi * f_c * t + φ)
                print("Amplitude Modulation :", r_t)
                return r_t

            print(nanobotreplacement(self))







