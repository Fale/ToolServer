#
# Load the user fixes file.

import config
import os
for filename in os.listdir(config.datafilepath(config.base_dir , "user-fixes")):
    execfile(config.datafilepath(config.base_dir , "user-fixes", filename))
