import random

class GoalBasedVacuumCleaner:
    def __init__(self, gs=3):
        self.grid_size = gs
        self.environment = []

        # Initialize environment with random states
        for _ in range(gs):
            row = [random.choice(["Clean", "Dirty", "Hurdle"]) for _ in range(gs)]
            self.environment.append(row)

        # Starting position
        self.position = [0, 0]
        if self.environment[0][0] == "Hurdle":
            self.environment[0][0] = "Clean"

        self.cleaned_rooms = 0
        self.dirty_rooms = sum(row.count("Dirty") for row in self.environment)

    def display_env(self):
        print("\n=== Environment State ===")
        for i in range(self.grid_size):
            row = ""
            for j in range(self.grid_size):
                if [i, j] == self.position:
                    row += "[A] "  # Agent’s position
                else:
                    row += f"[{self.environment[i][j][0]}] "
            print(row)

    def perceive(self):
        x, y = self.position
        return self.environment[x][y]

    def all_clean(self):
        for row in self.environment:
            for cell in row:
                if cell == "Dirty":
                    return False
        return True

    def rule(self, status):
        if status == "Dirty":
            return "Clean"
        elif self.all_clean():
            return "Stop"
        else:
            return "Move"

    def act(self, action):
        x, y = self.position

        if action == "Clean":
            print(f"Cleaning at {self.position}")
            self.environment[x][y] = "Clean"
            self.cleaned_rooms += 1

        elif action == "Move":
            # Try to move to a random adjacent clean cell (not hurdle)
            possible_moves = []
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.grid_size and 0 <= ny < self.grid_size:
                    if self.environment[nx][ny] != "Hurdle":
                        possible_moves.append([nx, ny])

            if possible_moves:
                self.position = random.choice(possible_moves)
                print(f"Moved to {self.position}")
            else:
                print("No available move — surrounded by hurdles!")

        elif action == "Stop":
            print("All rooms are clean. Stopping.")

    def start_cleaning(self):
        step = 0
        while not self.all_clean():
            print(f"\nStep {step + 1}:")
            self.display_env()

            status = self.perceive()
            action = self.rule(status)
            self.act(action)
            step += 1

        print("\nFinal Environment:")
        self.display_env()
        print(f"Cleaning completed in {step} steps with {self.cleaned_rooms} cleaned rooms.")


# Run the agent
agent = GoalBasedVacuumCleaner(gs=3)
agent.start_cleaning()
