import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
search_dir = "/Users/samiatkolawole/PycharmProjects/**/*.py"  #Use ** for recursive search, allows glob to search for files inside subdirectories as well, rather than only in the specified folder.
# Get list of matching files
for file in glob.glob(search_dir, recursive=True):
# TODO: use os.path.getsize to find each file's size
    size = os.path.getsize(file)
# TODO: Remove the leading directory name(s) from each filename before you print it -
    baseline = os.path.basename(file)
    if size > 0:
        print("Files with greater than 0 bytes", baseline, size, "bytes")
# TODO: Add a test to only display files that are not zero length
    else:
        print("Files with 0 bytes",baseline)