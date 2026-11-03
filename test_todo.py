import unittest
import todo

class TestTodo(unittest.TestCase):
    def setUp(self):
        # Reset the in-memory store before each test
        todo.tasks = {}
        todo.next_id = 1

    def test_add_task(self):
        tid = todo.add("Buy groceries")
        self.assertEqual(tid, 1)
        self.assertIn(1, todo.tasks)
        self.assertEqual(todo.tasks[1]['name'], "Buy groceries")
        self.assertFalse(todo.tasks[1]['done'])

        tid2 = todo.add("Read a book")
        self.assertEqual(tid2, 2)
        self.assertEqual(todo.tasks[2]['name'], "Read a book")

    def test_list_tasks(self):
        todo.add("Task 1")
        todo.add("Task 2")
        tasks = todo.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[1]['name'], "Task 1")
        self.assertEqual(tasks[2]['name'], "Task 2")

    def test_done_task(self):
        tid = todo.add("Finish project")
        self.assertFalse(todo.tasks[tid]['done'])

        result = todo.done(tid)
        self.assertTrue(result)
        self.assertTrue(todo.tasks[tid]['done'])

        # Test marking a non-existent task as done
        result_fail = todo.done(99)
        self.assertFalse(result_fail)

    def test_delete_task(self):
        tid = todo.add("Wash car")
        self.assertIn(tid, todo.tasks)

        result = todo.delete(tid)
        self.assertTrue(result)
        self.assertNotIn(tid, todo.tasks)

        # Test deleting a non-existent task
        result_fail = todo.delete(99)
        self.assertFalse(result_fail)

if __name__ == '__main__':
    unittest.main()
