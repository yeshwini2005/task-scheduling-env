from models import TaskSchedulingEnv, Action

def main():
    env = TaskSchedulingEnv()
    obs = env.reset()

    sorted_indices = sorted(
        range(len(obs.tasks)),
        key=lambda i: (-obs.tasks[i]["priority"], obs.tasks[i]["deadline"])
    )

    action = Action(order=sorted_indices)
    _, reward, _, _ = env.step(action)

    print("Reward:", reward)

if __name__ == "__main__":
    main()