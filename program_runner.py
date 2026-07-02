import io
import contextlib
import matplotlib.pyplot as plt

def run_program(path):
    output = io.StringIO()

    figures_before = len(plt.get_fignums())

    try:
        with contextlib.redirect_stdout(output):
            namespace = {}
            exec(open(path, encoding="utf-8").read(), namespace)

        figures = []

        for num in plt.get_fignums():
            figures.append(plt.figure(num))

        return {
            "text": output.getvalue(),
            "figures": figures,
            "error": None
        }

    except Exception as e:
        return {
            "text": "",
            "figures": [],
            "error": str(e)
        }

import re

def patch_input_calls(source, user_inputs):
    def replacement(match):
        prompt_content = match.group(1) or ""
        prompt_clean = re.sub(r"['\"]", "", prompt_content).lower()
        
        for key, value in user_inputs.items():
            if key and key.lower() in prompt_clean:
                return f'"{value}"'
                
        if "" in user_inputs:
            return f'"{user_inputs[""]}"'
        if user_inputs:
            return f'"{list(user_inputs.values())[0]}"'
        return '""'

    pattern = r'input\s*\(\s*(.*?)\s*\)'
    return re.sub(pattern, replacement, source)