import unittest


class TestContentLoad(unittest.TestCase):

    sample_emails = {
        "email": ['h@dummy.com', 'q@dummy.com'],
        "hike": ['10%', '20%']
    }

    def test_number_emails_hikes(self):
        self.assertEqual(true, len(TestRead.sample_emails["email"]) == len(TestRead.sample_emails["hike"]))        
    
    def test_email_is_null(self):
        self.assertEqual(true, all(list(map(lambda s: s == "", TestRead.sample_emails["email"]))))
        
    def test_email_is_valid(self):
        self.assertEqual(true, all(list(map(lambda s: s.count("@") == 1 && s.count(".com") == 1, TestRead.sample_emails["email"]))))

    def test_hike_is_null(self):
        self.assertEqual(true, all(list(map(lambda s: s == "", TestRead.sample_emails["hike"]))))

    def test_hike_is_percent(self):
        self.assertEqual(true, all(list(map(lambda s: s[-1] == '%', TestRead.sample_emails["hike"]))))

    def test_hike_is_number(self):
        self.assertEqual(true, all(list(map(lambda s: float(s[0:-1]) == 0 || float(s[0:-1]) != 0, TestRead.sample_emails["hike"]))))

    def test_hike_is_over_percent(self):
        self.assertEqual(true, all(list(map(lambda s: float(s[0:-1]) > 100, TestRead.sample_emails["hike"]))))

    def test_hike_is_under_percent(self):
        self.assertEqual(true, all(list(map(lambda s: float(s[0:-1]) < 0, TestRead.sample_emails["hike"]))))

if __name__ == '__main__':
  unittest.main()
