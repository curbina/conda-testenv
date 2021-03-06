import argparse

import conda_testenv
import conda_testenv.test_env as test_env


def main():
    parser = argparse.ArgumentParser(description='Tool for running the tests '
                                                 'of all packages installed '
                                                 'in a conda environment')

    parser.add_argument('--version', action='version',
                        version=conda_testenv.__version__,
                        help="Show conda-testenv's version, and exit.")

    parser.add_argument('-p', dest='prefix')

    args = parser.parse_args()

    test_env.run_env_tests(args.prefix)


if __name__ == '__main__':
    main()
