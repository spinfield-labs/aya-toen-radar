# icoer_kprime.py
def calculate_icoer(c_sem, c_lex, c_aff, c_temp, c_meta, weights=(0.25, 0.2, 0.15, 0.2, 0.2)):
    return sum(w * x for w, x in zip(weights, [c_sem, c_lex, c_aff, c_temp, c_meta]))
