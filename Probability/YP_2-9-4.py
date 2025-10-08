import scipy.stats as st
p = sum(st.binom.pmf(k, 12, 0.15) for k in range(0, 4))
print(p)  # ≈ 0.91