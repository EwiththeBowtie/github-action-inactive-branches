from src import actions, io

if __name__ == '__main__':
    ignore_branches, last_commit_age_days, dry_run, github_token, github_base_url, github_repo, ignore_prefix = io.parse_input()
    print(ignore_prefix)
    print(ignore_branches)
    print(last_commit_age_days)
    print(dry_run)
    print(github_token)
    print(github_base_url)
    print(github_repo)
    deleted_branches = actions.run_action(
        ignore_branches=ignore_branches,
        last_commit_age_days=last_commit_age_days,
        dry_run=dry_run,
        github_repo=github_repo,
        github_token=github_token,
        github_base_url=github_base_url,
        ignore_prefix=ignore_prefix
    )

    io.format_output({'deleted_branches': deleted_branches})
