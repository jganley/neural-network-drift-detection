from numpy import mean
from numpy import std
from numpy import cov
from scipy.stats import pearsonr

acc_test = [58.11,54.14,46.44,50.35,42.46]
acc = [58.11,54.14,46.44,50.35,42.46,38.27,14.31]
hist_corr = [0.8235,0.1156,0.1086,0.1881,0.1049,0.1848,0.2084]
hist_chi = [110.4048,135.3100,694.0800,243.2645,4877.8596,22039.6524,4179.2460]
hist_inter = [9.0936,4.9949,2.4694,6.1183,5.0175,5.1712,4.9164]
hist_bhatt = [0.2292,0.6024,0.7459,0.5778,0.6561,0.6535,0.6520]
diff = [24.9576,35.9826,37.9945,41.2338,53.1476,54.0341,52.9437]
diff_half = [12.8567,20.0413,28.2983,28.7896,35.9498]
diff_half_gray = [17.8759,28.7117,36.6552,37.4587,48.6719,79.0112,75.3936]
sift = [600.25,635.25,314.25,307.5,252.75,200.5,208.0]

corr_corr, _ = pearsonr(acc, hist_corr)
corr_chi, _ = pearsonr(acc, hist_chi)
corr_inter, _ = pearsonr(acc, hist_inter)
corr_bhatt, _ = pearsonr(acc, hist_bhatt)
corr_diff, _ = pearsonr(acc, diff)
corr_diff_half, _ = pearsonr(acc_test, diff_half)
corr_diff_half_gray, _ = pearsonr(acc, diff_half_gray)
corr_sift, _ = pearsonr(acc, sift)

print("Correlation " + str(corr_corr))
print("Chi Square " + str(corr_chi))
print("Intersection " + str(corr_inter))
print("Bhatt " + str(corr_bhatt))
print("Diff " + str(corr_diff))
print("Diff Half " + str(corr_diff_half))
print("Diff Half Gray " + str(corr_diff_half_gray))
print("SIFT " + str(corr_sift))
