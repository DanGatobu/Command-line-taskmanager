import unittest
import subprocess

class TestJafrApp(unittest.TestCase):
    def run_command(self, command):
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)  # Print the captured output for debugging
        return result

    def test_create_note(self):
        result = subprocess.run(["python3", "task_manager.py", "create", "--filename", "test_tasks.txt", "--task", "Finish project", "--date", "2023-09-01", "--time", "1500"], capture_output=True, text=True)
        print(result.stdout)
        self.assertIn("Note created successfully", result.stdout)
    def test_create_task(self):
        result = subprocess.run(["python3", "task_manager.py", "addto_note", "--filename", "test_tasks.txt", "--task", "Added note", "--date", "2023-09-01", "--time", "1500"], capture_output=True, text=True)
        self.assertIn("Task created successfully", result.stdout)
    def test_create_task2(self):
        result = subprocess.run(["python3", "task_manager.py", "addto_note", "--filename", "test_tasks.txt", "--task", "Added note2", "--date", "2023-09-01", "--time", "1500"], capture_output=True, text=True)
        self.assertIn("Task created successfully", result.stdout)
    def test_create_task3(self):
        result = subprocess.run(["python3", "task_manager.py", "addto_note", "--filename", "test_tasks.txt", "--task", "Added note3", "--date", "2023-09-01", "--time", "1500"], capture_output=True, text=True)
        self.assertIn("Task created successfully", result.stdout)

    def test_update_task(self):
        result = subprocess.run(["python3", "task_manager.py", "modifynote_content", "--filename", "test_tasks.txt", "--updatetext", "Added note2", "--newtext", "yes its working"], capture_output=True, text=True)
        self.assertIn("Task created successfully", result.stdout)
    def test_delete_task(self):
        result = subprocess.run(["python3", "task_manager.py", "deletenote_content", "--filename", "test_tasks.txt", "--delete_notecontent", "Added note"], capture_output=True, text=True)
        self.assertIn("Task created successfully", result.stdout)
    def test_mark_completed(self):
        result = subprocess.run(["python3", "task_manager.py", "markcomplete", "--filename", "test_tasks.txt", "--complete_taskname", "Added note3"], capture_output=True, text=True)
        self.assertIn("Task created successfully", result.stdout)
    def test_list(self):
        result = subprocess.run(["python3", "task_manager.py", "list", "--filename", "test_tasks.txt"], capture_output=True, text=True)
        self.assertIn("Note created successfully", result.stdout)
        

    def test_delete_note(self):
        result = subprocess.run(["python3", "task_manager.py", "delete_completenote", "--filename", "test_tasks.txt"], capture_output=True, text=True)
        self.assertIn("Note deleted successfully", result.stdout)


if __name__ == "__main__":
    unittest.main()