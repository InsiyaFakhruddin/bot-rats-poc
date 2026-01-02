def final_score(semantic, structural, constraint, alpha=0.5, beta=0.3, gamma=0.2):
    return alpha * semantic + beta * structural + gamma * constraint
