# Generate Ground Truth
python main.py --dataset=t25i10d10k --verbose --mode=groundtruth --k=900  --process=1 --xi=0.01 --num_candidate=1 --num_participants=1000000 --epsilon=7 --max_support=100000

# FFPA Comparison (Best)
python main.py --dataset=t25i10d10k --verbose --mode=ffpa --k=900  --process=1 --xi=0.01 --num_candidate=1 --num_participants=1000000 --epsilon=7 --max_support=100000