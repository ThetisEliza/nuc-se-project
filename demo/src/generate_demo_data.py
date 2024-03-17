
from model.data import Group

def generate_data(output_file, n = 30):
    with open(output_file, 'w') as f:
        for i in range(n):
            f.writelines(Group().random_gen().to_json()+"\n")

import sys


if __name__ == '__main__':
    generate_data(sys.argv[1], 50)