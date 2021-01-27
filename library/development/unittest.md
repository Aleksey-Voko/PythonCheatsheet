# Cheatsheet [unittest](https://docs.python.org/3/library/unittest.html) — Unit testing framework

### Run all tests:
unittest: `$ py -m unittest`  
or with details: `$ py -m unittest -v`

pytest: `$ pytest`  
or min: `$ pytest -q`

nose2: `$ nose2`  
or with details: `$ nose2 -v`

---

### Assert methods:
Method | Checks that
------ | -----------
assertEqual(a, b) | a == b
assertNotEqual(a, b) | a != b
assertTrue(x) | bool(x) is True
assertFalse(x) | bool(x) is False
assertIs(a, b) | a is b
assertIsNot(a, b) | a is not b
assertIsNone(x) | x is None
assertIsNotNone(x) | x is not None
assertIn(a, b) | a in b
assertNotIn(a, b) | a not in b
assertIsInstance(a, b) | isinstance(a, b)
assertNotIsInstance(a, b) | not isinstance(a, b)
assertRaises(exc, fun, *args, **kwds) | fun(*args, **kwds) raises exc
assertRaisesRegex(exc, r, fun, *args, **kwds) | fun(*args, **kwds) raises exc and the message matches regex r
assertWarns(warn, fun, *args, **kwds) | fun(*args, **kwds) raises warn
assertWarnsRegex(warn, r, fun, *args, **kwds) | fun(*args, **kwds) raises warn and the message matches regex r
assertLogs(logger, level) | The with block logs on logger with minimum level
assertAlmostEqual(a, b) | round(a-b, 7) == 0
assertNotAlmostEqual(a, b) | round(a-b, 7) != 0
assertGreater(a, b) | a > b
assertGreaterEqual(a, b) | a >= b
assertLess(a, b) | a < b
assertLessEqual(a, b) | a <= b
assertRegex(s, r) | r.search(s)
assertNotRegex(s, r) | not r.search(s)
assertCountEqual(a, b) | a and b have the same elements in the same number, regardless of their order.

#### Used to compare:
Method | Used to compare
------ | ---------------
assertMultiLineEqual(a, b) | strings
assertSequenceEqual(a, b) | sequences
assertListEqual(a, b) | lists
assertTupleEqual(a, b) | tuples
assertSetEqual(a, b) | sets or frozensets
assertDictEqual(a, b) | dicts

---

#### Example:
[primes.py](primes.py) - class under test  
[test_primes.py](test_primes.py) - class template with tests
