"""Reproduces metric calculations from paper's toy example."""

from src.data import R1, R2, TOTAL_USERS, USER_PROFILE, ARCHIVES
from src.metrics import epc, cr_gini, ca_eps, mwr, dri_ils, csva, normalize_for_csva
from src.config import WEIGHT_SCENARIOS

LINE_WIDTH = 55

def main():
    print("=" * LINE_WIDTH)
    print("TOY EXAMPLE CALCULATIONS")
    print("=" * LINE_WIDTH)
    print()
    
    # Individual metrics
    print("Individual Metrics")
    print("-" * LINE_WIDTH)
    
    metrics = {
        'RPQ (EPC)': {'R1': epc(R1, TOTAL_USERS), 'R2': epc(R2, TOTAL_USERS)},
        'CR (Gini)': {'R1': cr_gini(R1, ARCHIVES), 'R2': cr_gini(R2, ARCHIVES)},
        'CA (EPS)': {'R1': ca_eps(R1, USER_PROFILE), 'R2': ca_eps(R2, USER_PROFILE)},
        'MWR': {'R1': mwr(R1), 'R2': mwr(R2)},
        'DRI (ILS)': {'R1': dri_ils(R1), 'R2': dri_ils(R2)},
    }
    
    print(f"{'Metric':<15} {'R1':>10} {'R2':>10} {'Winner':>10}")
    print("-" * LINE_WIDTH)
    
    for name, values in metrics.items():
        r1, r2 = values['R1'], values['R2']
        winner = 'R2' if r2 > r1 else 'R1'
        print(f"{name:<15} {r1:>10.4f} {r2:>10.4f} {winner:>10}")
    
    print()
    
    # CSVA with z-score normalization
    print("CSVA (Z-Score Normalization)")
    print("-" * LINE_WIDTH)
    
    normalized = normalize_for_csva(metrics, strategy='zscore')
    
    print(f"{'Scenario':<15} {'R1':>10} {'R2':>10} {'Improvement':>15}")
    print("-" * LINE_WIDTH)
    
    for name, weights in WEIGHT_SCENARIOS.items():
        csva_r1 = csva({k: normalized[k]['R1'] for k in weights}, weights)
        csva_r2 = csva({k: normalized[k]['R2'] for k in weights}, weights)
        improvement = ((csva_r2 / csva_r1 - 1) * 100) if csva_r1 > 0 else 0
        print(f"{name.title():<15} {csva_r1:>10.4f} {csva_r2:>10.4f} {f'+{improvement:.1f}%':>15}")
    
    print()


if __name__ == "__main__":
    main()
