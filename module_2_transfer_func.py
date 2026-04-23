import numpy as np
import matplotlib.pyplot as plt
import control as ct

# Physical parameters of the robotic joint
J = 2.0  # Inertia (kg*m^2)
b = 0.5  # Viscous friction (N*m*s)

# Define the Transfer Function: G(s) = 1 / (J*s^2 + b*s)
numerator = [1]
denominator = [J, b, 0] # Represents 2*s^2 + 0.5*s + 0
plant_tf = ct.TransferFunction(numerator, denominator)

print("Plant Transfer Function:")
print(plant_tf)

# Simulate applying 1 Nm of torque suddenly (Step Response)
time, response = ct.step_response(plant_tf)

plt.figure(figsize=(8, 4))
plt.plot(time, response, 'b', linewidth=2)
plt.title('Open-Loop Step Response of Robotic Joint')
plt.xlabel('Time [s]')
plt.ylabel('Joint Angle $y(t)$ [rad]')
plt.grid(True)
plt.show()