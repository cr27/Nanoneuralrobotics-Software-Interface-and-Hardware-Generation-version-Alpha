'''
About 1 trillion auxiliary transport nanorobots may suffice to accommodate the workload of dynamically adjusting the
physical deployment of synaptobots. Auxiliary transport nanorobots (∼2.5 μm) would adhere to a similar transit protocol
for crossing the BBB and traversing the neuropil as the endoneurobots and gliabots, which are of comparable size
(∼2.2 μm).


Once arrived at the neurons, the auxiliary transport nanorobots would release their cargo of 24 synaptobots into the
cytoplasms of each neuron. Following deployment, each synaptobot would either remain within the neuron soma, or navigate
(utilizing its onboard locomotion system) from the neuron soma along the axon or dendrite into pre-synaptic or
post-synaptic structures — the sites at which synaptic monitoring would occur.

The auxiliary nanofiber-optic system (Figure 6), coupled with endoneurobot and gliabot data transmission support,
would likely serve to minimize the onboard data storage requirements for synaptobots.
nanorobotic auxiliary 30 cm3 volume nanoscale fiber-optic system that is capable of handling ∼1018 bits/sec.

This may permit real-time brain-state monitoring and data extraction into an external supercomputer that communicates
directly with the cloud.

fiber optic cables will be stored within nanobots and released or unraveled when certain criteria are met
'''
import random
import math
from nanoneuroantenna import Antenna
received_Signal_nanofiberopticcargo =  random.uniform(100,1000) # measured in MHz
received_signal_synaptobotcargo = random.uniform(1000, 10000)  # measured in MHz
volume_brain =1500 # measured in cm^3
volume_auxiliary_nanofiberopticsystem = 30 # volume of total fiber optic bundles measured in cm^3
# total fiber optic bundles required for human brain
total_nanofiberopticcargo = volume_brain/volume_auxiliary_nanofiberopticsystem # 50  expected
nanofiberopticcargo = 1  # fiber bundle per aux nanobot

class Auxiliary_transport_nanorobot(Antenna):
    synaptobotcargo = 24  # synaptobot per aux nanobot
    def __init__(self, on_off, sense, synaptobotcargo):
        super().__init__(on_off, sense)
        self.required_receiver_voltage()  # Invoke Inheritance
        self.required_transmitter_voltage()  # Invoke Inheritance
        r = 10.0  # Distance from the antenna (in meters)
        k = 2.0  # Wavenumber (in radians per meter)
        theta = math.pi / 4  # Angle between radial direction and propagation direction (in radians)
        E_0 = 10  # the electric field strength at the antenna measured in volts per meter
        self.calculate_power_density(E_0, r, k, theta)  # important for heat buildup - Invoke Inheritance
        self.synaptobotcargo = synaptobotcargo  # synaptobot per aux nanobot
        datahandlingcapacity_auxiliary_nanofiberopticsystem = 1018 # measured in bits/sec

    @abstractmethod  # Abstraction
    def movement(self):
        # initialize the movement counters
        up_count = 0
        down_count = 0
        left_count = 0
        right_count = 0
        rotation_value = 0

        while True:
            # get user input
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
        return up_count, down_count, left_count, right_count, rotation_value

    def reactivity_status(self):
        # unload nanofiberotpic cargo
        if received_Signal_nanofiberopticcargo > 100  and received_Signal_nanofiberopticcargo < 1000:
            if nanofiberopticcargo == 1 and nanofiberopticcargo < total_nanofiberopticcargo:
                inputnanofiberopticcargo = input("release nanofiberopticcargo? Yes/No?")
                tolowercase_string = inputnanofiberopticcargo.lower()
                if tolowercase_string == 'yes':
                    for i in range(int(total_nanofiberopticcargo)):
                        print('nanofiberoptic cables are being released', 'cable:', i )

        # unload synaptobot cargo
        if received_signal_synaptobotcargo > 1000 and received_signal_synaptobotcargo < 10000:
            while self.synaptobotcargo >=1 and self.synaptobotcargo <= 24:
                    inputsynaptobotcargo = input("release synaptobotcargo? yes/no?")
                    tolowercase_string = inputsynaptobotcargo.lower()
                    if tolowercase_string == 'yes':
                        self.synaptobotcargo -= 1
                        print('synaptobotcargo remaining: ', self.synaptobotcargo)
                    else:
                        print('synaptobotcargo remaining: ', self.synaptobotcargo)
                        break


