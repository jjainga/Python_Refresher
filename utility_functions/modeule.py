#modules are used to help organize your code and make it easy to use/read/edit
# then your import the module to the app you are writing your code in

import converters
from converters import kgs_to_lbs


print(kgs_to_lbs(70))
print(converters.lbs_to_kgs(160))