import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("token", type=str, help="GitHub Access Token")
    parser.add_argument("organization", type=str, help="GitHub Organization")
    parser.add_argument("repo", type=str, help="GitHub Repository")

    args = parser.parse_args()
    return args


if __name__ ="__main__":
    args = parse_args()
    GitHub(args.token, args.organization, args.repo)