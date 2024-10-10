import re
import sys

COMMIT_MSG_PATTERN = r"^DJ-\d{1,6}: .+"

def check_commit_msg(commit_msg):
    with open(commit_msg, 'r') as file:
        message = file.read().strip()
    if not re.match(COMMIT_MSG_PATTERN, message):
        print(f"Commit message does not match the required format: {message}")
        print("Expected format: DJ-<TASK_NUMBER>: <COMMIT_MESSAGE>")
        sys.exit(1)

if __name__ == "__main__":
    check_commit_msg(sys.argv[1])
