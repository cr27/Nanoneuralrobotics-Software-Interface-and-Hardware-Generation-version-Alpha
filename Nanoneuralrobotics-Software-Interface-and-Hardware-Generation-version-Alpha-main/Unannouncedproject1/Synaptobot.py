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


Synaptobots would be delivered via the brain microvasculature to avoid long-distance navigation within the brain
parenchyma. Auxiliary transport nanorobots having a volume of ∼20 μm3 (∼3.2 μm × 2.5 μm × 2.5 μm) might each convey
cargos of 24 synaptobots (total of ∼12 μm3) through the circulatory system and into the neuron soma. “The full
complement of synaptobots would be transported by a fleet of ∼1 trillion auxiliary transport nanorobots, which perform
∼10 round trips to complete the insertion of all synaptobots toward the implementation of the neuralnanorobotic system
prior to the activation of the B/CI system. Individual neurons, on average, would obtain ∼117 such shipments, for an
average overall distribution of 2800 synaptobots (≈2.42 × 1014 synapses/86 × 109 neurons), which would assign one
nanorobot per synapse”

Synaptobots are autonomous neuron-resident neuralnanorobots that might employ multiple flexible stalk-mounted nanosensors
to interface with each of the ∼2 × 1014 synapses of the human brain to directly monitor and interact with synaptically
processed and stored information.

Synaptobots would possess an independent propulsion system for traversing along the axons and dendrites in both
directions and may also exploit existing biological neuronal axonic or dendritic transport systems.
The process of locomotion may be biomimetically inspired by mitochondrial locomotion strategies within human neurons,
to minimize any physiological damage to neuronal processes. Alternatively,
oscillating piezo “fins” may operate in conjunction with a ovoid orifice to enable flow-through propulsion for
synaptobots

With one synaptobot positioned near each synapse in the human brain, the action potential data might be acquired
using ∼3375 nm3 FET-based neuroelectric nanosensors

An onboard synaptobot nanocomputer might be manifest as a ∼0.01 μm3 CPU device with ∼100 megaflops processing speed.
The total internal volume of onboard synaptobot computation might be 0.11 μm3 to fulfill redundancy requirements.
'''
from abc import ABC, abstractmethod
import numpy as np
from nanoneuroantenna import Antenna
import math
import random

received_signal = random.uniform(10, 100)  # measured in MHz
class Synaptobot(Antenna):
    neurotransmitter_cargo_amount = 0
    def __init__(self,on_off, sense, neurotransmitter_cargo_amount):
        super().__init__(on_off,sense)
        self.required_receiver_voltage()  # Invoke Inheritance
        self.required_transmitter_voltage()  # Invoke Inheritance
        r = 10.0  # Distance from the antenna (in meters)
        k = 2.0  # Wavenumber (in radians per meter)
        theta = math.pi / 4  # Angle between radial direction and propagation direction (in radians)
        E_0 = 10  # the electric field strength at the antenna measured in volts per meter
        self.calculate_power_density(E_0, r, k, theta)  # Invoke Inheritance
        self.payload_excit_delivery = {'Glutamate': neurotransmitter_cargo_amount}
        self.payload_inhib_delivery = {'GABA': neurotransmitter_cargo_amount}
        self.excit_reuptake = {"Glutamate": neurotransmitter_cargo_amount}
        self.inhib_reuptake = {"GABA": neurotransmitter_cargo_amount}
        self.neurotransmitter_cargo_amount = neurotransmitter_cargo_amount

    @abstractmethod # Abstraction
    def movement(self, method_iterations):
        # method_iterations = 0
        synapse_len = 1
        if (method_iterations > 1 and synapse_len >= 20):
            return

            '''
            The average distance between a typical cortical pre-synapse and cortical post-synapse is about 20 nanometers 
            (0.02 micrometers). This is the distance between the pre-synaptic axon terminal and the post-synaptic 
            dendritic spine, where the neurotransmitters are released and received.
            '''
        def auto_position_status(self):
            print("Auto-positioned within proximity of synapse")
            return True

        up_count = 0
        down_count = 0
        left_count = 0
        right_count = 0
        rotation_value = 0
        '''
        axon len in mm => millimeters
        Pyramidal Neuron	20-100 mm
        Purkinje Cell	20-40 mm
        Stellate Cell	1-5 mm
        Basket Cell	1-5 mm
        
        # use Basket Cell len for simplicity
        '''
        axon_len = 1 #random.randint(0,6) # measured in millimeters
        axon_traversed = False  # True - axon traversed, False - axon not fully traversed

        while True:
            if up_count == axon_len or down_count == axon_len:
                axon_traversed = True
                print("Axon Traversed?", axon_traversed)

            # get user input - measured in millimeters second iteration measured in nanometers for synapse traversal
            user_input = input("Enter a direction (Up, Down, Left, Right), or type 'Rotate' to rotate: ")

            # process user input
            if user_input == 'quit':
                break
            elif user_input == 'Up':
                up_count += 1
                if (method_iterations == 1 and up_count == synapse_len):
                    print(auto_position_status(self))
                    break
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
        method_iterations += 1
        self.movement(method_iterations)

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
                  abs(self.excit_reuptake['Glutamate']-self.neurotransmitter_cargo_amount))

        if self.payload_inhib_delivery['GABA'] == 0:
            print("Send Reuptake Signal to Nanobot")
            self.inhib_reuptake['GABA'] += 1
            print("...Nanobot Inhibitory Neurotransmitter debt is..",
                  abs(self.inhib_reuptake['GABA']-self.neurotransmitter_cargo_amount))

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