def distill_problem(problem_text):
    return {
        "structure": "equation",
        "constraints": ["solve", "optimize"],
        "embedding": [0.2, 0.5, 0.1]
    }
