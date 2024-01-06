"""
The Nano_Neuro_Interface is a supercomputer or quantum computer software interface that defines 4 classes of nanobots
1. Auxiliary Transport Nanobot
2. Gliabot
3. Synaptobot
4. Endoneurobot

The physical manifestations of the nanobots themselves do not possess high level software, the signals received from
these bots however, are considered in high level software when the nano_neuro_interface receiver receives the
electromagnetic signal in the form of photons, as such, there are 4 classes defined on the nano_neuro_interface for
categorical knowing of these signals in this OOP project

The network nodes, where the nanorobots communicate with, should ideally operate at a frequency range of 10 to
10,000 MHz (ten million to ten billion times per second), and optical switching could be even faster.
This means that passing the signal through the local nodes should not cause significant additional delays.
"""
# from Endoneurobot import Endoneurobot
# from Gliabot import Gliabot
# from Synaptobot import Synaptobot
# from Auxiliary_transport_nanorobot import Auxiliary_transport_nanorobot
from nanoneuroantenna import Antenna
from abc import ABC, abstractmethod

'''
Steering nanoparticles to selected brain regions may also be achieved using external magnetic fields (Li et al., 2018).
Neuralnanorobotics strategies involve the direct, comprehensive monitoring of the ∼86 × 109 neurons of the human brain, 
as well as its ∼2 × 1014 synapses and ∼84 × 109 glial cells. Three proposed classes of neuralnanorobots (endoneurobots, 
gliabots, and synaptobots) may employ ∼3375 nm3 FET-based neuroelectric nanosensors to detect and monitor virtually all 
individual action potentials and their waveforms. Neuralnanorobotic entities would transmit the nominal 
∼5 × 1016 bits/sec of synaptically processed electronic information, encoded in ∼4 × 1015 spikes/sec flowing 
within the entire living human brain, wirelessly via a nanorobotic auxiliary 30 cm3 volume nanoscale fiber-optic 
system that is capable of handling ∼1018 bits/sec. This may permit real-time brain-state monitoring and data 
extraction into an external supercomputer that communicates directly with the cloud.
'''

class MyAbstractClass(ABC):
    '''
    nano_ID logic:
    To ensure effective communication between these(~trillions of nanobots) nanorobots,
    each message packet needs to contain a sender identifier and a recipient identifier.


    Yes, the sender identifier and recipient identifier can be considered as unique identification numbers for
    each individual nanobot. These identification numbers help distinguish and address specific nanorobots within
    the network.By assigning a unique identifier to each nanobot, it becomes possible to direct messages to specific
    nanobots and ensure that they reach their intended recipients. The sender identifier allows the recipient nanobot to
    know who sent the message, while the recipient identifier helps in identifying the intended recipient of the
    message.

    '''
    # implementation also important for nanobots that need replacing
    nano_ID_identifier = ""
    nano_ID_recipient = ""

    status_endo = False
    status_glia = False
    def __init__(self, nano_ID_identifier,nano_ID_recepient):
        self.nano_ID_identifier = nano_ID_identifier;# "sender identifier"  fiber optic packets
        self.nano_ID_recipient = nano_ID_recepient  # "recipient identifier" fiber optic packets


    @abstractmethod # abstraction
    def movement(self): # Navigation of nanobot via sensors and molecular motors, using the cartesian coordinate x-y
        # logic for simplicity, however, a more sophisticated and realistic way of implementing this would be using the
        # x-y-z coordinate system
        pass

class inherit_abstract(MyAbstractClass):
    def __init__(self, nano_ID_identifier, nano_ID_recipient):
        super().__init__(nano_ID_identifier, nano_ID_recipient)

    def movement(self):
        pass

blah = inherit_abstract(0, 0)
blah.nano_ID_identifier = "0b111011100110101100101000000000"  # one trillion
blah.nano_ID_recipient = "0b10010001101000000011010100000000000000000"  # ten trillion
print("nano_ID_identifier:", blah.nano_ID_identifier)
print("nano_ID_recipient:", blah.nano_ID_recipient)


class non_abstract():
# ###############
# # Endoneurobot#
# ###############
#     # Has the endoneurobot been positioned at the Axon Initial Segment?
#     def auto_position_status(self): # polymorphism
#         endobot1 = Endoneurobot(True, ['ElectroChemical'], -70)
#         endostatus = endobot1.auto_position_status()
#         print(endostatus)
# nonabstract = non_abstract()
# nonabstract.auto_position_status()
#
# # Choose Whether ot not to initiate an Action Potential
# endobot2 = Endoneurobot(True, ['Optical'], -55)
# if endobot2.apply_voltage >= -55:
#     print("depolarization - action potential initiated")  # In theory bringing the threshold to -55 elicits A.P.
#
# # Monitoring Status of Neuron - Resting vs Depolarized
#     endobot2.reactivity_status()
#
# # Nanobot signal is on or off
#     Nanobot_signaling = endobot2.on_off
#     print(Nanobot_signaling)
#
# # Antenna sensor senses electromagnetic radiation
#     electromagnetic_radiation_type = endobot2.sense
#     print(electromagnetic_radiation_type)
#
# # Voltage being applied to Axon Initial Segment
#     AIS_Voltage = endobot2.apply_voltage
#     print(AIS_Voltage)
#
# #############
# # Synaptobot#
# #############
#     synaptobot1 = Synaptobot(True, ['ElectroChemical'],1)
#
#     # movement
#     synaptobot1.movement(0) # Keep method iterations 0
#
#     # Amt of N.T.
#     neurotransmitter_amt = synaptobot1.neurotransmitter_cargo_amount
#     print(neurotransmitter_amt)
#
#     # Payload Release/Reuptake
#     synaptobot1.reactivity_status()
#
#     # Nanobot signal is on or off
#     Nanobot_signaling = synaptobot1.on_off
#     print(Nanobot_signaling)
#
#     # Antenna sensor senses electromagnetic radiation
#     electromagnetic_radiation_type = synaptobot1.sense
#     print(electromagnetic_radiation_type)

# ###########
# # Gliabot #
# ###########
#     gliabot1 = Gliabot(True, ['ElectroChemical'],1)
#
#     # movement
#     gliabot1.movement()

#     # Amt of N.T.
#     neurotransmitter_amt = gliabot1.neurotransmitter_cargo_amount
#     print(neurotransmitter_amt)
#
#     # Payload Release/Reuptake
#     gliabot1.reactivity_status()
#
#     # Nanobot signal is on or off
#     Nanobot_signaling = gliabot1.on_off
#     print(Nanobot_signaling)
#
#     # Antenna sensor senses electromagnetic radiation
#     electromagnetic_radiation_type = gliabot1.sense
#     print(electromagnetic_radiation_type)

#################################
# Auxillary_transport_nanorobot #
#################################
#Synaptobot cargo must be <= 24
# nanofiberoptic cargo must be 1
#     auxtransbot1 = Auxiliary_transport_nanorobot(True, ['Optical'], 24)
#     auxtransbot1.reactivity_status()

#######
# SQL #
#######

    import SQL

    SQL.create_bionano_hardware_components()
    SQL.create_openflow_controller_hardware_components()

    retrieve_data = SQL

    retrieve_data.retrieval()
    retrieve_data.update()







