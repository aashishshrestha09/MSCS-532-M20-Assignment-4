import unittest
from src import priority_queue


class TestPriorityQueue(unittest.TestCase):

    def test_insert_and_extract_max(self):
        pq = priority_queue.PriorityQueue()
        pq.insert(priority_queue.Task(priority=3, task_id=1))
        pq.insert(priority_queue.Task(priority=5, task_id=2))
        pq.insert(priority_queue.Task(priority=1, task_id=3))

        self.assertEqual(pq.extract_max().priority, 5)
        self.assertEqual(pq.extract_max().priority, 3)
        self.assertEqual(pq.extract_max().priority, 1)
        self.assertIsNone(pq.extract_max())

    def test_increase_key(self):
        pq = priority_queue.PriorityQueue()
        pq.insert(priority_queue.Task(priority=3, task_id=1))
        pq.insert(priority_queue.Task(priority=2, task_id=2))

        pq.increase_key(2, 4)
        self.assertEqual(pq.extract_max().priority, 4)

    def test_decrease_key(self):
        pq = priority_queue.PriorityQueue()
        pq.insert(priority_queue.Task(priority=5, task_id=1))
        pq.insert(priority_queue.Task(priority=7, task_id=2))

        pq.decrease_key(2, 1)
        self.assertEqual(pq.extract_max().priority, 5)
        self.assertEqual(pq.extract_max().priority, 1)

    def test_is_empty(self):
        pq = priority_queue.PriorityQueue()
        self.assertTrue(pq.is_empty())
        pq.insert(priority_queue.Task(priority=2, task_id=1))
        self.assertFalse(pq.is_empty())

    def test_invalid_increase_key(self):
        pq = priority_queue.PriorityQueue()
        pq.insert(priority_queue.Task(priority=3, task_id=1))
        with self.assertRaises(ValueError):
            pq.increase_key(5, 10)
        with self.assertRaises(ValueError):
            pq.increase_key(1, 1)  # lower new priority is invalid

    def test_invalid_decrease_key(self):
        pq = priority_queue.PriorityQueue()
        pq.insert(priority_queue.Task(priority=5, task_id=1))
        with self.assertRaises(ValueError):
            pq.decrease_key(3, 1)
        with self.assertRaises(ValueError):
            pq.decrease_key(1, 10)  # higher new priority is invalid


if __name__ == "__main__":
    unittest.main()
