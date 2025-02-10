# Unit Testing

This section contains unit tests for validating various string methods using Python's built-in `unittest` module.

```python
import unittest


class TestStringMethods(unittest.TestCase):
    # This is first test case (1)
    def test_strip(self):
        self.assertEqual("www.dicoding.com".strip("c.mow"), "dicoding")

    # This is second test case (2)
    def test_isalnum(self):
        self.assertTrue("c0d1ng".isalnum())
        self.assertFalse("c0d!ng".isalnum())

    # This is third test case (3)
    def test_index(self):
        s = "dicoding"
        self.assertEqual(s.index("coding"), 2)
        # Check if "decode" is NOT found in s
        with self.assertRaises(ValueError):
            s.index("decode")


if __name__ == "__main__":
    # Test Runner
    unittest.main()

# python main.py 
# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s

# OK
```

## User

This unit test suite verifies the behavior of the `User` class in relation to its activation status. It simulates database connectivity using `koneksi_ke_db()` and `putus_koneksi_db()` functions.

```python
import unittest


def koneksi_ke_db():
    print("[terhubung ke db]")


def putus_koneksi_db(db):
    print("[tidak terhubung ke db {}]".format(db))


class User:
    username = ""
    aktif = False

    def __init__(self, db, username):  # using db sample
        self.username = username

    def set_aktif(self):
        self.aktif = True


class TestUser(unittest.TestCase):
    # Test Case 1
    def test_user_default_not_active(self):
        db = koneksi_ke_db()
        kisah = User(db, "kisah")
        self.assertFalse(kisah.aktif)  # tidak aktif secara default
        putus_koneksi_db(db)

    # Test Case 2
    def test_user_is_active(self):
        db = koneksi_ke_db()
        kisah = User(db, "kisah")
        kisah.set_aktif()  # aktifkan user baru
        self.assertTrue(kisah.aktif)
        putus_koneksi_db(db)


if __name__ == "__main__":
    # Test Runner
    unittest.main()

# python main.py
#
# [terhubung ke db]
# [tidak terhubung ke db None]
# .[terhubung ke db]
# [tidak terhubung ke db None]
# .
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK
```

This section contains unit tests for the `User` class, ensuring correct behavior regarding user activation status.  
To improve efficiency, we use **test fixtures** with the `setUp()` and `tearDown()` methods.

```python
import unittest


def koneksi_ke_db():
    print("[terhubung ke db]")


def putus_koneksi_db(db):
    print("[tidak terhubung ke db {}]".format(db))


class User:
    username = ""
    aktif = False

    def __init__(self, db, username):  # using db sample
        self.username = username

    def set_aktif(self):
        self.aktif = True


class TestUser(unittest.TestCase):
    # Test Fixture
    def setUp(self):
        self.db = koneksi_ke_db()
        self.kisah = User(self.db, "kisah")

    def tearDown(self):
        putus_koneksi_db(self.db)

    # Test Case 1
    def test_user_default_not_active(self):
        self.assertFalse(self.kisah.aktif)  # tidak aktif secara default

    # Test Case 2
    def test_user_is_active(self):
        self.kisah.set_aktif()  # aktifkan user baru
        self.assertTrue(self.kisah.aktif)


if __name__ == "__main__":
    # Test Runner
    unittest.main()

# python main.py
#
# [terhubung ke db]
# [tidak terhubung ke db None]
# .[terhubung ke db]
# [tidak terhubung ke db None]
# .
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK
```
