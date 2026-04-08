from models import TaskSchedulingEnv, Action

# Create environment
env = TaskSchedulingEnv()

# Reset environment
obs = env.reset()

print("Tasks:")
for i, task in enumerate(obs.tasks):
    print(f"{i}: {task}")

# Simple baseline: sort by priority & deadline (same logic)
sorted_indices = sorted(
    range(len(obs.tasks)),
    key=lambda i: (-obs.tasks[i]["priority"], obs.tasks[i]["deadline"])
)

action = Action(order=sorted_indices)

# Take step
new_obs, reward, done, info = env.step(action)

print("\nPredicted Order:", sorted_indices)
print("Reward:", reward)