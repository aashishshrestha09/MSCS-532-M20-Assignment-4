# priority_queue.py

from dataclasses import dataclass
from typing import Optional


@dataclass(order=True)
class Task:
    """
    Represents a schedulable task.

    Attributes:
        priority (int): The priority of the task. Higher value means higher priority.
        task_id (int): Unique identifier for the task.
        arrival_time (Optional[float]): Time at which the task arrives.
        deadline (Optional[float]): Deadline by which the task must be completed.
    """

    priority: int
    task_id: int
    arrival_time: Optional[float] = None
    deadline: Optional[float] = None

    def __repr__(self):
        return (
            f"Task(id={self.task_id}, priority={self.priority}, "
            f"arrival={self.arrival_time}, deadline={self.deadline})"
        )


class PriorityQueue:
    """
    Implements a max-heap priority queue for Task objects.
    """

    def __init__(self):
        self.heap: list[Task] = []
        self.task_index_map: dict[int, int] = {}

    def is_empty(self) -> bool:
        """Return True if the queue is empty."""
        return len(self.heap) == 0

    def insert(self, task: Task):
        """
        Insert a new task into the priority queue.
        Time complexity: O(log n)
        """
        self.heap.append(task)
        self.task_index_map[task.task_id] = len(self.heap) - 1
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self) -> Optional[Task]:
        """
        Remove and return the task with the highest priority.
        Time complexity: O(log n)
        """
        if self.is_empty():
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_task = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_task

    def increase_key(self, task_id: int, new_priority: int):
        """
        Increase the priority of a task by task_id.
        Time complexity: O(n) for lookup + O(log n) for heapify.
        """
        index = self._find_task_index(task_id)
        if index is None:
            raise ValueError(f"Task with id {task_id} not found")
        if new_priority < self.heap[index].priority:
            raise ValueError("New priority must be higher than current priority")

        self.heap[index].priority = new_priority
        self._heapify_up(index)

    def decrease_key(self, task_id: int, new_priority: int):
        """
        Decrease the priority of a task by task_id.
        Time complexity: O(n) for lookup + O(log n) for heapify.
        """
        index = self._find_task_index(task_id)
        if index is None:
            raise ValueError(f"Task with id {task_id} not found")
        if new_priority > self.heap[index].priority:
            raise ValueError("New priority must be lower than current priority")

        self.heap[index].priority = new_priority
        self._heapify_down(index)

    def _find_task_index(self, task_id: int) -> Optional[int]:
        """Helper method to find the index of a task by task_id. O(n)"""
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                return i
        return None

    def _heapify_up(self, index: int):
        """Restore heap property by moving task at index up."""
        parent_index = (index - 1) // 2
        while (
            index > 0 and self.heap[index].priority > self.heap[parent_index].priority
        ):
            self.heap[index], self.heap[parent_index] = (
                self.heap[parent_index],
                self.heap[index],
            )
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index: int):
        """Restore heap property by moving task at index down."""
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and self.heap[left].priority > self.heap[largest].priority:
                largest = left
            if right < size and self.heap[right].priority > self.heap[largest].priority:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest
