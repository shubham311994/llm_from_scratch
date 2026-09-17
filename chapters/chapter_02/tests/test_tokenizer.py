import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from tokenizer import Tokenizer


class TokenizerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tokenizer = Tokenizer.from_text("Hello, world! Hello.")

    def test_tokenize_separates_punctuation(self) -> None:
        self.assertEqual(self.tokenizer.tokenize("Hello, world!"), ["Hello", ",", "world", "!"])

    def test_encode_decode_round_trip(self) -> None:
        encoded = self.tokenizer.encode("Hello, world!")
        self.assertEqual(self.tokenizer.decode(encoded), "Hello, world!")

    def test_unknown_and_boundaries(self) -> None:
        encoded = self.tokenizer.encode("unknown", add_boundaries=True)
        self.assertEqual(len(encoded), 3)
        self.assertEqual(self.tokenizer.decode(encoded), "[UNK]")

    def test_invalid_id_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.tokenizer.decode([999])


if __name__ == "__main__":
    unittest.main()