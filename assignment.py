class FlightProcess:
    def __init__(self, pid, process, start_time, priority):
        self.pid = pid
        self.process = process
        self.start_time = start_time
        self.priority = priority

def display_flight_table(flight_table):
    print("P_ID\tProcess\t\tStart Time (ms)\tPriority")
    print("=" * 45)
    for process in flight_table:
        print(f"{process.pid}\t{process.process}\t\t{process.start_time}\t\t{process.priority}")

def main():
    flight_table = [
        FlightProcess("P1", "VSCode", 100, "MID"),
        FlightProcess("P23", "Eclipse", 234, "MID"),
        FlightProcess("P93", "Chrome", 189, "High"),
        FlightProcess("P42", "JDK", 9, "High"),
        FlightProcess("P9", "CMD", 7, "High"),
        FlightProcess("P87", "NotePad", 23, "Low"),
    ]
    
    print("Flight Table Sorting Options:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")
    
    choice = int(input("Enter your sorting choice (1/2/3): "))
    
    if choice == 1:
        sorted_table = sorted(flight_table, key=lambda process: process.pid)
    elif choice == 2:
        sorted_table = sorted(flight_table, key=lambda process: process.start_time)
    elif choice == 3:
        sorted_table = sorted(flight_table, key=lambda process: process.priority)
    else:
        print("Invalid choice")
        return
    
    display_flight_table(sorted_table)

if __name__ == "__main__":
    main()
