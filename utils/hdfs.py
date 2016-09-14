import os


def split_with_block(filenames: list, block_size=16*1024):
    splits = []
    for filename in filenames:
        FILE_SIZE = os.path.getsize(filename)
        block_sum = FILE_SIZE // block_size if FILE_SIZE % block_size == 0 else FILE_SIZE // block_size + 1
        for block_num in range(0, block_sum - 1):
            splits.append({'filename': filename,
                           'begin_at': block_num * block_size,
                           'end_at': (block_num + 1) * block_size})
        splits.append({'filename': filename,
                       'begin_at': (block_sum - 1) * block_size,
                       'end_at': FILE_SIZE - (block_sum - 1) * block_size})

    return splits


def split_with_line(filenames: list, block_size=16):
    splits = []
    for filename in filenames:
        read_size = 0
        with open(filename, 'r') as file:
            while True:
                data = file.readline()
                if not data:
                    break
                splits.append({'filename': filename,
                               'begin_at': read_size,
                               'end_at': read_size + len(data)})
                read_size += len(data)
    return splits
