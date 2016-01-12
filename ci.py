# to be run by jenkins.
import os
import logging
import argparse
LOG = logging.getLogger(__name__)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', required=True, help="result files for test cases")
    args = parser.parse_args()
    for filename in os.listdir(args.dir):
        if filename.endswith('py') and filename not in ("ci.py", "__init__.py"):
            filepath = os.path.join(args.dir, filename)
            LOG.debug("-----------------python %s--------------------", filepath)
            os.system("python %s" % filepath)