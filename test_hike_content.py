import unittest

class TestRead(unittest.TestCase):

  sample_emails = {
    "email": ['h@dummy.com', 'q@dummy.com'],
    "hike": ['10%', '20%']
  }

  def test_is_percentage(self, _):
    self.assertEqual(true, all(list(map(lambda s: s.count('%') > 0, TestRead.sample_emails["hike"]))))

if __name__ == '__main__':
  unittest.main()
