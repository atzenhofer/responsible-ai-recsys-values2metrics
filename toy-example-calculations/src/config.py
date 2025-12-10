"""Stakeholder weight configurations and normalization strategies."""

WEIGHTS_CONSUMER = {
    'RPQ (EPC)': 0.35,
    'CA (EPS)': 0.25,
    'DRI (ILS)': 0.15,
    'CR (Gini)': 0.10,
    'MWR': 0.10,
}

WEIGHTS_PROVIDER = {
    'CR (Gini)': 0.40,
    'MWR': 0.30,
    'DRI (ILS)': 0.15,
    'RPQ (EPC)': 0.10,
    'CA (EPS)': 0.05,
}

WEIGHTS_BALANCED = {
    'RPQ (EPC)': 0.20,
    'CR (Gini)': 0.20,
    'CA (EPS)': 0.20,
    'MWR': 0.20,
    'DRI (ILS)': 0.20,
}

WEIGHT_SCENARIOS = {
    'consumer': WEIGHTS_CONSUMER,
    'provider': WEIGHTS_PROVIDER,
    'balanced': WEIGHTS_BALANCED,
}

NORMALIZATION_STRATEGIES = ['minmax', 'zscore', 'rank', 'softmax', 'percentile']
