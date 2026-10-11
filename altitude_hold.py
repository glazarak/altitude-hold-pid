# altitude_hold.py - a pretend drone trying to hold 10 m

import matplotlib.pyplot as plt

m = 1.0         # mass, kg
g = 9.81        # gravity, m/s^2
target = 10.0   # where we want it, m
Kp = 2.0        # spring stiffness, N per m
Kd = 0.0        # damper, N per (m/s)

height = 0.0    # starting height, m
velocity = 0.0  # starting speed, m/s
dt = 0.01       # length of one tick, s

times = []
heights_nodamp = []
heights_damp = []

print("hover thrust needed:", m * g, "N")
print("starting at", height, "m, aiming for", target, "m")

for step in range(2000):              # 2000 ticks x 0.01 s = 20 seconds
    error = target - height
    thrust = m * g + Kp * error - Kd * velocity
    net_force = thrust - m * g
    acceleration = net_force / m
    velocity = velocity + acceleration * dt
    height = height + velocity * dt
    times.append(step * dt)
    heights_nodamp.append(height)

    if step % 100 == 0:               # every 100th tick = once a second
        print(round(step * dt, 1), "s   height", round(height, 2), "m")

height = 0.0            # back to the ground
velocity = 0.0          # and standing still
Kd = 1.5                # damper on for run 2

for step in range(2000):              # 2000 ticks x 0.01 s = 20 seconds
    error = target - height
    thrust = m * g + Kp * error - Kd * velocity
    net_force = thrust - m * g
    acceleration = net_force / m
    velocity = velocity + acceleration * dt
    height = height + velocity * dt
    heights_damp.append(height)

    if step % 100 == 0:               # every 100th tick = once a second
        print(round(step * dt, 1), "s   height", round(height, 2), "m")

plt.plot(times, heights_nodamp, label="no damping (Kd = 0)")
plt.plot(times, heights_damp, label="with damping (Kd = 1.5)")
plt.axhline(10, linestyle="--", color="gray", label="target")
plt.xlabel("time (s)")
plt.ylabel("height (m)")
plt.title("Altitude Hold Simulation")
plt.legend()
plt.savefig("plot.png")
plt.show()