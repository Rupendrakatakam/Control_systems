import numpy as np
import matplotlib.pyplot as plt
import control as ct

# Physical parameters
J = 2.0  # Inertia
b = 0.5  # Friction

# State-Space Matrices
A = np.array([[0, 1],
              [0, -b/J]])
B = np.array([[0],
              [1/J]])
C = np.array([[1, 0]]) # We only measure position (x_1)
D = np.array([[0]])

# Create the State-Space system
sys_ss = ct.StateSpace(A, B, C, D)
print("State-Space System A Matrix:\n", sys_ss.A)

# Simulate Step Response (1 Nm torque)
time, response = ct.step_response(sys_ss)

plt.figure(figsize=(8, 4))
plt.plot(time, response, 'r', linewidth=2, label='Measured Position')
plt.title('State-Space Open-Loop Step Response')
plt.xlabel('Time [s]')
plt.ylabel('Position [rad]')
plt.grid(True)
plt.legend()
plt.show()