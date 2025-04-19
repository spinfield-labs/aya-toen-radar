# cmeta_advanced.py
def compute_cmeta_advanced(loop_sem, compress_ratio, reflexivity, weights=(0.4, 0.3, 0.3)):
    return sum(w * x for w, x in zip(weights, [loop_sem, compress_ratio, reflexivity]))
