import unittest
from due_date import calculate_due_date
from datetime import datetime

class DueDateTestCase(unittest.TestCase):

    def test_submit_datetime_higher_value(self):
        with self.assertRaises(ValueError):
            calculate_due_date(datetime(2021, 6, 28, 19, 54, 55), 23), datetime(2021, 7, 1, 12, 54, 55)

    def test_submit_datetime_lover_value(self):
        with self.assertRaises(ValueError):
            calculate_due_date(datetime(2021, 6, 28, 8, 54, 55), 23), datetime(2021, 7, 1, 12, 54, 55)

    def test_submit_datetime_is_sunday(self):
        with self.assertRaises(ValueError):
            calculate_due_date(datetime(2021, 7, 10, 10, 54, 55), 23), datetime(2021, 7, 1, 12, 54, 55)

    def test_submit_datetime_is_saturday(self):
        with self.assertRaises(ValueError):
            calculate_due_date(datetime(2021, 7, 18, 9, 54, 55), 23), datetime(2021, 7, 1, 12, 54, 55)

    def test_actual_day(self):
        self.assertEqual(calculate_due_date(datetime(2021, 6, 28, 12, 54, 55), 3), datetime(2021, 6, 28, 15, 54, 55))

    def test_actual_day_higher_hours(self):
        self.assertEqual(calculate_due_date(datetime(2021, 6, 28, 12, 54, 55), 7), datetime(2021, 6, 29, 11, 54, 55))

    def test_friday_afternoon_one_hour_turnaround_time(self):
        self.assertEqual(calculate_due_date(datetime(2021, 7, 2, 16, 54, 55), 1), datetime(2021, 7, 5, 9, 54, 55))

    def test_friday_afternoon_more_than_one_day_turnaround_time(self):
        self.assertEqual(calculate_due_date(datetime(2021, 7, 2, 16, 54, 55), 10), datetime(2021, 7, 6, 10, 54, 55))

    def test_friday_afternoon_more_than_two_day_turnaround_time(self):
        self.assertEqual(calculate_due_date(datetime(2021, 7, 2, 16, 54, 55), 19), datetime(2021, 7, 7, 11, 54, 55))

    def test_next_day(self):
        self.assertEqual(calculate_due_date(datetime(2021, 6, 28, 13, 54, 55), 11), datetime(2021, 6, 29, 16, 54, 55))

    def test_two_day_after(self):
        self.assertEqual(calculate_due_date(datetime(2021, 6, 28, 13, 54, 55), 12), datetime(2021, 6, 30, 9, 54, 55))

    def test_three_day_after(self):
        self.assertEqual(calculate_due_date(datetime(2021, 6, 28, 13, 54, 55), 23), datetime(2021, 7, 1, 12, 54, 55))

    def test_final_date_on_saturday(self):
        self.assertEqual(calculate_due_date(datetime(2021, 6, 30, 13, 54, 55), 25), datetime(2021, 7, 5, 14, 54, 55))

    def test_final_date_on_sunday(self):
        self.assertEqual(calculate_due_date(datetime(2021, 6, 30, 13, 54, 55), 34), datetime(2021, 7, 6, 15, 54, 55))

    def test_final_date_on_sunday_after_working_hours(self):
        self.assertEqual(calculate_due_date(datetime(2021, 6, 30, 13, 54, 55), 36), datetime(2021, 7, 7, 9, 54, 55))

if __name__ == '__main__':
    unittest.main()
