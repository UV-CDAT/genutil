import os
import sys
import cdat_info

test_suite_name = 'genutil'

workdir = os.getcwd()
runner = cdat_info.TestRunnerBase(test_suite_name, get_sample_data=True)
ret_code = runner.run(workdir)

sys.exit(ret_code)
