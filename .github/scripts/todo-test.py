import io
import sys
import unittest
sys.path.insert(0, "/app/.github/scripts")
sys.path.insert(0, ".github/scripts")
from todo import Task, TaskPool


class TestTaskPool(unittest.TestCase):
    def setUp(self):
        self.pool = TaskPool()

    def test_add_task(self):
        self.pool.add_task(Task("New"))
        self.assertEqual(len(self.pool.tasks), 1)

    def test_get_open_tasks(self):
        self.pool.populate()
        self.assertEqual(len(self.pool.get_open_tasks()), 3)

    def test_get_done_tasks(self):
        self.pool.populate()
        self.assertEqual(len(self.pool.get_done_tasks()), 3)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskPool)
    stream = io.StringIO()
    unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    for line in stream.getvalue().splitlines():
        if "... ok" in line:
            print(line.split(" (")[0] + " ... ok")
        elif "FAIL" in line or "ERROR" in line:
            print(line)
