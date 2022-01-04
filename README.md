# datadriven

datadriven allows you to run a test case multiple times with different data. It was designed to work
with `unittest.TestCase` test methods, any test runner (nose, nose2, unittest, unittest2 and
pytest), in Python 2.7 or 3.7+.

## Usage

```py
import datadriven

class SomeTestCase(unittest.TestCase):

    @datadriven.datadriven(
        caseA=datadriven.Args(first="foo"),
        caseB=datadriven.Args("hello", second="world"),
    )
    def test_method(self, first, second=None):
        ...
```

This is the equivalent of writing:

```py
import datadriven

class SomeTestCase(unittest.TestCase):

    def test_method(self, first, second=None):
        ...

    def test_method_caseA(self):
        self.test_method("foo")

    def test_method_caseB(self):
        self.test_method("hello", "world")
```

The only difference is that the test `test_method` won't actually be executed.

## License

[Apache-2.0 License](./LICENSE)
