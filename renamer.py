from glob import glob
from os import rename

# Set src_path to be the directory containing the files you want to rename.
#   use double backslashes (\\) as seperator, must include the seperator at the end

src_path = "D:\\change\\this\\to\\your\\directory\\"


# Set filename_prefix to what you want the first part of the filename to be.
#   This prefix will be concatenated with a serialized integer to form the new filename

filename_prefix = "prefix"


# Set src_extension to the extension of the files you want to find.  This uses standard wildcard pattern matching.
#   i.e. "*" will return all files, "stl" will return all files with the extension of .stl,
#       "jp*" will return all files with an extension that starts with 'jp' like both .jpg and .jpeg.

src_extension = "*"


# count is the starting number used for renaming files.  Normally this should be set to 0.  Change it if you
#   want to start renaming with a particular number.

count = 0

# Below this line is the actual code that executes.  Don't change it unless you know Python and want to customize it.
# -------------------------------------------------------------------------------------------------------------------

for file in glob(f"{src_path}*.{src_extension}"):
    # Grab the extension of the file being renamed to be reused in the next statement.
    #   This is done so we can use wildcards in the pattern matching without fouling up the renamed file.
    dest_extension = file.split(".")[-1]

    # Create a string with the path, prefix, and existing extension
    newFilename = f"{src_path}{filename_prefix}-{count:04d}.{dest_extension}"

    # A couple of print statements to output to screen the renaming.  This is mostly just so you can see that it is
    #   still working on long runs.
    print(f" Renaming {file} to {newFilename}")
    print()

    # Increment the count variable so the next file has a new number in sequence
    count += 1

    # Rename the file
    rename(file, newFilename)

