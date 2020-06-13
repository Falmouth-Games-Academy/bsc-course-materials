import os

old_year = "2019-20"
new_year = "2020-21"

for (dirpath, dirnames, filenames) in os.walk('.'):
    try:
        dirnames.remove(".git")
    except ValueError:
        pass

    for filename in filenames:
        if filename.startswith(old_year):
            new_filename = new_year + filename[len(old_year):]
            print("Renaming", filename, "to", new_filename, "in", dirpath)

            old_path = os.path.join(dirpath, filename)
            new_path = os.path.join(dirpath, new_filename)
            os.rename(old_path, new_path)
