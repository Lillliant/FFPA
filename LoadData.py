from models.DataSet import Itemset, ItemDataSet
import pickle

"""
Structure
Dataset -> DataSet.ItemDataSet
            # The list of items in the domain
            self.points = points 
            # The list of transactions, each transaction is a list of items in DataSet.Itemset format
            self.record = [] 
Transaction -> DataSet.Itemset
            # The list of unique items in the transaction
            self.data = set(data) 
            # The length of the transaction (i.e., number of elements)
            self.data_length = len(data) 
"""

def loadDataSet(data_path: str, name: str, output_dir: str):
    records = []
    items = set()
    print("Loading data...")
    with open(data_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            transaction = list(map(int, line.strip().split()))
            items.update(transaction)
            records.append(transaction)
    print("Converting to FedFPM format...")
    dataset = ItemDataSet(list(items))
    for record in records:
        transaction = Itemset(record)
        dataset.add_line(transaction)
    print(f"Saving data to {output_dir}/{name}.pickle...")
    with open(f'{output_dir}/{name}.pickle', 'wb') as f:
        pickle.dump(dataset, f)
    print("Data saved successfully.")

if __name__ == "__main__":
    dataset = 't25i10d10k' # 't25i10d10k' or 'retail'
    data_dir = f'./raw/{dataset}.txt'
    output_dir = './data'
    loadDataSet(data_dir, dataset, output_dir)