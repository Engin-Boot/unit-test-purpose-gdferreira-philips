import unittest
from unittest.mock import patch
from read_excel_isolated import read_hike_data

class TestRead(unittest.TestCase):

  sample_emails = {
    "email": ['h@dummy.com', 'q@dummy.com'],
    "hike": ['10%', '20%']
  }

  def has_percentage_char(s):
    s.count("%");

  @patch('read_excel_isolated.pandas.read_excel', return_value=sample_emails)
  def test_is_percentage(self, _):
    hikes = read_hike_data()
    self.assertEqual(len(hikes), len(map(has_percentage_char, TestRead.sample_emails["hike"])))

if __name__ == '__main__':
  unittest.main()
