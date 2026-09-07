# import matplotlib.pyplot as plt
# import numpy as np

# from scipy import signal

# # drone properties
# m = 1.5
# g = 9.81
# b = 0.2 #air drag cooefficient damping

# # Transfer Function: G(s) = 1 / (ms^2 + bs)
# # Numerator coefficients: [1]
# # Denominator coefficients: [m, b, 0]
# num = [1]
# den = [m, b, 0]

# sys = signal.TransferFunction(num, den)

# # Simulate a Step Response (u = 1 unit of thrust)
# t, y = signal.step(sys)

# plt.plot(t, y)
# plt.title("Drone Altitude Step Response (No Gravity)")
# plt.xlabel("Time (s)")
# plt.ylabel("Altitude (z)")
# plt.grid()
# plt.show()



# import numpy as np
# from scipy.integrate import solve_ivp
# import matplotlib.pyplot as plt

# def drone_dynamics(t, state, m, b, g, u):
#     z, vz = state
    
#     # Differential Equations
#     dz_dt = vz
#     dvz_dt = (u - m*g - b*vz) / m
    
#     return [dz_dt, dvz_dt]

# # Simulation settings
# m, b, g = 1.5, 0.1, 9.81
# u = 16.0  # Thrust slightly higher than weight (1.5 * 9.81 = 14.71)
# t_span = (0, 10)  # 10 seconds
# initial_state = [10, 0] # Start at 10m altitude, 0 velocity

# # Solve
# sol = solve_ivp(drone_dynamics, t_span, initial_state, args=(m, b, g, u), t_eval=np.linspace(0, 10, 100))

# # Plotting
# plt.plot(sol.t, sol.y[0])
# plt.ylabel("Altitude (z)")
# plt.xlabel("Time (s)")
# plt.title("Drone Flight Simulation")
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import signal

# # 1. System Parameters
# m, b, g = 1.5, 0.2, 9.81

# # 2. Define Transfer Function G(s) = 1 / (ms^2 + bs)
# num = [1]
# den = [m, b, 0]
# tf_sys = signal.TransferFunction(num, den)

# # 3. Convert to State-Space (Continuous)
# ss_sys = tf_sys.to_ss()
# A, B, C, D = ss_sys.A, ss_sys.B, ss_sys.C, ss_sys.D

# # 4. Discretize for your simulation loop (e.g., 100Hz)
# dt = 0.01 
# sys_discrete = signal.cont2discrete((A, B, C, D), dt)
# Ad, Bd, Cd, Dd = sys_discrete[0:4]

# # 5. Simulation Loop (Testing the Implementation)
# steps = 500
# t = np.linspace(0, steps*dt, steps)
# z_pos = np.zeros(steps)
# curr_state = np.array([[0.0], [0.0]]) # [z, vz]

# for i in range(steps):
#     # u_eff: Your thrust minus gravity offset
#     # In a real drone, u must at least equal m*g to hover
#     u_control = 16.0 
#     u_eff = u_control - (m * g) 
    
#     # Update State: x[k+1] = Ad*x[k] + Bd*u[k]
#     curr_state = Ad @ curr_state + Bd * u_eff
    
#     # Extract position (z)
#     z_pos[i] = curr_state[0, 0]

# # Plotting
# plt.plot(t, z_pos)
# plt.axhline(y=0, color='r', linestyle='--')
# plt.title("Discrete-Time State-Space Simulation")
# plt.xlabel("Time (s)")
# plt.ylabel("Altitude (z)")
# plt.grid(True)
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import signal

# # --- System Parameters ---
# m = 3.0      # kg
# b = 0.5      # damping (air resistance)
# g = 9.81     # gravity
# dt = 0.01    # time step (100Hz)
# target_z = 10.0 # Goal: 10 meters

# # --- 1. Define State-Space ---
# A = np.array([[0, 1], 
#               [0, -b/m]])
# B = np.array([[0], 
#               [1/m]])
# C = np.array([[1, 0]])
# D = np.array([[0]])

# # Discretize the system
# sys_disc = signal.cont2discrete((A, B, C, D), dt)
# Ad, Bd = sys_disc[0], sys_disc[1]

# # --- 2. Controller Setup ---
# # --- Controller Gains ---
# K_p = 25.0  # Proportional: pushes drone toward target
# K_d = 15.0  # Derivative: slows drone down as it approaches (Damping)

# # --- 3. Simulation Loop ---
# steps = 1800
# t = np.linspace(0, steps*dt, steps)
# state = np.array([[0.0], [0.0]]) # Start at z=0, vz=0
# history = []

# # --- Inside the Simulation Loop ---
# for i in range(steps):
#     curr_z = state[0, 0]
#     curr_vz = state[1, 0] # This is the derivative of position
    
#     # 1. Position Error (P)
#     error_p = target_z - curr_z
    
#     # 2. Velocity Error (D) 
#     # Target velocity is 0 because we want to hover at the target height
#     error_d = 0 - curr_vz 
    
#     # 3. Total Control Input (PD + Feed-forward Gravity)
#     u = (K_p * error_p) + (K_d * error_d) + (m * g)
    
#     # Physics Update
#     # Net force is (u - mg)
#     state = Ad @ state + Bd * (u - m * g)
    
#     history.append(curr_z)

# # --- 4. Plotting ---
# plt.figure(figsize=(10, 5))
# plt.plot(t, history, label='Drone Altitude', color='teal', linewidth=2)
# plt.axhline(y=target_z, color='r', linestyle='--', label='Target (10m)')
# plt.title("Phase 3: Closed-Loop Proportional Control Step Response")
# plt.xlabel("Time (seconds)")
# plt.ylabel("Altitude (meters)")
# plt.legend()
# plt.grid(True)
# plt.show()


""" 
problem statement : quadrotor control to a fixed altitude above ground , using the transfer fns and state space reprenstation 
and as a controller use p and then advance to d and i controllers
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# --- System Parameters ---
# diff eqn of the system : m*z'' + b*z' - u + m*g = 0

m = 3.0
g = 9.81 
z = 10
b = 0.5

# state matrices
A = np.array([[0, 1],
            [0, -b/m]])
B = np.array([0, 1/m])
C = np.array([1, 0])
D = np.array([0])

# controller
K_p = 20



