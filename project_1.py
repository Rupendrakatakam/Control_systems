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


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 1. System Parameters
m, b, g = 1.5, 0.2, 9.81

# 2. Define Transfer Function G(s) = 1 / (ms^2 + bs)
num = [1]
den = [m, b, 0]
tf_sys = signal.TransferFunction(num, den)

# 3. Convert to State-Space (Continuous)
ss_sys = tf_sys.to_ss()
A, B, C, D = ss_sys.A, ss_sys.B, ss_sys.C, ss_sys.D

# 4. Discretize for your simulation loop (e.g., 100Hz)
dt = 0.01 
sys_discrete = signal.cont2discrete((A, B, C, D), dt)
Ad, Bd, Cd, Dd = sys_discrete[0:4]

# 5. Simulation Loop (Testing the Implementation)
steps = 500
t = np.linspace(0, steps*dt, steps)
z_pos = np.zeros(steps)
curr_state = np.array([[0.0], [0.0]]) # [z, vz]

for i in range(steps):
    # u_eff: Your thrust minus gravity offset
    # In a real drone, u must at least equal m*g to hover
    u_control = 16.0 
    u_eff = u_control - (m * g) 
    
    # Update State: x[k+1] = Ad*x[k] + Bd*u[k]
    curr_state = Ad @ curr_state + Bd * u_eff
    
    # Extract position (z)
    z_pos[i] = curr_state[0, 0]

# Plotting
plt.plot(t, z_pos)
plt.axhline(y=0, color='r', linestyle='--')
plt.title("Discrete-Time State-Space Simulation")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (z)")
plt.grid(True)
plt.show()