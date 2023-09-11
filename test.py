import unittest

from data.data import get_todays_birthdays
from letters import replace_names


class TestBirthdays(unittest.TestCase):

    def test_get_todays_birthdays(self):
        expected_result = [{'name': 'Boromir', 'email': 'boromir@email.com', 'year': 1999, 'month': 9, 'day': 11}]
        self.assertEqual(get_todays_birthdays(), expected_result)

    def test_replace_names(self):
        text = "Dear [NAME],\n\nHappy birthday!\n\nAll the best for the year!\n\n[YOUR_NAME]"
        result = replace_names(text, "Boromir", "Gollum")
        expected_result = "Dear Boromir,\n\nHappy birthday!\n\nAll the best for the year!\n\Gollum"
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()