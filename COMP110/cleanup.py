import os
import glob
import re
import win32api

INCLUDE_TEX_PATTERNS = [
    re.compile(r"\\input{([^}]*)}"),
    re.compile(r"\\include{([^}]*)}")
]

INCLUDE_IMAGE_PATTERNS = [
    re.compile(r"\\includegraphics\[[^]]*\]{([^}]*)}"),
    re.compile(r"\\pictureslide{[^}]*}{([^}]*)}"),
    re.compile(r"\\pictureslideb{[^}]*}{([^}]*)}"),
]

IMAGE_EXTENSIONS = [".pdf", ".png", ".jpg", ".jpeg"]

DELETE_PATTERNS = ["*.tex"] + ["*" + ext for ext in IMAGE_EXTENSIONS if ext != ".pdf"]



# https://stackoverflow.com/a/3788191
def get_proper_cased_path(p):
    return win32api.GetLongPathName(win32api.GetShortPathName(p))


def get_included_files(filepath):
    with open(filepath, 'rt') as f:
        for line in f:
            comment_position = line.find('%')
            if comment_position > -1:
                line = line[:comment_position]
            
            for pattern in INCLUDE_TEX_PATTERNS:
                result = pattern.search(line)
                if result is not None:
                    included_file = os.path.join(os.path.dirname(filepath), result[1]) + ".tex"
                    included_file = get_proper_cased_path(included_file)
                    yield included_file
                    for x in get_included_files(included_file):
                        yield x
            
            for pattern in INCLUDE_IMAGE_PATTERNS:
                result = pattern.search(line)
                if result is not None and not result[1].startswith("#"): # ignore newcommand definitions
                    base_name = os.path.join(os.path.dirname(filepath), result[1])
                    image_files = [base_name + ext for ext in IMAGE_EXTENSIONS if os.path.exists(base_name + ext)]
                    assert(len(image_files) == 1)
                    yield get_proper_cased_path(image_files[0])



def cleanup_dir(dirpath):
    root_files = glob.glob(os.path.join(dirpath, "20*materials.tex")) + glob.glob(os.path.join(dirpath, "20*materials-screen.tex"))
    dead_files = set()
    for pattern in DELETE_PATTERNS:
        dead_files.update(glob.glob(os.path.join(dirpath, pattern)))
    
    if root_files == []:
        print("Root file not found -- skipping")
        return

    live_files = set(root_files)

    for root_file in root_files:
        live_files.update(get_included_files(root_file))

    for live_file in live_files:
        if not live_file.lower().endswith(".pdf"):
            dead_files.remove(live_file)

    print(dead_files)

    for dead_file in dead_files:
        os.remove(dead_file)

    print("......")


if __name__ == '__main__':
    for dirname in os.listdir():
        if os.path.isdir(dirname) and not dirname.startswith("."):
            cleanup_dir(dirname)
