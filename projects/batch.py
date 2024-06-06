import os
import shutil
import argparse

def batch_files(directory, batch_size):
    files = os.listdir(directory)
    for i in range(0, len(files), batch_size):
        yield files[i:i + batch_size]

parser = argparse.ArgumentParser()
parser.add_argument("directory")
parser.add_argument("batch_size", type=int)
args = parser.parse_args()

directory = args.directory
batch_size = args.batch_size

def create_batches(batch_files, directory, batch_size):
    for i, batch in enumerate(batch_files(directory, batch_size), 1):
        new_dir = os.path.join(directory, f'Batch_{i}')
        os.makedirs(new_dir, exist_ok=True)
        for file in batch:
            shutil.move(os.path.join(directory, file), new_dir)

create_batches(batch_files, directory, batch_size)

