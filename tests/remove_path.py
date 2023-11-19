import os
import sys
# =============================================================


current_directory = os.getcwd()
flaskr_path = os.path.join(current_directory, 'flaskr')
src_path = os.path.join(current_directory, 'src')

# sys.path.insert(0, flaskr_path)
# sys.path.insert(0, src_path)

# sys.path.pop(0)
# sys.path.pop(0)

print("Python path directory: ", sys.path)
print("The inserted path", os.path.join(current_directory, 'flaskr'))
# Your existing import statements go here

# ...

# Remove the added directories from sys.path
# sys.path.remove(flaskr_path)
# sys.path.remove(src_path)


# =============================================================
