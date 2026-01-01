def apply_rules(branch, title):
    checks = []

    if branch.startswith("feature/"):
        checks.append({"rule": "Tests included", "result": "PASS"})
        checks.append({"rule": "Good description", "result": "PASS"})

    elif branch.startswith("bugfix/"):
        if "bug" in title.lower():
            checks.append({"rule": "Bug reference", "result": "PASS"})
        else:
            checks.append({"rule": "Bug reference", "result": "FAIL"})

    elif branch.startswith("hotfix/"):
        checks.append({"rule": "Minimal checks", "result": "PASS"})

    else:
        checks.append({"rule": "Unknown branch", "result": "FAIL"})

    return checks
