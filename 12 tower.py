def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    # Move the nth disk to destination
    print(f"Move disk {n} from {source} to {destination}")
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)

# Main Program
try:
    num_disks = int(input("Enter number of disks: "))
    print("\nSteps to solve Tower of Hanoi:")
    tower_of_hanoi(num_disks, 'A', 'B', 'C')  # A: source, B: auxiliary, C: destination
except ValueError:
    print("Please enter a valid integer.")
