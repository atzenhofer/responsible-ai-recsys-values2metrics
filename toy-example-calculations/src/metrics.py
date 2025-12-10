"""Metric implementations following paper's formulations."""

import math
import numpy as np
from typing import List, Dict, Callable


def disc_log(k: int) -> float:
    """Logarithmic rank discount: disc(k) = 1 / log_2(k + 1)."""
    return 1.0 / math.log2(k + 1)


def p_rel(item: Dict, tau: float = 0.0, g_max: int = 1) -> float:
    """Relevance probability. Binary relevance in toy example."""
    return float(item['rel'])


def p_seen(item: Dict, total_users: int) -> float:
    """Probability item has been seen: p(seen|i) = raters / total_users."""
    return item['raters'] / total_users


def epc(rec_list: List[Dict], 
        total_users: int,
        disc_func: Callable[[int], float] = disc_log,
        use_relevance: bool = True,
        use_rank: bool = True) -> float:
    """Expected Popularity Complement (EPC) for Research Path Quality."""
    score = 0.0
    normalizer = 0.0
    
    for item in rec_list:
        k = item['pos']
        discount = disc_func(k) if use_rank else 1.0
        relevance = p_rel(item) if use_relevance else 1.0
        novelty = 1.0 - p_seen(item, total_users)
        
        score += discount * relevance * novelty
        normalizer += discount
    
    return score / normalizer if normalizer > 0 else 0.0


def cr_gini(rec_list: List[Dict], archives: List[str]) -> float:
    """Collection Representation via Gini coefficient."""
    archive_counts = {archive: 0 for archive in archives}
    for item in rec_list:
        archive_counts[item['archive']] += 1
    
    counts = list(archive_counts.values())
    n = len(counts)
    
    if n == 0 or sum(counts) == 0:
        return 0.0
    
    total_recs = sum(counts)
    sum_abs_diff = sum(abs(counts[i] - counts[j]) 
                      for i in range(n) 
                      for j in range(n))
    
    gini = sum_abs_diff / (2 * n * total_recs)
    return 1.0 - gini


def ca_eps(rec_list: List[Dict],
           user_profile: Dict,
           disc_func: Callable[[int], float] = disc_log,
           use_relevance: bool = True,
           use_rank: bool = True) -> float:
    """Contextual Appropriateness via Expected Profile Similarity."""
    score = 0.0
    normalizer = 0.0
    
    for item in rec_list:
        k = item['pos']
        discount = disc_func(k) if use_rank else 1.0
        relevance = p_rel(item) if use_relevance else 1.0
        similarity = item['sem']
        
        score += discount * relevance * similarity
        normalizer += discount
    
    return score / normalizer if normalizer > 0 else 0.0


def ce_coc(rec_list: List[Dict], goal_items: List[int] = None) -> float:
    """Control Effectiveness (conceptual). Discussed qualitatively in paper."""
    if goal_items is None:
        archive_c_items = [item for item in rec_list if item['archive'] == 'C']
        top_positions = [item['pos'] for item in archive_c_items if item['pos'] <= 5]
        effort = max(0, 2 - len(top_positions))
        return float(effort)
    else:
        top_items = [item['pos'] for item in rec_list if item['pos'] in goal_items]
        effort = len(goal_items) - len(top_items)
        return float(effort)


def mwr(rec_list: List[Dict], use_relevance: bool = True) -> float:
    """Metadata-Weighted Relevance."""
    if len(rec_list) == 0:
        return 0.0
    
    score = 0.0
    for item in rec_list:
        relevance = p_rel(item) if use_relevance else 1.0
        quality = item['meta']
        score += relevance * quality
    
    return score / len(rec_list)


def dri_ils(rec_list: List[Dict]) -> float:
    """Document Relationship Insight via Intra-List Similarity."""
    n = len(rec_list)
    if n <= 1:
        return 0.0
    
    total_sim = 0.0
    count = 0
    
    for i, item_i in enumerate(rec_list):
        for j, item_j in enumerate(rec_list):
            if i != j:
                sim = 1.0 - abs(item_i['sem'] - item_j['sem'])
                total_sim += sim
                count += 1
    
    return total_sim / count if count > 0 else 0.0


