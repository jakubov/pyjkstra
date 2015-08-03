import os
import argparse

import nose


def main():
    env = os.environ.copy()
    # Don't capture output, print to STDOUT
    env['NOSE_NOCAPTURE'] = 1

    parser = argparse.ArgumentParser()
    parser.add_argument("--with-coverage", help="Run with coverage", action='store_true')
    parser.add_argument("--cover-html", help="output coverage html", action='store_true')
    parser.add_argument("--tests", help="Run certain tests", action='store')
    parser.add_argument("-v", help="Be more verbose", action='store_true')
    parser.add_argument("-x", "--stop", help="Stop running tests after the first error or failure", action='store_true')
    parser.add_argument("--not-local", help="We are not running the test locally, use a different config file.")


    args = parser.parse_args()
    os.environ['SERVICE_ENVIRONMENT'] = 'Testing' if args.not_local else 'TestingLocal'

    if args.with_coverage:
        env['NOSE_WITH_COVERAGE'] = 1
        env['NOSE_COVER_PACKAGE'] = 'pyjkstra'

    nose.main(env=env)

if __name__ == '__main__':
    main()
