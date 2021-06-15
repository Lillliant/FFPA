import argparse

def args_parser():
    parser = argparse.ArgumentParser()
    # Basic params
    parser.add_argument('--k', type=int, default=50, help="param of k-anonymity")
    parser.add_argument('--xi', type=float, default=0.1, help="allowed error rate for k-anonymity")
    parser.add_argument('--epsilon', type=float, default=10.0, help="param of LDP")
    parser.add_argument('--num_participants', type=int, default=100000, help="number of participating clients")
    parser.add_argument('--mode', type=str, default='ffpa', help="mode: groundtruth || ffpa")
    parser.add_argument('--num_candidate', type=int, default=10, help="maximum candidates assigned to one client")
    parser.add_argument('--max_support', type=int, default=-1, help="force candidates to leave the pool after its support exceeds the threshold")
    
    # Settings
    parser.add_argument('--dataset', type=str, default='msnbc', help="msnbc || zipf || oldenburg")
    parser.add_argument('--duplicate', type=int, default=1, help="virtually duplicate the dataset")
    parser.add_argument('--min_length', type=int, default=3, help="minimal length of each trajectory")
    parser.add_argument('--max_length', type=int, default=None, help="maximal length of each trajectory")
    parser.add_argument('--verbose', action='store_true', help='verbose print')
    parser.add_argument('--process', type=int, default=0, help="number of worker processes, 0: single process")


    args = parser.parse_args()
    return args