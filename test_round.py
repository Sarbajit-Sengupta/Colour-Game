import unittest
from unittest.mock import Mock, patch
import main


class RoundTests(unittest.TestCase):
    def test_first_enter_starts_full_round_without_scoring(self):
        main.timeleft, main.score, main.started = 30, 0, False
        main.e, main.label = Mock(), Mock()
        main.e.get.return_value = 'Blue'
        main.e.delete.side_effect = lambda *args: setattr(main.e.get, 'return_value', '')
        main.timeLabel, main.scoreLabel = Mock(), Mock()
        with patch.object(main.random, 'shuffle'):
            main.startGame(None)
            self.assertEqual(main.score, 0)
            self.assertEqual(main.timeleft, 30)
            main.timeLabel.after.assert_called_once_with(1000, main.countdown)
            main.e.get.return_value = 'Blue'
            main.startGame(None)
            self.assertEqual(main.score, 1)
            self.assertEqual(main.timeLabel.after.call_count, 1)
            main.countdown()
            self.assertEqual(main.timeleft, 29)


if __name__ == '__main__':
    unittest.main()
