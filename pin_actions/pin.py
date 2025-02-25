import os
import re
import requests
import yaml
import click

GITHUB_API_URL = "https://api.github.com/repos/{owner}/{repo}/git/refs/tags/{branch}"

def get_pinned_sha(repo, version):
    """Fetch the SHA for a given GitHub Action."""
    owner, repo_name = repo.split('/')
    url = GITHUB_API_URL.format(owner=owner, repo=repo_name, branch=version)
    print("🔄 Fetching SHA for %s@%s", repo, version)
    print(url)

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["object"]["sha"]
    print(f"⚠️ Failed to fetch SHA for {repo}@{version} ({response.status_code})")
    return None

def replace_unpinned_actions(file_path):
    """Replace unpinned actions in a workflow file with pinned SHAs."""
    with open(file_path, 'r') as file:
        content = file.read()

    updated_content = content
    actions = re.findall(r'([\w-]+/[\w-]+)@([\w.-]+)', content)

    for repo, version in actions:
        if not re.match(r'^[a-f0-9]{40}$', version):  # Ignore pinned actions
            sha = get_pinned_sha(repo, version)
            if sha:
                updated_content = updated_content.replace(f"{repo}@{version}", f"{repo}@{sha}")

    if updated_content != content:
        with open(file_path, 'w') as file:
            file.write(updated_content)
        print(f"✅ Updated {file_path}")
    else:
        print(f"🔹 No changes needed for {file_path}")

@click.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False))
def pin_actions(directory):
    """CLI to pin GitHub Actions dependencies in workflows."""
    workflow_dir = os.path.join(directory, ".github/workflows")

    if not os.path.exists(workflow_dir):
        print("❌ No workflow directory found.")
        return

    for filename in os.listdir(workflow_dir):
        if filename.endswith(('.yml', '.yaml')):
            replace_unpinned_actions(os.path.join(workflow_dir, filename))

if __name__ == "__main__":
    pin_actions()
