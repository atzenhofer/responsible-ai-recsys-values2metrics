"""Fixed data for toy example: R1 (popularity-based) vs R2 (balanced)."""

TOTAL_USERS = 1000
ARCHIVES = ['A', 'B', 'C']

ARCHIVE_NAMES = {
    'A': 'AT-HHStA (Vienna, Austria)',
    'B': 'DE-BayHStA (Munich, Germany)',
    'C': 'IT-ASFi (Florence, Italy)',
}

USER_PROFILE = {
    'avg_sem': 0.4,  # Average semantic similarity of user's profile
    'avg_meta': 0.7,  # Average metadata quality
}

# R1: Popularity-based (archetypal)
# Ranked by descending access count, concentrated on Archive A (70%)
R1 = [
    {'pos': 1, 'rel': 1, 'archive': 'A', 'raters': 450, 'meta': 0.9, 'sem': 0.3},
    {'pos': 2, 'rel': 1, 'archive': 'A', 'raters': 400, 'meta': 0.8, 'sem': 0.2},
    {'pos': 3, 'rel': 1, 'archive': 'B', 'raters': 350, 'meta': 0.9, 'sem': 0.4},
    {'pos': 4, 'rel': 1, 'archive': 'A', 'raters': 300, 'meta': 0.7, 'sem': 0.3},
    {'pos': 5, 'rel': 0, 'archive': 'A', 'raters': 250, 'meta': 0.8, 'sem': 0.2},
    {'pos': 6, 'rel': 1, 'archive': 'B', 'raters': 200, 'meta': 0.6, 'sem': 0.5},
    {'pos': 7, 'rel': 1, 'archive': 'A', 'raters': 150, 'meta': 0.5, 'sem': 0.4},
    {'pos': 8, 'rel': 0, 'archive': 'A', 'raters': 100, 'meta': 0.4, 'sem': 0.3},
    {'pos': 9, 'rel': 0, 'archive': 'C', 'raters': 50, 'meta': 0.3, 'sem': 0.6},
    {'pos': 10, 'rel': 0, 'archive': 'C', 'raters': 25, 'meta': 0.2, 'sem': 0.7},
]

# R2: Balanced multistakeholder (archetypal)
# Inverts popularity bias, balanced archives (40% A, 20% B, 40% C)
R2 = [
    {'pos': 1, 'rel': 1, 'archive': 'C', 'raters': 15, 'meta': 0.6, 'sem': 0.8},
    {'pos': 2, 'rel': 1, 'archive': 'C', 'raters': 20, 'meta': 0.7, 'sem': 0.7},
    {'pos': 3, 'rel': 1, 'archive': 'A', 'raters': 50, 'meta': 0.8, 'sem': 0.6},
    {'pos': 4, 'rel': 1, 'archive': 'B', 'raters': 100, 'meta': 0.9, 'sem': 0.5},
    {'pos': 5, 'rel': 1, 'archive': 'A', 'raters': 200, 'meta': 0.8, 'sem': 0.4},
    {'pos': 6, 'rel': 1, 'archive': 'B', 'raters': 250, 'meta': 0.7, 'sem': 0.6},
    {'pos': 7, 'rel': 0, 'archive': 'A', 'raters': 300, 'meta': 0.9, 'sem': 0.3},
    {'pos': 8, 'rel': 1, 'archive': 'C', 'raters': 25, 'meta': 0.5, 'sem': 0.7},
    {'pos': 9, 'rel': 0, 'archive': 'A', 'raters': 400, 'meta': 0.8, 'sem': 0.2},
    {'pos': 10, 'rel': 0, 'archive': 'C', 'raters': 15, 'meta': 0.4, 'sem': 0.8},
]
