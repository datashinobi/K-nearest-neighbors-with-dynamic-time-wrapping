# K-nearest-neighbors-with-dynamic-time-wrapping

While working on a time series classification, I have came across several papers reporting great result using K-nearest neighbors and dynamic time warping as similarity measures betweens temporal sequences which may vary in speed.

A knn classifier can achieve state-of-the-art performance when using Dynamic Time Warping as a distance measure[3].

This repo contains a python implementation using Scikit learn and fastDTW that provide O(n) time and space complexity






# References

1.  A. Bagnall and J. Lines. An experimental evaluation of nearest neighbour time series classification https://arxiv.org/abs/1406.4757

2.  htps://github.com/markdregan/K-Nearest-Neighbors-with-Dynamic-Time-Warping

3. Ding, Hui; Trajcevski, Goce; Scheuermann, Peter; Wang, Xiaoyue; Keogh, Eamonn (2008). "Querying and mining of time series data: experimental comparison of representations and distance measures".http://dl.acm.org/citation.cfm?id=2429754
