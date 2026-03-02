from src.data import R1, R2, R3, TOTAL_USERS, USER_PROFILE, ARCHIVES
from src.metrics import epc, cr_gini, ca_eps, mwr, dri_ils, csva, normalize_for_csva
from src.config import WEIGHT_SCENARIOS

LINE_WIDTH = 70

def main():
    print("=" * LINE_WIDTH)
    print("TOY EXAMPLE CALCULATIONS")
    print("=" * LINE_WIDTH)
    print()

    systems = {'R1': R1, 'R2': R2, 'R3': R3}

    print("Individual Metrics (higher = better)")
    print("-" * LINE_WIDTH)

    metrics = {
        'RPQ (EPC)': {s: epc(R, TOTAL_USERS) for s, R in systems.items()},
        'CR (Gini)': {s: cr_gini(R, ARCHIVES) for s, R in systems.items()},
        'CA (EPS)': {s: ca_eps(R, USER_PROFILE) for s, R in systems.items()},
        'MWR': {s: mwr(R) for s, R in systems.items()},
        'DRI (ILS)': {s: dri_ils(R) for s, R in systems.items()},
    }

    print(f"{'Metric':<15} {'R1':>10} {'R2':>10} {'R3':>10} {'Winner':>10}")
    print("-" * LINE_WIDTH)

    for name, values in metrics.items():
        winner = max(values, key=values.get)
        vals = [f"{values[s]:>10.4f}" for s in systems]
        print(f"{name:<15} {''.join(vals)} {winner:>10}")

    print()

    print("CSVA (Z-Score Normalization, higher = better)")
    print("-" * LINE_WIDTH)

    normalized = normalize_for_csva(metrics, strategy='zscore')

    print(f"{'Scenario':<15} {'R1':>10} {'R2':>10} {'R3':>10} {'Winner':>10}")
    print("-" * LINE_WIDTH)

    for name, weights in WEIGHT_SCENARIOS.items():
        results = {}
        for s in systems:
            results[s] = csva({k: normalized[k][s] for k in weights}, weights)
        winner = max(results, key=results.get)
        vals = [f"{results[s]:>10.4f}" for s in systems]
        print(f"{name.title():<15} {''.join(vals)} {winner:>10}")

    print()


if __name__ == "__main__":
    main()
