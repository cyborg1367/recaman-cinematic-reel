import math
import unittest

from python.camera import Camera, camera_for_time, project, temporal_depth
from python.recaman import generate, trace
from python.score import build_score, duration_seconds, master_gain


class RecamanTests(unittest.TestCase):
    def test_known_prefix(self):
        self.assertEqual(generate(10), [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11])

    def test_trace_matches_values(self):
        jumps = trace(180)
        self.assertEqual(len(jumps), 180)
        self.assertEqual([0, *(jump.destination for jump in jumps)], generate(180))
        self.assertTrue(all(jump.step == index for index, jump in enumerate(jumps, 1)))

    def test_negative_steps_are_rejected(self):
        with self.assertRaises(ValueError):
            generate(-1)


class ScoreTests(unittest.TestCase):
    def test_score_is_exactly_one_minute(self):
        self.assertAlmostEqual(duration_seconds(), 60.0)

    def test_score_has_all_three_voices(self):
        voices = {event.voice for event in build_score()}
        self.assertEqual(voices, {"bass", "arpeggio", "melody"})

    def test_master_fades_only_in_last_three_seconds(self):
        self.assertEqual(master_gain(57.0), 1.0)
        self.assertAlmostEqual(master_gain(58.5), 0.5)
        self.assertEqual(master_gain(60.0), 0.0)


class CameraTests(unittest.TestCase):
    def test_temporal_depth(self):
        self.assertAlmostEqual(temporal_depth(12, 10), 2.9)

    def test_front_projection_is_identity(self):
        x, y = project((12.0, -4.0, 0.0), Camera())
        self.assertAlmostEqual(x, 12.0)
        self.assertAlmostEqual(y, -4.0)

    def test_camera_reveal_stays_finite(self):
        camera = camera_for_time(30.0)
        x, y = project((30.0, 10.0, temporal_depth(90, 100)), camera)
        self.assertTrue(math.isfinite(x) and math.isfinite(y))


if __name__ == "__main__":
    unittest.main()

