def simulate_populations(years=20):
    rabbits = 50.0
    wolves = 0.0

    print(f"{'Year':<5}{'Rabbits':>12}{'Wolves':>12}")
    for year in range(1, years + 1):
        if year < 5:
            # Before wolves arrive: rabbits grow 10%
            rabbits *= 1.10

        elif year == 5:
            # Wolves introduced in year 5
            wolves = 10.0
            # Rabbits still grow, then suffer 1% predation loss
            rabbits *= 1.10
            rabbits *= 0.99

        else:
            # After year 5: both species grow/decline
            # Wolves grow 8%, then 6% die
            wolves *= 1.08
            wolves *= 0.94

            # Rabbits grow 10%, then 1% are eaten
            rabbits *= 1.10
            rabbits *= 0.99

        # Print current populations (rounded)
        print(f"{year:<5}{rabbits:12.1f}{wolves:12.1f}")


if __name__ == "__main__":
    simulate_populations()
