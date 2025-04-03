import turtle
import matplotlib.pyplot as plt
import time as ttime
import tkinter as tk

class BouncingBallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bouncing Ball Simulation - Input Parameters")

        self.create_input_fields()
        self.create_options()
        self.create_buttons()

    def create_input_fields(self):
        self.labels = ["Gravity (m/s²):", "Time Step (s):", "Restitution (0-1):", "Air Resistance (0-0.1):"]
        self.default_values = ["9.8", "0.5", "0.9", "0.02"]
        self.entries = []

        for i, label in enumerate(self.labels):
            tk.Label(self.root, text=label, font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(self.root, font=("Arial", 12))
            entry.insert(0, self.default_values[i])
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries.append(entry)

    def create_options(self):
        tk.Label(self.root, text="Choose Method:", font=("Arial", 12)).grid(row=len(self.labels), column=0, padx=10, pady=5, sticky="w")
        
        self.method_var = tk.StringVar(value="RK2")
        rk2_radio = tk.Radiobutton(self.root, text="Runge-Kutta 2nd Order", variable=self.method_var, value="RK2", font=("Arial", 12))
        rk4_radio = tk.Radiobutton(self.root, text="Runge-Kutta 4th Order", variable=self.method_var, value="RK4", font=("Arial", 12))
        
        rk2_radio.grid(row=len(self.labels), column=1, padx=10, pady=2, sticky="w")
        rk4_radio.grid(row=len(self.labels)+1, column=1, padx=10, pady=2, sticky="w")

    def create_buttons(self):
        start_button = tk.Button(self.root, text="Start Simulation", font=("Arial", 12), command=self.start_simulation)
        start_button.grid(row=len(self.labels)+2, columnspan=2, pady=10)

    def start_simulation(self):
        values = [float(entry.get()) for entry in self.entries]
        method = self.method_var.get()
        self.root.destroy()
        run_simulation(*values, method)

def run_simulation(g, dt, restitution, air_resistance, method):
    initial_velocity = 0  
    window_height = 600  
    ground_y = -10  
    velocity_threshold = 0.002  
    ball_radius = 10  
    screen_width = 800  
    max_iterations = 5000  
    restitution_decay = 0.98  

    screen = turtle.Screen()
    screen.title(f"Bouncing Ball Simulation ({method})")
    screen.bgcolor("white")
    screen.setup(width=screen_width, height=window_height)

    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("red")
    ball.penup()

    ground = turtle.Turtle()
    ground.color("black")
    ground.penup()
    ground.goto(-screen_width//2, ground_y)
    ground.pendown()
    ground.goto(screen_width//2, ground_y)

    y_pos = 250  
    y_vel = initial_velocity
    ball.setposition(0, y_pos)

    time_list = [0]
    height_list = [y_pos]
    velocity_list = [y_vel]
    t = 0  

    def runge_kutta_2nd_order(v, y, g, air_resistance, dt):
        def dv_dt(v):
            return -g - air_resistance * v  

        k1_v = dt * dv_dt(v)
        k2_v = dt * dv_dt(v + 0.5 * k1_v)
        v_new = v + k2_v

        k1_y = dt * v
        k2_y = dt * (v + 0.5 * k1_v)
        y_new = y + k2_y
        
        return v_new, y_new

    def runge_kutta_4th_order(v, y, g, air_resistance, dt):
        def dv_dt(v):
            return -g - air_resistance * v  

        k1_v = dt * dv_dt(v)
        k2_v = dt * dv_dt(v + 0.5 * k1_v)
        k3_v = dt * dv_dt(v + 0.5 * k2_v)
        k4_v = dt * dv_dt(v + k3_v)
        v_new = v + (k1_v + 2*k2_v + 2*k3_v + k4_v) / 6

        k1_y = dt * v
        k2_y = dt * (v + 0.5 * k1_v)
        k3_y = dt * (v + 0.5 * k2_v)
        k4_y = dt * (v + k3_v)
        y_new = y + (k1_y + 2*k2_y + 2*k3_y + k4_y) / 6

        return v_new, y_new

    last_heights = []  

    for _ in range(max_iterations):
        collision = False

        if method == "RK2":
            y_vel, y_pos = runge_kutta_2nd_order(y_vel, y_pos, g, air_resistance, dt)
        else:
            y_vel, y_pos = runge_kutta_4th_order(y_vel, y_pos, g, air_resistance, dt)

        if y_pos - ball_radius <= ground_y:
            collision = True
            y_pos = ground_y + ball_radius  
            y_vel = -y_vel * restitution  
            restitution *= restitution_decay  

        ball.sety(y_pos)

        time_list.append(t)
        height_list.append(y_pos)
        velocity_list.append(y_vel)
        t += dt

        last_heights.append(y_pos)
        if len(last_heights) > 10:
            last_heights.pop(0)

        if abs(y_vel) < velocity_threshold and y_pos - ball_radius <= 10:
            print("Simulation stopped: Ball is stationary.")
            break  

        plt.clf()
        plt.subplot(2, 1, 1)
        plt.plot(time_list, height_list, label="Height (m)", color="blue")
        plt.title("Bouncing Ball Motion")
        plt.xlabel("Time (s)")
        plt.ylabel("Height (m)")
        plt.grid(True)
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(time_list, velocity_list, label="Velocity (m/s)", color="red")
        plt.xlabel("Time (s)")
        plt.ylabel("Velocity (m/s)")
        plt.grid(True)
        plt.legend()

        plt.tight_layout()
        plt.pause(0.005)

        turtle.update()
        ttime.sleep(0.01)

    plt.show()  
    turtle.done()

root = tk.Tk()
app = BouncingBallApp(root)
root.mainloop()