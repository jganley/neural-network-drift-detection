from numpy import mean
from numpy import std
from numpy import cov
from scipy.stats import pearsonr

def correlation(acc_test, acc, hist_corr, hist_chi, hist_inter, hist_bhatt, diff, diff_half, diff_half_gray, sift):
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
