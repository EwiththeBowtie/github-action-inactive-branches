import sys
from os import getenv
from typing import List




 # ignore_branches, last_commit_age_days, dry_run, github_token, github_base_url, github_repo, ignore_prefix = io.parse_input()


def parse_input() -> (list, int, bool, str, str, str, str):
    args: List[str] = sys.argv

    if len(args) != 7:
        input_string = ' '.join(args)
        expected_string = f'{args[0]} ignore_branches last_commit_age_days dry_run_yes_no github_token github_repo github_base_url'
        raise RuntimeError(f'Incorrect input: {input_string}. Expected: {expected_string}')

    branches_raw: str = args[1]
    ignore_branches = branches_raw.split(',')
    if ignore_branches == ['']:
        ignore_branches = []

    last_commit_age_days = int(args[2])

    # Dry run can only be either `true` or `false`, as strings due to github actions input limitations
    dry_run = False if args[3] == 'no' else True

    github_token = args[4]

    github_repo = getenv('GITHUB_REPOSITORY')


    github_base_url = args[5]

    ignore_prefix = args[6]

    return ignore_branches, last_commit_age_days, dry_run, github_token, github_base_url, github_repo, ignore_prefix


def format_output(output_strings: dict) -> None:
    for name, value in output_strings.items():
        print(f'::set-output name={name}::{value}')
