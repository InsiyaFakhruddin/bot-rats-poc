def semantic_similarity(problem_vec, template_vec):
    # placeholder cosine similarity
    return sum(p * t for p, t in zip(problem_vec, template_vec))
