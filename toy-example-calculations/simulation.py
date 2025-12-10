"""Robustness testing: validates metrics with random trials."""

import numpy as np
from src.metrics import epc, cr_gini, ca_eps, mwr, dri_ils
from src.data import TOTAL_USERS, ARCHIVES, USER_PROFILE

LINE_WIDTH = 55

def generate_rec_list(profile='popularity', n_items=10):
    """Generate synthetic recommendation list with given profile."""
    rec_list = []
    
    if profile == 'popularity':
        # Popularity-based: skewed archives, low coherence
        raters = np.random.power(0.5, size=n_items) * 450 + 20
        archives = np.random.choice(ARCHIVES, size=n_items, p=[0.70, 0.20, 0.10])
        sem = np.random.uniform(0.1, 0.6, size=n_items)
        meta = np.random.uniform(0.3, 0.9, size=n_items)
    elif profile == 'balanced':
        # Balanced: uniform popularity, high coherence
        raters = np.random.randint(10, 250, size=n_items)
        archives = np.random.choice(ARCHIVES, size=n_items, p=[0.40, 0.30, 0.30])
        sem = np.random.normal(loc=USER_PROFILE['avg_sem']+0.15, scale=0.15, size=n_items)
        meta = np.random.normal(loc=USER_PROFILE['avg_meta'], scale=0.15, size=n_items)
    else:
        raise ValueError(f"Unknown profile: {profile}")

    for i in range(n_items):
        rec_list.append({
            'pos': i + 1,
            'rel': 1,
            'archive': archives[i],
            'raters': int(np.clip(raters[i], 0, TOTAL_USERS)),
            'meta': np.clip(meta[i], 0, 1),
            'sem': np.clip(sem[i], 0, 1)
        })
    
    if profile == 'popularity':
        rec_list.sort(key=lambda x: x['raters'], reverse=True)
        for i, item in enumerate(rec_list):
            item['pos'] = i + 1

    return rec_list


def run_simulation(n_trials=100):
    """Run n_trials and aggregate results."""
    results = {
        'RPQ_R1': [], 'RPQ_R2': [],
        'CR_R1': [], 'CR_R2': [],
        'CA_R1': [], 'CA_R2': [],
        'MWR_R1': [], 'MWR_R2': [],
        'DRI_R1': [], 'DRI_R2': [],
    }

    for _ in range(n_trials):
        r1_sim = generate_rec_list('popularity')
        r2_sim = generate_rec_list('balanced')
        
        results['RPQ_R1'].append(epc(r1_sim, TOTAL_USERS))
        results['RPQ_R2'].append(epc(r2_sim, TOTAL_USERS))
        results['CR_R1'].append(cr_gini(r1_sim, ARCHIVES))
        results['CR_R2'].append(cr_gini(r2_sim, ARCHIVES))
        results['CA_R1'].append(ca_eps(r1_sim, USER_PROFILE))
        results['CA_R2'].append(ca_eps(r2_sim, USER_PROFILE))
        results['MWR_R1'].append(mwr(r1_sim))
        results['MWR_R2'].append(mwr(r2_sim))
        results['DRI_R1'].append(dri_ils(r1_sim))
        results['DRI_R2'].append(dri_ils(r2_sim))
    
    print(f"Simulation: {n_trials} trials")
    print(f"{'Metric':<15} {'R1_Mean':>12} {'R2_Mean':>12}")
    print("-" * LINE_WIDTH)
    
    metrics = ['RPQ (EPC)', 'CR (Gini)', 'CA (EPS)', 'MWR', 'DRI (ILS)']
    keys = ['RPQ', 'CR', 'CA', 'MWR', 'DRI']
    
    for metric, key in zip(metrics, keys):
        r1_mean = np.mean(results[f'{key}_R1'])
        r2_mean = np.mean(results[f'{key}_R2'])
        print(f"{metric:<15} {r1_mean:>12.4f} {r2_mean:>12.4f}")


if __name__ == '__main__':
    run_simulation()
