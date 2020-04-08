import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, exp

# phi_H(t) = e^(-zeta * omega_n * t) * [C_1 * cos(omega_d * t) + C_2 * sin(omega_d * t)]
# phi_P(t) = Phi * sin(omega * t - theta)

omega_n = 10.54
omega_d = 10.3939
zeta = 0.1659

C_1 = -0.001317
C_2 = -0.1098

Phi = -0.009145
theta = 2.9971

omega = 28

t_steps = 1000
t_arr = np.linspace(0, 4, num=t_steps + 1, endpoint=True)

phi_H = lambda t: exp(-zeta * omega_n * t) * (C_1 * cos(omega_d * t) + C_2 * sin(omega_d * t))
phi_P = lambda t: Phi * sin(omega * t - theta)
phi = lambda t: phi_H(t) + phi_P(t)

phi_d = lambda t: -zeta * omega_n * exp(-zeta * omega_n * t) * (C_1 * cos(omega_d * t) + C_2 * sin(omega_d * t)) +\
                  exp(-zeta * omega_n * t) * (-C_1 * omega_d * sin(omega_d * t) + C_2 * omega_d * cos(omega_d * t)) +\
                  Phi * omega * cos(omega * t - theta)

phi_arr = np.array([phi(t_i) for t_i in t_arr])
phi_d_arr = np.array([phi_d(t_i) for t_i in t_arr])

plt.figure()

plt.subplot(211)

plt.title("Lengőkar szögkitérése ütközés és gerjesztés hatására")
plt.plot(t_arr, phi_arr, "r-")
plt.axis([0, 4, -0.1, 0.1])
plt.ylabel('Szögkitérés [rad]')
plt.xlabel('Ütközés után eltelt idő [s]')
plt.grid(color='black', linestyle='-', linewidth=0.5)

plt.subplot(212)

plt.title("Lengőkar szögsebessége ütközés és gerjesztés hatására")
plt.plot(t_arr, phi_d_arr, "b-")
plt.axis([0, 4, -1, 1])
plt.ylabel('Szögsebesség [rad/s]')
plt.xlabel('Ütközés után eltelt idő [s]')
plt.grid(color='black', linestyle='-', linewidth=0.5)

plt.tight_layout()
plt.savefig('grafikon.png', dpi=500)
plt.show()
