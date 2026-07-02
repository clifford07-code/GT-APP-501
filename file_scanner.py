import os
import re

def scan_experiments(base_dir):
    experiments = {}

    for file in os.listdir(base_dir):
        if file.endswith(".py"):
            match = re.match(r"exp(\d+)(?:-(\d+))?\.py", file)

            if match:
                exp_num = int(match.group(1))
                prog_num = int(match.group(2) or 1)

                if exp_num not in experiments:
                    experiments[exp_num] = {"files": {}}

                experiments[exp_num]["files"][prog_num] = os.path.join(base_dir, file)

    return dict(sorted(experiments.items()))