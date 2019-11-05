# Copyright 2019, University of Illinois at Chicago and Oregon Health & Science University
# This file is part of the deduplicator project.
# See the ReadMe.txt file for licensing information.

import unittest

import deduplicator.tests.test_match_dictionaries
import deduplicator.tests.test_adding_comparison_keys


if __name__ == "__main__":
	unittest.main(module = deduplicator.tests.test_match_dictionaries, verbosity=2, exit=False)
	unittest.main(module = deduplicator.tests.test_adding_comparison_keys, verbosity=2, exit=False)
