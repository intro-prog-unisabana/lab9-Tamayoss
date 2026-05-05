from aircraft import Aircraft

def main():
    model = input("Enter aircraft model:\n")
    plane = Aircraft(model)

    while True:
        command = input("Enter command (A for ascent, D for descent, X to exit):\n").strip()
        if command.upper() == "X":
            break
        parts = command.split()
        if len(parts) == 2:
            action, value = parts[0].upper(), int(parts[1])
            if action == "A":
                plane.climb(value)   # aquí usamos climb
            elif action == "D":
                plane.descend(value)

    print(f"Final altitude: {plane.altitude} feet")

if __name__ == "__main__":
    main()
