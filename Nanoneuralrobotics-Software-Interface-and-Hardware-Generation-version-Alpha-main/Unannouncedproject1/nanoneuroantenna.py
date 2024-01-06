'''
To utilize signal reception for achieving behaviors such as movement or payload delivery from a nanobot, the electronic
 device needs to interpret and process the received signals appropriately. Here are a few ways an electronic device can
 leverage signal reception phenomena:

1. Signal Strength: The device can measure the received signal strength to determine the proximity of the signal source.
By monitoring changes in signal strength, the device can infer the relative position or distance between the nanobot and
 the signal source. This information can be used to control the movement of the nanobot or trigger specific actions.

2. Signal Modulation: The device can analyze the modulation characteristics of the received signal, such as amplitude,
frequency, or phase modulation. Different modulation schemes can be used to encode specific instructions or commands
for the nanobot. By decoding and interpreting the modulated signal, the device can extract instructions related to
movement, payload delivery, or other desired behaviors.

3. Signal Encoding: The device can employ specific encoding techniques, such as digital modulation or spread spectrum
techniques, to embed information within the received signal. This encoded information can contain instructions or data
for the nanobot, specifying desired behaviors or actions. The device can decode the encoded information and act accordingly.

4. Signal Timing: The device can analyze the timing characteristics of the received signal, such as signal arrival
time or time intervals between signal events. By monitoring these timing parameters, the device can synchronize its
actions with the nanobot or coordinate multiple nanobots for collective behaviors. Precise timing information can be
utilized to trigger payload delivery or coordinate movement patterns.

5. Signal Analysis: The device can apply signal processing algorithms, such as filtering, pattern recognition, or
machine learning techniques, to analyze the received signals. By extracting relevant features or patterns from the
signal, the device can identify specific commands or instructions related to movement, payload delivery, or other
behaviors. This enables the device to make informed decisions and control the nanobot accordingly.

In summary, by leveraging various phenomena of signal reception, an electronic device can extract information,
decode instructions, and make decisions related to the desired behaviors of nanobots. Through signal strength,
modulation, encoding, timing analysis, and signal processing techniques, the device can interpret the received
signals and initiate actions such as movement or payload delivery, enabling precise control and coordination of
nanobots for specific applications.
'''


