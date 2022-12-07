import sys
import subprocess
import pkg_resources


required = {'termcolor'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call(
        [python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
# ^ This entire code essentially checks for termcolor and if the user does not have it installed, it will install it before moving forward.
# ========================================================================================================================================