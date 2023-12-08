from unittest import TestCase
from test_multiple_forms import Translate


class TestTranslate(TestCase):
    def test_move(self):
        t = Translate((1, 1))
        result = t.move((2, 2))
        self.assertEqual((3, 3), result)


