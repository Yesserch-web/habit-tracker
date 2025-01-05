import unittest
import os
from habit_tracker import HabitTracker


class TestHabitTracker(unittest.TestCase):
    def setUp(self):
        """Set up a temporary habit tracker instance with a test file."""
        self.test_file = "test_habits.json"
        self.tracker = HabitTracker(filename=self.test_file)
        self.tracker.habits = {}  # Ensure a clean state

    def tearDown(self):
        """Remove the test file after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_habit(self):
        """Test adding a new habit."""
        self.tracker.add_habit("Exercise", "Daily workout", "daily")
        self.assertIn("Exercise", self.tracker.habits)
        self.assertEqual(self.tracker.habits["Exercise"]["description"], "Daily workout")
        self.assertEqual(self.tracker.habits["Exercise"]["frequency"], "daily")
        self.assertEqual(self.tracker.habits["Exercise"]["completion_count"], 0)

    def test_add_existing_habit(self):
        """Test adding a habit that already exists."""
        self.tracker.add_habit("Exercise", "Daily workout", "daily")
        with self.assertRaises(ValueError):
            self.tracker.add_habit("Exercise", "Another description", "weekly")

    def test_mark_completed(self):
        """Test marking a habit as completed."""
        self.tracker.add_habit("Exercise", "Daily workout", "daily")
        self.tracker.mark_completed("Exercise")
        self.assertEqual(self.tracker.habits["Exercise"]["completion_count"], 1)

    def test_mark_completed_nonexistent_habit(self):
        """Test marking a nonexistent habit as completed."""
        with self.assertRaises(ValueError):
            self.tracker.mark_completed("Nonexistent")

    def test_view_progress(self):
        """Test viewing the progress of a habit."""
        self.tracker.add_habit("Exercise", "Daily workout", "daily")
        self.tracker.mark_completed("Exercise")
        progress = self.tracker.view_progress("Exercise")
        self.assertEqual(progress, 1)

    def test_view_progress_nonexistent_habit(self):
        """Test viewing progress of a nonexistent habit."""
        with self.assertRaises(ValueError):
            self.tracker.view_progress("Nonexistent")

    def test_remove_habit(self):
        """Test removing a habit."""
        self.tracker.add_habit("Exercise", "Daily workout", "daily")
        self.tracker.remove_habit("Exercise")
        self.assertNotIn("Exercise", self.tracker.habits)

    def test_remove_nonexistent_habit(self):
        """Test removing a nonexistent habit."""
        with self.assertRaises(ValueError):
            self.tracker.remove_habit("Nonexistent")

    def test_reset_progress(self):
        """Test resetting progress for all habits."""
        self.tracker.add_habit("Exercise", "Daily workout", "daily")
        self.tracker.add_habit("Meditation", "Daily meditation", "daily")
        self.tracker.mark_completed("Exercise")
        self.tracker.mark_completed("Meditation")
        self.tracker.reset_progress()
        self.assertEqual(self.tracker.habits["Exercise"]["completion_count"], 0)
        self.assertEqual(self.tracker.habits["Meditation"]["completion_count"], 0)


if __name__ == "__main__":
    unittest.main()
