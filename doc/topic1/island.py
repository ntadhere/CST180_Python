import math

def simulate_populations(years=20):
    rabbits = 50.0
    wolves = 0.0

    print(f"{'Year':<5}{'Rabbits':>12}{'Wolves':>12}")
    for year in range(1, years + 1):
        if year < 5:
            # Only rabbits grow
            rabbits *= 1.10
        elif year == 5:
            # Introduce wolves
            wolves = 10
            rabbits *= 1.10
            rabbits *= 0.99
        else:
            # After year 5 both species change
            wolves *= 1.08
            wolves *= 0.94
            rabbits *= 1.10
            rabbits *= 0.99

        # Floor before display
        rabbits_disp = math.floor(rabbits)
        wolves_disp   = math.floor(wolves)

        print(f"{year:<5}{rabbits_disp:12}{wolves_disp:12}")

if __name__ == "__main__":
    simulate_populations()
