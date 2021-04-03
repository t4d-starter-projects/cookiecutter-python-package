""" Test Sample Module """

from unittest import TestCase, main

from {{cookiecutter.package_name}}.some_pkg.some_mod import do_it


class TestSample(TestCase):
    """ Test Sample Class """

    def test_sample(self) -> None:
        """ Sample Test """

        result = do_it()

        self.assertEqual(result, True)


if __name__ == "__main__":
    main()