import math
import numpy as np
import random
from abc import ABC, abstractmethod
class Antenna:
    on_off = False
    sense = []
    def __init__(self, on_off, sense):
        self.on_off = on_off
        self.sense = sense

    # Polymorphism
    def reactivity_status(self):
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
        t = 10  # seconds
        φ = 0  # radians
        r_t = A_c * (1 + m * s_t) * math.cos(2 * pi * f_c * t + φ)
        print("Amplitude Modulation :", r_t)
        return r_t

    def required_receiver_voltage(self):
        import math
        ########################
        # Voltage for function #
        ########################
        # voltage induced in the receiving antenna and the voltage applied to the transmitting antenna can# be described by the following equations: =>
        # For the receiving antenna: Vr = E * A * cos(theta) * exp(-j * k * r) / (r * sqrt(Lr * Cr))
        # For the transmitting antenna: Vt = Et * At * cos(theta) * exp(-j * k * r) / (r * sqrt(Lt * Ct))
        # Vr is Voltage measured in volts


        pi = math.pi
        E = 10  # is the incident electric field strength measured in volts per meter
        A = 0.2  # Effective aperture area measured in square meters
        theta = pi / 4  # angle measured in radians
        λ = 0.5  # wavelength measured in meters, k's dependency
        k = 2 * pi / λ  # wave number radians per meter
        r = 10  # distance measured in meters
        Lr = 1  # inductance measured in microhenry
        Cr = 100  # capacitance measured in picofarads

        def Vr(E, A, theta, k, r, Lr, Cr):
            cos_theta = math.cos(theta)
            Vr = np.real(E * A * cos_theta * np.exp(-1j * k * r) / (r * math.sqrt(Lr * Cr)))
            return Vr

        Vr = Vr(E, A, theta, k, r, Lr, Cr)
        print("Voltage Required for Recieving Antenna:", Vr)

    def required_transmitter_voltage(self):
        import math
        # Vt is Voltage measured in volts
        Et = 1 # Incident electric field strength measured in volts per meter
        At = 0.5 # Effective aperture area of the transmitting antenna
        pi = math.pi
        theta = pi/4 # angle measured in radians
        k = 2*pi*10**6 # wave number measured in radians per meter
        r = 10 # distance measured in meters
        Lt = 1*math.exp(-6) # Inductance of the transmitting antenna measured in henries
        Ct = 1*math.exp(-9) # Capacitance of the transmitting antenna measured in farads
        Vt = Et * At * math.cos(theta) * np.exp(-1j * k * r) / (r * math.sqrt(Lt * Ct))
        print("Voltage Required for Transmitting Antenna:", Vt)

        ####################################################################################
        # receiver logic =>  # the equation for power transfer in a bistatic radar system can be determined using the concept
        # of Radar Cross Section (RCS) and the Friis formula. The equation for power received (Prec) in a bistatic radar
        # system can be written as: Prec = Pinc * σ * (Gt * Gr * λ^2) / ( (4 * π)^2 * R^4 )
        # Where:
        # - Prec is the received power at the receiver measured in Watts (W)
        # P_inc = 10 # - Pinc is the incident power density from the transmitter measured in Watts per square meter (W/m^2)
        # σ = 2 # - σ is the Radar Cross Section (RCS) of the target measured in Square meters (m^2)
        # Gt = 5 # - Gt is the gain of the transmitting antenna. no units - dimensionless
        # Gr = 8 # - Gr is the gain of the receiving antenna. no units - dimensionless
        # λ = 0.1 # - λ is the wavelength of the electromagnetic wave measured in meters.
        # R = 1000 # - R is the distance between the target and the receiver measured in meters.
        ###################################################################################################################
        # transmitter logic => identical to receiver logic
        ##################################################

        ########################################################################################################################
        # actual power transfer in a radar system can be influenced by various factors, such as losses in the transmission line,
        # and environmental conditions
        ########################################################################################################################
        # The equation for attenuation in a lossy transmission line can be represented as follows: Attenuation (dB) = α * L
        # Attenuation (dB) = α * L
        a = 10 # attenuation coefficient, which represents the rate of signal power loss per unit length of the transmission
        # line.
        # It is measured in decibels per unit length (dB/m) or decibels per unit distance (dB/km).
        L = 10 # L is the length of the transmission line over which the attenuation is measured, usually given in meters (m)
        # or kilometers (km).
        Attenuation = a * L
        ###################
        # a mathematical equation that creates or combines equations to describe the radiation pattern equation through
        # stratified media - stratified media is an object the obstructs electromagnetic waves - can be considered an
        # environmental factor
        # => E_theta_phi = ∑[n=1 to N] A_n * exp(i * k_n * r) * sin(k_n * z) * cos(n * phi)
        # ∑[n=1 to N] => for n in range(N)
        E_theta_phi = 0  # Initialize the electric field - E_theta_phi is the electric field at the observation point,
        # in volts per meter
        A = [1.5, 2.0, 0.8, 1.2, 0.5] # A_n is amplitude measured in volts per meter
        imaginary = 1j# imaginary is the imaginary number sqrt(-1)
        k = [0.1, 0.2, 0.3, 0.4, 0.5] # k_n is the wave number in the nth layer, in radians per meter
        r = 10.0 # r is the distance from the source to the observation point, in meters
        z = 5.0 # z is the height of the observation point, in meters
        N = 5 # N is iteration of the summation
        phi = random.choice([0, pi/6, pi/4, pi/3, pi/2, pi, 2*pi]) # measured in radians
        ##################################################################################################################
        # Compute the far field to calculate the electric field strength at the antenna and power density  - heat build up
        ##################################################################################################################
        # far field => E_r = E_0 * r^-1 * sin(kr) * cos(theta) && H_r = E_0 * r^-1 * sin(kr) * sin(theta)
        #################################################################################################
        # Where:
        # E_r is the electric field strength in the radial direction # measured in volts per meter
        # H_r is the magnetic field strength in the radial direction # measured in amperes per meter
        # E_0 is the electric field strength at the antenna # measured in volts per meter
        # r is the distance from the antenna # measured in meters
        # k is the wavenumber # measured in radians per meter
        # theta is the angle between the radial direction and the direction of propagation
        ##################################################################################################
        # power density - heat build up in device:
        import math
    def calculate_power_density(self, E_0, r, k, theta):
        # r = 10.0  # Distance from the antenna (in meters)
        # k = 2.0  # Wavenumber (in radians per meter)
        # theta = math.pi / 4  # Angle between radial direction and propagation direction (in radians)
        # E_0 = 10  # the electric field strength at the antenna measured in volts per meter
        E_r = E_0 * (r**-1) * math.sin(k*r) * math.cos(theta)
        H_r = E_0 * (r**-1) * math.sin(k*r) * math.sin(theta)
        power_density = 0.5 * (E_r * H_r.conjugate()).real
        print("Power Density:", power_density)
        return power_density

    # r = 10.0  # Distance from the antenna (in meters)
    # k = 2.0  # Wavenumber (in radians per meter)
    # theta = math.pi / 4  # Angle between radial direction and propagation direction (in radians)
    # E_0 = 10  # the electric field strength at the antenna measured in volts per meter
    # result = calculate_power_density(E_0, r, k, theta)
    # print("Power Density:", result)
        #################################################################################################