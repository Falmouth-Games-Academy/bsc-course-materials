import re
import sys
import os


def get_parts(filename):
    try:
        with open(filename, 'rt') as f:
            for line in f:
                line = line.split('%')[0]
                m = re.search('\\input{([^}]*)}', line)
                if m is not None:
                    child_filename = m.group(1)
                    if not child_filename.endswith('.tex'):
                        child_filename += '.tex'
                    child_filename = os.path.join(os.path.dirname(filename), child_filename)
                    get_parts(child_filename)
                else:
                    m = re.search('\\part{([^}]*)}', line)
                    if m is not None:
                        print "\t", m.group(1)
    except IOError as e:
        print e

if __name__ == '__main__':
    for filename in sys.argv[1:]:
        print
        print filename
        get_parts(filename)
