import argparse
import random
import string
import tqdm

import pandas as pd


def parse_args():
    parser = argparse.ArgumentParser(description='Generate examples')
    parser.add_argument('--N', type=int, help='Number of examples to generate')
    parser.add_argument('--M', type=int, help='Vocabulary size')
    parser.add_argument('--K', type=int, help='Maximum length of a sequence')
    parser.add_argument('--path', type=str, help='Path to store the resulting dataframe')
    return parser.parse_args()


def main():
    args = parse_args()
    N = args.N
    M = args.M
    K = args.K
    path = args.path

    vocabulary = [''.join(random.choices(string.ascii_lowercase, k=10))
                  for _ in range(M)]

    examples = []
    for i in tqdm.tqdm(range(N)):
        n_elements = random.randint(1, K)
        examples.append({"id": i,
                         "elements_1": set(random.choices(vocabulary, k=n_elements)),
                         "elements_2": set(random.choices(vocabulary, k=n_elements)),
                         })
    df_examples = pd.DataFrame(examples)

    df_examples.to_parquet(path=path, index=False)


if __name__ == '__main__':
    main()
