""" Test Sample Module """

from {{cookiecutter.package_name}}.some_pkg.some_mod import do_it


class TestSample:
    """ Test Sample Class """

    def test_sample(self) -> None:
        """ Sample Test """

        result = do_it()

        assert result is True
