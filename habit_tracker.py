import json


class HabitTracker:
    def __init__(self, filename="habits.json"):
        self.filename = filename
        self.habits = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.habits, file, indent=4)

    def add_habit(self, habit_name, description="", frequency="daily"):
        if habit_name in self.habits:
            raise ValueError("Habit already exists")
        self.habits[habit_name] = {
            "description": description,
            "frequency": frequency,
            "completion_count": 0
        }
        self.save_data()

    def mark_completed(self, habit_name):
        if habit_name not in self.habits:
            raise ValueError("Habit not found")
        self.habits[habit_name]["completion_count"] += 1
        self.save_data()

    def view_progress(self, habit_name):
        if habit_name not in self.habits:
            raise ValueError("Habit not found")
        return self.habits[habit_name]["completion_count"]

    def remove_habit(self, habit_name):
        if habit_name not in self.habits:
            raise ValueError("Habit not found")
        del self.habits[habit_name]
        self.save_data()

    def reset_progress(self):
        for habit in self.habits:
            self.habits[habit]["completion_count"] = 0
        self.save_data()


def main():
    tracker = HabitTracker()

    while True:
        print("\nHabit Tracker")
        print("1. Add Habit")
        print("2. Mark Habit as Completed")
        print("3. View Progress")
        print("4. Remove Habit")
        print("5. Reset Progress")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter habit name: ")
            description = input("Enter description (optional): ")
            frequency = input("Enter frequency (daily/weekly): ")
            tracker.add_habit(name, description, frequency)
            print(f"Habit '{name}' added!")

        elif choice == '2':
            name = input("Enter habit name: ")
            tracker.mark_completed(name)
            print(f"Habit '{name}' marked as completed!")

        elif choice == '3':
            name = input("Enter habit name: ")
            progress = tracker.view_progress(name)
            print(f"Progress for '{name}': {progress}")

        elif choice == '4':
            name = input("Enter habit name: ")
            tracker.remove_habit(name)
            print(f"Habit '{name}' removed!")

        elif choice == '5':
            tracker.reset_progress()
            print("All progress has been reset.")

        elif choice == '6':
            print("Exiting the Habit Tracker.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
