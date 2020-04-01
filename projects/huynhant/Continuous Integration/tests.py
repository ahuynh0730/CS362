import unittest
import task
import datetime


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def testcirclearea(self):
        expected = 78.54
        radius = 5
        self.assertAlmostEqual(expected, task.circlearea(radius), 2)

        expected = 28.27
        radius = 3
        self.assertAlmostEqual(expected, task.circlearea(radius), 2)

        expected = 12.57
        radius = 2
        self.assertAlmostEqual(expected, task.circlearea(radius), 2)

    def test_ends_of_list(self):
        list = ["apple", "banana", "cherry", "orange"]
        first_in_list, last_in_list = task.ends_of_list(list)
        self.assertEqual(first_in_list, "apple")
        self.assertEqual(last_in_list, "orange")

    def test_date_difference(self):
        date1 = datetime.date(2020, 3, 1)
        date2 = datetime.date(2020, 2, 23)
        self.assertEqual(7, task.date_difference(date1, date2))


if __name__ == '__main__':
    unittest.main()
