class TrafficLightAgent:
    def __init__(self):
        pass

    def perceive(self):
        light = input("Enter the traffic light color (red, yellow, green or exit to stop the simulation): ")
        return light.strip().lower()

    def rule(self, light_color):
        if light_color == "red":
            return "Stop"
        elif light_color == "yellow":
            return "Slow down"
        elif light_color == "green":
            return "Go"
        else:
            return "Invalid input"

    def run(self):
        while True:
            light = self.perceive()
            if light == "exit":
                print("Stopping the simulation...")
                break
            action = self.rule(light)
            print(f"Action: {action}\n")
