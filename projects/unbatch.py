import os
import shutil
import argparse

def get_batch_dirs(directory):
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            if dir.startswith('Batch_'):
                yield dir

parser = argparse.ArgumentParser()
parser.add_argument("directory")
args = parser.parse_args()

directory = args.directory

def unbatch_files(directory):
    for batch_dir in get_batch_dirs(directory):
        for file in os.listdir(os.path.join(directory, batch_dir)):
            shutil.move(os.path.join(directory, batch_dir, file), directory)
        os.rmdir(os.path.join(directory, batch_dir))

unbatch_files(directory)