def ri_count(rec_list: List[Dict], scholarly_outputs: List[int] = None) -> float:
    """Research Integration (conceptual). Discussed qualitatively in paper."""
    score = 0.0
    for item in rec_list:
        if item['rel'] == 1:
            popularity = item['raters'] / 1000.0
            discovery_value = (1.0 - popularity) * 0.5
            score += discovery_value
    
    return score


def csva(metrics: Dict[str, float],
         weights: Dict[str, float],
         thresholds: Dict[str, float] = None) -> float:
    """Cross-Stakeholder Value Alignment."""
    if thresholds:
        for metric_name, threshold in thresholds.items():
            if metric_name in metrics and metrics[metric_name] < threshold:
                print(f"Warning: {metric_name} = {metrics[metric_name]:.4f} below threshold {threshold}")
    
    score = 0.0
    total_weight = 0.0
    
    for metric_name, weight in weights.items():
        if metric_name in metrics:
            score += weight * metrics[metric_name]
            total_weight += weight
    
    return score / total_weight if total_weight > 0 else 0.0


def normalize_for_csva(metrics: Dict[str, Dict[str, float]], 
                       strategy: str = 'minmax') -> Dict[str, Dict[str, float]]:
    """Normalize metrics for CSVA. Supports minmax, zscore, rank, softmax, percentile."""
    normalized = {}
    
    for metric_name, values in metrics.items():
        if strategy == 'minmax':
            min_val = min(values.values())
            max_val = max(values.values())
            
            if max_val - min_val > 0:
                normalized[metric_name] = {
                    rec_name: (val - min_val) / (max_val - min_val)
                    for rec_name, val in values.items()
                }
            else:
                normalized[metric_name] = {rec_name: 0.5 for rec_name in values.keys()}
        
        elif strategy == 'zscore':
            vals = list(values.values())
            mean = sum(vals) / len(vals)
            
            if len(vals) > 1:
                variance = sum((x - mean) ** 2 for x in vals) / len(vals)
                std = math.sqrt(variance)
            else:
                std = 1.0
            
            if std > 0:
                z_scores = {name: (val - mean) / std for name, val in values.items()}
                normalized[metric_name] = {
                    name: max(0, min(1, (z + 3) / 6))
                    for name, z in z_scores.items()
                }
            else:
                normalized[metric_name] = {rec_name: 0.5 for rec_name in values.keys()}
        
        elif strategy == 'rank':
            sorted_items = sorted(values.items(), key=lambda x: x[1])
            n = len(sorted_items)
            ranks = {name: i for i, (name, val) in enumerate(sorted_items)}
            
            if n > 1:
                normalized[metric_name] = {
                    name: rank / (n - 1) 
                    for name, rank in ranks.items()
                }
            else:
                normalized[metric_name] = {rec_name: 0.5 for rec_name in values.keys()}
        
        elif strategy == 'softmax':
            exp_values = {name: math.exp(val) for name, val in values.items()}
            total = sum(exp_values.values())
            
            if total > 0:
                normalized[metric_name] = {
                    name: exp_val / total 
                    for name, exp_val in exp_values.items()
                }
            else:
                normalized[metric_name] = {
                    name: 1.0 / len(values) 
                    for name in values.keys()
                }
        
        elif strategy == 'percentile':
            vals = list(values.values())
            sorted_vals = sorted(vals)
            n = len(sorted_vals)
            
            normalized[metric_name] = {}
            for rec_name, val in values.items():
                rank = sum(1 for v in sorted_vals if v < val)
                percentile = (rank / (n - 1)) if n > 1 else 0.5
                normalized[metric_name][rec_name] = percentile
        
        else:
            raise ValueError(f"Unknown normalization strategy: {strategy}")
    
    return normalized

