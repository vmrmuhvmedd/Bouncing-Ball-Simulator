# Bouncing Ball Simulation

## Overview
This project simulates the motion of a bouncing ball under the influence of gravity, air resistance, and restitution using Runge-Kutta numerical methods.

## Features
- **Graphical Simulation**: Uses `turtle` for animation.
- **Numerical Methods**: Implements Runge-Kutta 2nd and 4th order methods for motion calculation.
- **Customizable Parameters**: Gravity, time step, restitution, and air resistance can be adjusted.
- **Real-time Graphing**: Uses `matplotlib` to plot height and velocity over time.

## Requirements
Make sure you have the following dependencies installed:

```sh
pip install matplotlib
```

## How to Run
### Clone the Repository
```sh
git clone https://github.com/yourusername/bouncing-ball-simulation.git
cd bouncing-ball-simulation
```

### Run the Simulation
```sh
python main.py
```

## Usage
1. A GUI will appear, prompting you to enter simulation parameters:
   - **Gravity** (m/s²)
   - **Time Step** (s)
   - **Restitution** (0-1)
   - **Air Resistance** (0-0.1)
2. Choose the numerical method:
   - **Runge-Kutta 2nd Order (RK2)**
   - **Runge-Kutta 4th Order (RK4)**
3. Click **Start Simulation**.
4. The bouncing ball animation will run, and real-time plots of height and velocity will be displayed.

## Files
- `main.py` - The main script that runs the simulation.
- `README.md` - Documentation for the project.

## License
This project is open-source and available under the **MIT License**.

## Contributions
Contributions are welcome! Feel free to fork the repository and submit pull requests.

