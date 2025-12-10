"""Weight sensitivity analysis: tests ±10% variations in CSVA weights."""

from src.data import R1, R2, TOTAL_USERS, USER_PROFILE, ARCHIVES
from src.metrics import epc, cr_gini, ca_eps, mwr, dri_ils, csva, normalize_for_csva

LINE_WIDTH = 55

def main():
    metrics = {
        'RPQ (EPC)': {'R1': epc(R1, TOTAL_USERS), 'R2': epc(R2, TOTAL_USERS)},
        'CR (Gini)': {'R1': cr_gini(R1, ARCHIVES), 'R2': cr_gini(R2, ARCHIVES)},
        'CA (EPS)': {'R1': ca_eps(R1, USER_PROFILE), 'R2': ca_eps(R2, USER_PROFILE)},
        'MWR': {'R1': mwr(R1), 'R2': mwr(R2)},
        'DRI (ILS)': {'R1': dri_ils(R1), 'R2': dri_ils(R2)},
    }
    
    normalized = normalize_for_csva(metrics, strategy='zscore')
    
    original_weights = {
        'Consumer': {'RPQ (EPC)': 0.35, 'CA (EPS)': 0.25, 'DRI (ILS)': 0.15, 'CR (Gini)': 0.10, 'MWR': 0.10},
        'Provider': {'CR (Gini)': 0.40, 'MWR': 0.30, 'DRI (ILS)': 0.15, 'RPQ (EPC)': 0.10, 'CA (EPS)': 0.05},
    }
    
    print("Original Weights")
    print(f"{'Scenario':<12} {'R1':>10} {'R2':>10} {'Improvement':>15}")
    print("-" * LINE_WIDTH)
    
    for name, weights in original_weights.items():
        r1_score = csva({k: normalized[k]['R1'] for k in weights}, weights)
        r2_score = csva({k: normalized[k]['R2'] for k in weights}, weights)
        improvement = ((r2_score / r1_score - 1) * 100) if r1_score > 0 else 0
        print(f"{name:<12} {r1_score:>10.4f} {r2_score:>10.4f} {improvement:>14.1f}%")
    
    print()
    print("Consumer Weight Variations (±10%)")
    print(f"{'Variation':<12} {'R1':>10} {'R2':>10} {'Improvement':>15}")
    print("-" * LINE_WIDTH)
    
    consumer_base = original_weights['Consumer']
    variations = [
        {'name': 'RPQ+10%', 'weights': {**consumer_base, 'RPQ (EPC)': 0.45, 'MWR': 0.05}},
        {'name': 'CA+10%', 'weights': {**consumer_base, 'CA (EPS)': 0.35, 'MWR': 0.05}},
        {'name': 'DRI+10%', 'weights': {**consumer_base, 'DRI (ILS)': 0.25, 'MWR': 0.05}},
    ]
    
    for var in variations:
        r1_score = csva({k: normalized[k]['R1'] for k in var['weights']}, var['weights'])
        r2_score = csva({k: normalized[k]['R2'] for k in var['weights']}, var['weights'])
        improvement = ((r2_score / r1_score - 1) * 100) if r1_score > 0 else 0
        print(f"{var['name']:<12} {r1_score:>10.4f} {r2_score:>10.4f} {improvement:>14.1f}%")


if __name__ == "__main__":
    main()
