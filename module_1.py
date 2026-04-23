import numpy as np
import matplotlib.pyplot as plt

# Time setup
t = np.linspace(0, 10, 500)
dt = t[1] - t[0]

# Reference (Target Altitude = 10m)
r = np.ones_like(t) * 10.0

# System states
y_open = np.zeros_like(t)
y_closed = np.zeros_like(t)

# Controller gains (simplified mapping of error to input)
K_open = 1.0  
K_closed = 0.1

for i in range(1, len(t)):
    # Unmodeled disturbance: a severe downdraft starts at t=4s
    disturbance = -5.0 if t[i] > 4.0 else 0.0

    # OPEN LOOP: Input u(t) is pre-computed based on reference only. Blind to reality.
    u_open = K_open * r[i]
    # Plant dynamics integration: next_state = current_state + (input + disturbance) * dt
    y_open[i] = y_open[i-1] + (u_open - y_open[i-1] + disturbance) * dt

    # CLOSED LOOP: Input u(t) is based on ERROR.
    e = r[i] - y_closed[i-1]
    u_closed = K_closed * e
    # Plant dynamics integration
    y_closed[i] = y_closed[i-1] + (u_closed - y_closed[i-1] + disturbance) * dt

plt.figure(figsize=(10, 5))
plt.plot(t, r, 'k--', label='Reference $r(t)$')
plt.plot(t, y_open, 'r', label='Open-Loop Output')
plt.plot(t, y_closed, 'g', label='Closed-Loop Output')
plt.axvline(4.0, color='gray', linestyle=':', label='Disturbance hits')
plt.xlabel('Time [s]')
plt.ylabel('Altitude [m]')
plt.title('Drone Altitude: Open vs Closed Loop under Disturbance')
plt.legend()
plt.grid(True)
plt.show()