import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Parameters
xspace = 240
yspace = 180

# Physics function
def projectile_motion(v0, angle_deg):
    g = 9.81  # m/s^2
    angle = np.radians(angle_deg)
    t_flight = 2 * v0 * np.sin(angle) / g
    t = np.linspace(0, t_flight, num=300)
    x = v0 * np.cos(angle) * t
    y = v0 * np.sin(angle) * t - 0.5 * g * t**2
    return x, y

# Streamlit UI
st.title("Test: Projectile Motion Simulator")

v0 = st.slider("Initial velocity (m/s)", 1, 100, 50)
angle = st.slider("Launch angle (degrees)", 0, 90, 45)

x, y = projectile_motion(v0, angle)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlim([0,xspace])
ax.set_ylim([0,yspace])
ax.set_xlabel("Distance (m)")
ax.set_ylabel("Height (m)")
ax.set_title("Tata")
st.pyplot(fig)

st.markdown(f"**Flight time:** {2*v0*np.sin(np.radians(angle))/9.81:.2f} s")
st.markdown(f"**Range:** {v0**2*np.sin(2*np.radians(angle))/9.81:.2f} m")
