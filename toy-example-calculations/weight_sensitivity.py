from src.data import R1, R2, R3, TOTAL_USERS, USER_PROFILE, ARCHIVES
from src.metrics import epc, cr_gini, ca_eps, mwr, dri_ils, csva, normalize_for_csva

LINE_WIDTH = 70

def main():
    systems = {'R1': R1, 'R2': R2, 'R3': R3}

    metrics = {
        'RPQ (EPC)': {s: epc(R, TOTAL_USERS) for s, R in systems.items()},
        'CR (Gini)': {s: cr_gini(R, ARCHIVES) for s, R in systems.items()},
        'CA (EPS)': {s: ca_eps(R, USER_PROFILE) for s, R in systems.items()},
        'MWR': {s: mwr(R) for s, R in systems.items()},
        'DRI (ILS)': {s: dri_ils(R) for s, R in systems.items()},
    }

    normalized = normalize_for_csva(metrics, strategy='zscore')

    original_weights = {
        'Consumer': {'RPQ (EPC)': 0.35, 'CA (EPS)': 0.25, 'DRI (ILS)': 0.15, 'CR (Gini)': 0.15, 'MWR': 0.10},
        'Provider': {'CR (Gini)': 0.40, 'MWR': 0.30, 'DRI (ILS)': 0.15, 'RPQ (EPC)': 0.10, 'CA (EPS)': 0.05},
        'Balanced': {'RPQ (EPC)': 0.20, 'CR (Gini)': 0.20, 'CA (EPS)': 0.20, 'MWR': 0.20, 'DRI (ILS)': 0.20},
    }

    print("Original Weights (higher = better)")
    print(f"{'Scenario':<12} {'R1':>10} {'R2':>10} {'R3':>10} {'Winner':>10}")
    print("-" * LINE_WIDTH)

    for name, weights in original_weights.items():
        results = {s: csva({k: normalized[k][s] for k in weights}, weights) for s in systems}
        winner = max(results, key=results.get)
        print(f"{name:<12} {results['R1']:>10.4f} {results['R2']:>10.4f} {results['R3']:>10.4f} {winner:>10}")

    print()
    print("Consumer Weight Variations (±10%)")
    print(f"{'Variation':<12} {'R1':>10} {'R2':>10} {'R3':>10} {'Winner':>10}")
    print("-" * LINE_WIDTH)

    consumer_base = original_weights['Consumer']
    variations = [
        {'name': 'RPQ+10%', 'weights': {**consumer_base, 'RPQ (EPC)': 0.45, 'MWR': 0.00}},
        {'name': 'CA+10%', 'weights': {**consumer_base, 'CA (EPS)': 0.35, 'MWR': 0.00}},
        {'name': 'DRI+10%', 'weights': {**consumer_base, 'DRI (ILS)': 0.25, 'MWR': 0.00}},
        {'name': 'CR+10%', 'weights': {**consumer_base, 'CR (Gini)': 0.25, 'MWR': 0.00}},
    ]

    for var in variations:
        results = {s: csva({k: normalized[k][s] for k in var['weights']}, var['weights']) for s in systems}
        winner = max(results, key=results.get)
        print(f"{var['name']:<12} {results['R1']:>10.4f} {results['R2']:>10.4f} {results['R3']:>10.4f} {winner:>10}")


if __name__ == "__main__":
    main()
