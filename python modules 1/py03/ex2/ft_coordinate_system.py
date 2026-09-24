import math


def get_player_pos():
    while True:
        try:
            line = input("Enter new coordinates as floats in format 'x,y,z': ")
            parts = [p.strip() for p in line.split(',')]

            if len(parts) != 3:
                print("Invalid syntax")
                continue

            coords = []
            for p in parts:
                try:
                    coords.append(float(p))
                except ValueError as e:
                    print(f"Error on parameter '{p}': {e}")
                    raise

            return tuple(coords)

        except (ValueError, IndexError):
            continue


def main():
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    p1 = get_player_pos()

    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")

    dist_center = math.sqrt(p1[0]**2 + p1[1]**2 + p1[2]**2)
    print(f"Distance to center: {round(dist_center, 4)}")

    print("Get a second set of coordinates")
    p2 = get_player_pos()

    dist_points = (math.sqrt((p2[0] - p1[0])**2 +
                   (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2))
    print(f"Distance between the 2 sets of "
          f"coordinates: {round(dist_points, 4)}")


if __name__ == "__main__":
    main()
