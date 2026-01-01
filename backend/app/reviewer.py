from .rules import apply_rules

def generate_review(branch, title):
    return {
        "branch": branch,
        "checks": apply_rules(branch, title),
        "decision": "PENDING_APPROVAL"
    }
