import os
import argparse

import requests
import git


def clone_repo(clone_url, clone_dest: str):
    if not os.path.exists(clone_dest):
        git.Repo.clone_from(clone_url, clone_dest)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="arguments for github repo downloader")
    parser.add_argument("--username", type=str, help="github username", required=True)
    parser.add_argument(
        "--dest",
        type=str,
        help="local path to save repos, github username and repo name is already included in the script",
        required=False,
    )

    parser.add_argument(
        "--fork",
        type=str,
        default="yes",
        help="choose no to skip downloading forks",
        required=False,
    )

    args = parser.parse_args()

    api_url = "https://api.github.com"
    profile_url = f"{api_url}/users/{args.username}/repos?per_page=1000"

    for repo in requests.get(profile_url).json():
        if args.fork == "no" and repo["fork"] is True:
            continue

        print(repo["full_name"])
        if not args.dest:
            clone_repo(repo["clone_url"], args.username + "/" + repo["name"])
        else:
            clone_repo(
                repo["clone_url"], args.dest + "/" + args.username + "/" + repo["name"]
            )
