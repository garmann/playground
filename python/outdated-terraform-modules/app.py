import os
import sys
import json

import gitlab


""" DESCRIPTION
this script will output outdated terraform modules 
in your terraform code, by scanning gitlab tags and your local filesystem

simplified workflow:
- get latest tags from gitlab for all projects in a specific group (terraform mods group)
- get used tags from *.tf and *.tfvars files looking for the "sources" attribute
- compare all tags and output which versions are not up-to-date

limitations:
- runs with currently only one tag scheme => v0.0.0
- tags with v1.2.3-rc/hotfix and other are not fully working
"""

# gitlab
URL = "http://foobar"
GITLAB_GROUP_TF_MODS = "foobar"
PRIVATE_TOKEN = "foobar"

# local file system scan
SCAN_DIR = [
    "foobar",
]
BLACKLIST_DIRS = [
    ".terragrunt-cache",
    ".git",
]
WHITELIST_FILE_EXTENSION = [
    ".tf",
    ".tfvars"
]
TF_SOURCE_SEARCH_PATTERN = '"git::ssh://git@gitlab.foobar'


def convert_tag(tagname: str) -> int:
    try:
        if tagname[0] == 'v':
            tagname = tagname[1:]
    except TypeError:
        return 0

    tagname = tagname.replace(".", "")

    try:
        tagname = int(tagname)
    except ValueError:
        return None

    return tagname


def find_highest_tag(tag_list: list) -> str:
    """ decided to go just with tag numbers, name will be stripped to compare it
    not looking at tag creation date from gitlab, one might push a lot stuff to test tags
    """
    highest_tag = None
    return_tag = None

    for tag in tag_list:
        clean_tag = convert_tag(tag)

        if clean_tag is None:
            continue

        if not highest_tag:
            highest_tag = clean_tag
            return_tag = tag
        else:
            if clean_tag > highest_tag:
                highest_tag = clean_tag
                return_tag = tag

    return return_tag


def gitlab_terraform_modules_taglist() -> list:
    """ gets all projects from terraform group to acquire current tags on our tf-mods
    """
    gl = gitlab.Gitlab(URL, PRIVATE_TOKEN, ssl_verify=False)
    # test connection
    try:
        if gl.projects.list():
            pass
    except Exception:
        print("could not reach gitlab")
        sys.exit(1)

    terraform_group = None
    for group in gl.groups.list(all=True):
        if group.name == GITLAB_GROUP_TF_MODS:
            terraform_group = group

    terraform_modules_latest_tags = {}
    for tfmod_project in terraform_group.projects.list(all=True):
        project = gl.projects.get(tfmod_project.id)
        tag_list = [tag.name for tag in project.tags.list()]
        highest_tag = find_highest_tag(tag_list)

        if highest_tag is not None:
            terraform_modules_latest_tags[project.name] = highest_tag

    return terraform_modules_latest_tags


def is_blacklist_dir(directory: str) -> bool:
    for blacklist_string in BLACKLIST_DIRS:
        if blacklist_string in directory:
            return True

    return False


def is_whitelist_file(filepath: str) -> bool:
    for whitelist_string in WHITELIST_FILE_EXTENSION:
        if whitelist_string == os.path.splitext(filepath)[1]:
            return True

    return False


def get_terraform_files() -> list:
    """ looks for possible files which include sources to terraform mods
    """
    terraform_files = []
    for dir in SCAN_DIR:
        for root, _, files in os.walk(dir, topdown=False):
            if is_blacklist_dir(root):
                continue

            for file in files:
                if is_whitelist_file(file):
                    filepath = root + "/" + file
                    terraform_files.append(filepath)

    return terraform_files


def get_terraform_sources_from_file(file: str) -> list:
    """ returns empty list or any tf mod sources as lines if in file
    """
    filecontent = []
    with open(file, 'r') as fh:
        filecontent = fh.readlines()

    sources_in_file = []
    for line in filecontent:

        if TF_SOURCE_SEARCH_PATTERN in line \
                and "source" in line \
                and "#" not in line:

            sources_in_file.append(line.rstrip())

    return sources_in_file


def extract_tag(source: str) -> str:
    try:
        return source.split("ref=")[1].split('"')[0]
    except IndexError:
        return '0'


def main():
    hightest_tags = gitlab_terraform_modules_taglist()

    output = []
    """ layout:
    [
        {
            'tfmod': 'xxx',
            'data': {
                'highest': 'xxx'
                'outdated': [
                    {
                        'path': 'xxx'
                        'source': 'xxx'
                        'tag': 'xxx'
                    }
                ]
            }
        }
    ]
    """

    for tfmod in hightest_tags:
        output.append({
            "tfmod": tfmod,
            "data": {
                "highest": hightest_tags[tfmod],
                "outdated": [],
            }
        })

    tf_files = get_terraform_files()
    for file in tf_files:
        for source_in_file in get_terraform_sources_from_file(file):
            tag = extract_tag(source_in_file)
            terraform_module_name = source_in_file.split(
                ".git")[0].split("/")[-1:][0]

            if terraform_module_name not in hightest_tags:
                print(f"Warning {terraform_module_name} still used with non valid tag or project in {file}")
                continue

            # go through prepared output list and fill in more data
            if tag != hightest_tags[terraform_module_name]:
                for tf_module_name in output:
                    if tf_module_name['tfmod'] == terraform_module_name:
                        tf_module_name['data']['outdated'].append({
                            'path': file,
                            'source': source_in_file,
                            'tag': tag,
                        })

    print(json.dumps(output))


if __name__ == "__main__":
    main()
