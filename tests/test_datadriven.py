import unittest
import unittest.loader

import datadriven as data


def add_metadata(metadata):
    def decorator(f):
        f.__metadata = metadata
        return f

    return decorator


class DataDrivenTest(unittest.TestCase):

    expected_results = dict(
        test_data_driven_method_dataA=(1, 0),
        test_data_driven_method_dataB=(3, 4),
        test_data_driven_method_dataC=(5, 6),
    )

    @data.datadriven(
        dataA=data.Args(1),
        dataB=data.Args(3, 4),
        dataC=data.Args(first_number=5, second_number=6),
    )
    def test_data_driven_method(self, first_number, second_number=0):
        self.assertEqual(
            self.expected_results[self._testMethodName], (first_number, second_number)
        )

    @data.datadriven(single_test_case=data.Args())
    @add_metadata("metadata")
    def test_data_driven_preserves_metadata(self, *args, **kwargs):
        self.assertEqual(
            "metadata",
            getattr(
                self.test_data_driven_preserves_metadata_single_test_case,
                "__metadata",
                None,
            ),
        )

    def test_datadriven_creates_methods(self):
        test_methods = unittest.loader.getTestCaseNames(self.__class__, "test_")

        for method_name in self.expected_results:
            self.assertIn(method_name, test_methods)
            self.assertTrue(
                callable(getattr(self, method_name)),
                msg="{} should be callable".format(method_name),
            )


class MatrixDataDrivenTest(unittest.TestCase):

    expected_results = dict(
        test_matrix_datadriven_method_neo_blue=("neo", "blue"),
        test_matrix_datadriven_method_neo_red=("neo", "red"),
        test_matrix_datadriven_method_trinity_blue=("trinity", "blue"),
        test_matrix_datadriven_method_trinity_red=("trinity", "red"),
        test_matrix_datadriven_method_morpheus_blue=("morpheus", "blue"),
        test_matrix_datadriven_method_morpheus_red=("morpheus", "red"),
    )

    @data.matrix_datadriven(
        [
            dict(
                neo=data.Args(name="neo"),
                trinity=data.Args(name="trinity"),
                morpheus=data.Args("morpheus"),
            ),
            dict(blue=data.Args(pill="blue"), red=data.Args(pill="red")),
        ]
    )
    def test_matrix_datadriven_method(self, name, pill):
        self.assertEqual(self.expected_results[self._testMethodName], (name, pill))

    def test_matrix_datadriven_creates_methods(self):
        test_methods = unittest.loader.getTestCaseNames(self.__class__, "test_")

        for method_name in self.expected_results:
            self.assertIn(method_name, test_methods)
            self.assertTrue(
                callable(getattr(self, method_name)),
                msg="{} should be callable".format(method_name),
            )
