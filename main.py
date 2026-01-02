from meta_buffer.templates import ThoughtTemplate
from retrieval.scoring import final_score
from retrieval.structural_matcher import structural_fit

template = ThoughtTemplate(
    name="QuadraticSolver",
    description="Solve quadratic equations",
    structure_type="equation"
)

problem = {
    "structure": "equation",
    "embedding": [0.25, 0.45, 0.15]
}

semantic = 0.92
structural = structural_fit(problem["structure"], template.structure_type)
constraint = 0.8

score = final_score(semantic, structural, constraint)
print("Template score:", score)
