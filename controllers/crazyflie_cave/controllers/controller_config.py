# ============================================================
# CONTROLLER CONFIGURATION
# ============================================================

# =========================
# POSITION CONTROLLER
# =========================
POSITION_GAINS = {
    "Kp_x": 1.0,
    "Kp_y": 1.0,
    "Kp_z": 1.0,
    "Ki_x": 0.0,
    "Ki_y": 0.0,
    "deadband": 0.001,
    "vx_max": 0.3,
    "vy_max": 0.3,
    "vz_max": 0.5,
    "integral_limit": 0.02,
}

# =========================
# VELOCITY CONTROLLER
# =========================
VELOCITY_GAINS = {
    "Kp_xy": 0.5,
    "Kd_xy": 1.0,
    # Aufgabe 2a: Tune the height controller gains
    "Kp_z": 0.0,   
    "Ki_z": 0.0,   
    "Kd_z": 0.0,   
    "tau_d": 0.1,
}

# =========================
# ATTITUDE CONTROLLER
# =========================
ATTITUDE_GAINS = {
    "Kp_att_rp": 0.3,
    "Kp_yaw": 0.4,
}

# =========================
# ATTITUDE RATE CONTROLLER
# =========================
RATE_GAINS = {
    "Kp": 0.05,
    "Ki": 0.02,
    "Kd": 0.002,
}

# =========================
# QUADCOPTER PARAMETERS
# =========================
QUADCOPTER_PARAMS = {
    "F_hover": 0, # Aufgabe 2a: Force for hovering - compansating gravity [Newton]
    "max_tilt_deg": 10.0,
}
