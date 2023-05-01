import os
import yaml

env = 'accounts'
if env in ['accounts']:
    TEST_DATA = yaml.safe_load(open(os.path.dirname(__file__) + "/login/yml/{}.yml".format(env)))
else:
    raise ("Invalid Environment")

