# AT-Praktikum Aufgabe 2a – Vertical Velocity Controller

Implement a **PD** or **PID** controller for the Crazyflie's vertical velocity in Webots.

## Tasks

* Complete the implementation in `velocity_controller.py`.
* Tune the controller gains.
* Verify the controller response in simulation.

## Goal

Design and tune a controller that tracks a vertical velocity reference and generates an appropriate thrust command.

## Project Structure

* `crazyflie_cave.py` — Main Webots controller script that runs the simulation loop.
* `controllers/` — Flight-control pipeline and controller configuration.

  * `controller_config.py` — Controller gains and quadcopter parameters.
  * `controller_factory.py` — Creates the selected flight controller.
  * `flight_controller_interface.py` — Common flight-controller interface.
  * `cascaded_controller.py` — Contains the position, velocity, attitude, rate controllers, and the motor mixer.
  * `position_controller.py` — Converts position errors into velocity setpoints.
  * `velocity_controller.py` — Converts velocity errors into attitude and thrust commands.
  * `attitude_controller.py` — Converts attitude errors into body-rate setpoints.
  * `attitude_rate_controller.py` — Converts body-rate errors into torque commands.
  * `motor_mixer.py` — Converts thrust and torque commands into motor velocities.
* `trajectory_planner/` — Reference trajectory generation and tracking.
* `utils/` — Sensor, motor, and logging utilities.

Good luck!

# Development setup
Can be found here: `INSTALL.md`