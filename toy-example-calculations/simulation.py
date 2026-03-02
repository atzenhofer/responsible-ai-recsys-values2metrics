import numpy as np
from src.metrics import epc, cr_gini, ca_eps, mwr, dri_ils
from src.data import TOTAL_USERS, ARCHIVES, USER_PROFILE

LINE_WIDTH = 70

def generate_rec_list(profile='popularity', n_items=10):
    """Generate synthetic recommendation list with given profile."""
    rec_list = []

    if profile == 'popularity':
        raters = np.random.power(0.5, size=n_items) * 450 + 20
        archives = np.random.choice(ARCHIVES, size=n_items, p=[0.70, 0.20, 0.10])
        sem = np.random.uniform(0.1, 0.6, size=n_items)
        meta = np.random.uniform(0.3, 0.9, size=n_items)
    elif profile == 'balanced':
        raters = np.random.randint(10, 250, size=n_items)
        archives = np.random.choice(ARCHIVES, size=n_items, p=[0.40, 0.30, 0.30])
        sem = np.random.normal(loc=USER_PROFILE['avg_sem']+0.15, scale=0.15, size=n_items)
        meta = np.random.normal(loc=USER_PROFILE['avg_meta'], scale=0.15, size=n_items)
    elif profile == 'relevance':
        raters = np.random.randint(50, 350, size=n_items)
        archives = np.random.choice(ARCHIVES, size=n_items, p=[0.60, 0.30, 0.10])
        sem = np.random.normal(loc=0.5, scale=0.1, size=n_items)
        meta = np.random.normal(loc=0.75, scale=0.1, size=n_items)
    else:
        raise ValueError(f"Unknown profile: {profile}")

    for i in range(n_items):
        rec_list.append({
            'pos': i + 1,
            'rel': 1,
            'archive': archives[i],
            'raters': int(np.clip(raters[i], 0, TOTAL_USERS)),
            'meta': float(np.clip(meta[i], 0, 1)),
            'sem': float(np.clip(sem[i], 0, 1))
        })

    if profile == 'popularity':
        rec_list.sort(key=lambda x: x['raters'], reverse=True)
        for i, item in enumerate(rec_list):
            item['pos'] = i + 1

    return rec_list


def run_simulation(n_trials=100):
    """Run n_trials and aggregate results."""
    profiles = ['popularity', 'balanced', 'relevance']
    labels = ['R1', 'R2', 'R3']
    results = {f'{key}_{label}': [] for key in ['RPQ', 'CR', 'CA', 'MWR', 'DRI'] for label in labels}

    for _ in range(n_trials):
        lists = {label: generate_rec_list(prof) for label, prof in zip(labels, profiles)}

        for label, rec in lists.items():
            results[f'RPQ_{label}'].append(epc(rec, TOTAL_USERS))
            results[f'CR_{label}'].append(cr_gini(rec, ARCHIVES))
            results[f'CA_{label}'].append(ca_eps(rec, USER_PROFILE))
            results[f'MWR_{label}'].append(mwr(rec))
            results[f'DRI_{label}'].append(dri_ils(rec))

    print(f"Simulation: {n_trials} trials (higher = better)")
    print(f"{'Metric':<15} {'R1_Mean':>12} {'R2_Mean':>12} {'R3_Mean':>12}")
    print("-" * LINE_WIDTH)

    metrics = ['RPQ (EPC)', 'CR (Gini)', 'CA (EPS)', 'MWR', 'DRI (ILS)']
    keys = ['RPQ', 'CR', 'CA', 'MWR', 'DRI']

    for metric, key in zip(metrics, keys):
        vals = [np.mean(results[f'{key}_{l}']) for l in labels]
        print(f"{metric:<15} {vals[0]:>12.4f} {vals[1]:>12.4f} {vals[2]:>12.4f}")


if __name__ == '__main__':
    run_simulation()
