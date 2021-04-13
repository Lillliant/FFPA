import argparse

def args_parser():
    parser = argparse.ArgumentParser()
    # Basic params
    parser.add_argument('--l', type=int, default=3, help="target fragment length")
    parser.add_argument('--k', type=int, default=100, help="threshold of k-anonymity")
    parser.add_argument('--delta', type=float, default=0.1, help="allowed error rate for k-anonymity")
    parser.add_argument('--epsilon', type=float, default=5.0, help="param of LDP")

    # Settings
    parser.add_argument('--load_pickle', action='store_true', help='read dataset form pickle file')
    parser.add_argument('--write_pickle', action='store_true', help='store dataset into pickle file, do not work when --load_pickle is activated')


    parser.add_argument('--min_length', type=int, default=None, help="minimal length of each trajectory")
    parser.add_argument('--max_length', type=int, default=None, help="maximal length of each trajectory")


    args = parser.parse_args()
    return args