from interaction import InteractionManager

def main():
    interaction_manager = InteractionManager()

    # Number of iterations for the simulation
    num_iterations = 10

    for iteration in range(num_iterations):
        print(f"\nIteration {iteration + 1}")
        interaction_manager.run_interaction()

if __name__ == "__main__":
    main()