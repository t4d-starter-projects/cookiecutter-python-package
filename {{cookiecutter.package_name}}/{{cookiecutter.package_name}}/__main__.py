"""Main Module"""

from {{cookiecutter.package_name}}.some_pkg.some_mod import do_it


def main() -> None:
    """Main Function"""

    do_it()
    print("Welcome to Package {{cookiecutter.package_name}}")


if __name__ == '__main__':
    main()
