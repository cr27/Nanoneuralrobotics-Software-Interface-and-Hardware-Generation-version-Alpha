'''
Active Propulsion: The nanobot may have its own propulsion system, such as tiny motors or flagella-like structures,
enabling it to actively navigate through the bloodstream and reach the target neuron.  This could involve swimming or
crawling motions propelled by chemical reactions or other energy sources.

he manipulation and transmission of neural signals by nanodevices can involve various techniques depending on the
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



Gliabots are glia-resident autonomous neuralnanorobots that are endowed with the capacity
to monitor human–brain glial cells and may further serve as supportive infrastructure elements of the system.

Similarly, a 10 μm3 volume of gliabots (Figure 4) would egress the bloodstream, enter their respective glial cells,
and position themselves intracellularly at the most appropriate intra-glial region

Facilitated and mediated by endoneurobots and gliabots, the synaptobots would subsequently transmit 5.52 × 1016
bits/sec of continuous action potential data (Martins et al., 2012) via an in vivo nanofiber-optic network system,
as described above (Freitas, 1999b).

Astrocytes are a type of glial cell that play a critical role in supporting neurons.
They provide nutrients to neurons, maintain the blood-brain barrier, recycle neurotransmitters,
and help support the overall structure of the nervous system.

Microglia are another type of glial cell that acts as the brain's immune system. They proliferate
in areas of brain damage and remove toxic materials, playing a vital role in protecting the brain from harm.
One of the most important functions of glial cells is myelination, which increases the speed of
propagation of an action potential. Glia cells form insulating sheaths around some axons, with small gaps
(Nodes of Ranvier) in between sheaths. Oligodendrocytes myelinate cells in the central nervous system
(brain and spinal cord), while Schwann cells myelinate cells in the peripheral nervous system.

Ependymal cells are another type of glial cell that line the ventricles of the brain and secrete cerebrospinal fluid.
They also beat cilia to circulate fluid, helping to maintain a healthy environment for neurons.
Radial glia are a type of glial cell that guide the migration and growth of neurons during development. Without these
cells, the nervous system would not develop properly.

'''
from nanoneuroantenna import Antenna
from abc import ABC, abstractmethod
import numpy as np
import math
import random

received_signal = random.uniform(10, 100)  # measured in MHz
class Gliabot(Antenna): # Inheriting functions from Antenna parent class
    neurotransmitter_cargo_amount = 0
    def __init__(self, on_off, sense, neurotransmitter_cargo_amount):
        super().__init__(on_off, sense)
        self.required_receiver_voltage()  # Invoke Inheritance
        self.required_transmitter_voltage()  # Invoke Inheritance
        r = 10.0  # Distance from the antenna (in meters)
        k = 2.0  # Wavenumber (in radians per meter)
        theta = math.pi / 4  # Angle between radial direction and propagation direction (in radians)
        E_0 = 10  # the electric field strength at the antenna measured in volts per meter
        self.calculate_power_density(E_0, r, k, theta)  # important for heat buildup - Invoke Inheritance
        self.payload_excit_delivery = {'Glutamate': neurotransmitter_cargo_amount}
        self.payload_inhib_delivery = {'GABA': neurotransmitter_cargo_amount}
        self.excit_reuptake = {"Glutamate": neurotransmitter_cargo_amount}
        self.inhib_reuptake = {"GABA": neurotransmitter_cargo_amount}
        self.neurotransmitter_cargo_amount = neurotransmitter_cargo_amount



    @abstractmethod  # Abstraction
    def movement(self):

        def auto_position_status(self):
            print("Auto-positioned on axon segment")
            return True


        up_count = 0
        down_count = 0
        left_count = 0
        right_count = 0
        rotation_value = 0
        '''
        For a typical cortical neuron, the axon diameter is about 1 micrometer. If the gliabots need to be positioned 
        within 1 micrometer of each other, then the distance interval would be 1 micrometer. However, if the gliabots 
        only need to be positioned within 10 micrometers of each other, then the distance interval could be 10 
        micrometers.
        '''
        axon_distance = 0 # keep track of distance traversed on axon to auto-position measured in  micrometers


        while True:
            if up_count == 10 or down_count == 10:
                axon_distance = 10
                print("Axon DIstance:", axon_distance)
                print(auto_position_status(self))
                break

            # get user input in micrometers
            user_input = input("Enter a direction (Up, Down, Left, Right), or type 'Rotate' to rotate: ")

            # process user input, movement calculated on super/quantum computer per micrometer for gliabot
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

    def reactivity_status(self):
        # signal from nanoantenna via chemicalnanobiosensors - nano sensor hardware
        if self.payload_excit_delivery['Glutamate'] >= 1:
            print("Neurotransmitter cargo full")
            release = input("Release excitatory neurotransmitter? (yes/no): ")
        if release.lower() == "yes":
            print("Excitatory neurotransmitter released.")
            self.payload_excit_delivery['Glutamate'] -= 1
        else:
            print("Excitatory neurotransmitter not released.")

        if self.payload_inhib_delivery['GABA'] >= 1:
            print("Neurotransmitter cargo full")
            release = input("Release inhibitory neurotransmitter? (yes/no): ")
            if release.lower() == "yes":
                print("Inhibitory neurotransmitter released.")
                self.payload_inhib_delivery['GABA'] -= 1
            else:
                print("Inhibitory neurotransmitter not released.")

        if self.payload_excit_delivery['Glutamate'] == 0:
            print("Send Reuptake Signal to Nanobot")
            self.excit_reuptake['Glutamate'] += 1
            print("...Nanobot Excitatory Neurotransmitter debt is..",
                  abs(self.excit_reuptake['Glutamate'] - self.neurotransmitter_cargo_amount))

        if self.payload_inhib_delivery['GABA'] == 0:
            print("Send Reuptake Signal to Nanobot")
            self.inhib_reuptake['GABA'] += 1
            print("...Nanobot Inhibitory Neurotransmitter debt is..",
                  abs(self.inhib_reuptake['GABA'] - self.neurotransmitter_cargo_amount))

        if received_signal >= 10 and received_signal <= 100:  # MHz frequency

            def chemicalreplacementanddelivery_chemicalnanobiosensorsignal(self):
                '''
                reflect or reveal the specific characteristics of a radio signal being received from a
                nanobot transmitter (or any transmitter in general).
                r(t) = A_c * (1 + m * s(t)) * cos(2*pi*f_c t + φ)
                r(t) represents the received signal at time t
                '''
                pi = math.pi
                A_c = 1  # The amplitude of the carrier signal, in volts.
                m = 2  # The modulation index, dimensionless
                s_t = 0.1 # The message signal, in volts.
                f_c = 1000 # frequency in hertz
                t = 10 # seconds
                φ = 0 # radians
                r_t = A_c * (1 + m * s_t) * math.cos(2*pi*f_c*t + φ)
                print("Amplitude Modulation :", r_t)
                return r_t

            print(chemicalreplacement_chemicalnanobiosensorsignal(self))

