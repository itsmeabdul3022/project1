from sayings import hello
from sayings import goodbye
import sys

if len(sys.argv) < 2:
    sys.exit()

hello(sys.argv[1])
goodbye(sys.argv[2])


