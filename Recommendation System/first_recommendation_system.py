#####################################################################
#   In this program I subset data from GetGlue website.             #
#   Each row represent user rating system of product.               #
#   The output is a Principal Component Analysis.                   #
#####################################################################
import math
import numpy as np

__author__ = "Eduardo Lalo Carrasco Jr."

pu = [[(0, 0, 1), (0, 1, 22), (0, 2, 1), (0, 3, 1), (0, 5, 0)],
      [(1, 0, 1), (1, 1, 32), (1, 2, 0), (1, 3, 0), (1, 4, 1), (1, 5, 0)],
      [(2, 0, 0), (2, 1, 18), (2, 2, 1), (2, 3, 1), (2, 4, 0), (2, 5, 1)],
      [(3, 0, 1), (3, 1, 40), (3, 2, 1), (3, 3, 0), (3, 4, 0), (3, 5, 1)],
      [(4, 0, 0), (4, 1, 40), (4, 2, 0), (4, 4, 1), (4, 5, 0)],
      [(5, 0, 0), (5, 1, 25), (5, 2, 1), (5, 3, 1), (5, 4,1 )]
      ]

pv = [[(0, 0, 1), (0, 1, 22), (0, 2, 1), (0, 3, 1), (0, 5, 0)],
      [(1, 0, 22), (1, 1, 32), (1, 2, 18), (1, 3, 40), (1, 4, 40), (1, 5, 25)],
      [(2, 0, 1), (2, 1, 0), (2, 2, 1), (2, 3, 1), (2, 4, 0), (2, 5, 1)],
      [(3, 0, 1), (3, 1, 0), (3, 2, 1), (3, 3, 0), (3, 5, 1)],
      [(4, 1, 1), (4, 2, 0), (4, 3, 0), (4, 4, 1), (4, 5, 1)],
      [(5, 0, 0), (5, 1, 0), (5, 2, 1), (5, 3, 1), (5, 4, 0)]
      ]

V = np.mat([
    [0.15968384, 0.9441198, 0.83651085],
    [0.73573009, 0.24906915, 0.85338239],
    [0.25605814, 0.6990532, 0.50900407],
    [0.2405843, 0.31848888, 0.60233653],
    [0.24237479, 0.15293281, 0.22240255],
    [0.03943766, 0.19287528, 0.95094265]
])

print V

U = np.mat(np.zeros([6, 3]))
L = 0.03

for iter in xrange(5):
    print"\n------ ITER %s ------" % (iter+1)
    print "U"

    urs = []

    for uset in pu:
        vo = []
        pvo = []

        for i, j, p in uset:
            vor = []
            for k in xrange(3):
                vor.append(V[j, k])
            vo.append(vor)
            pvo.append(p)

        vo = np.mat(vo)
        ur = np.linalg.inv(vo.T*vo + L*np.mat(np.eye(3))) * vo.T * np.mat(pvo).T
        urs.append(ur.T)
    U = np.vstack(urs)
    print U

    print"V"
    vrs = []
    for vset in pv:
        uo = []
        puo = []
        for j, i, p in vset:
            uor = []
            for k in xrange(3):
                uor.append(U[i, k])
            uo.append(uor)
            puo.append(p)
        uo = np.mat(uo)
        vr = np.linalg.inv(uo.T*uo + L*np.mat(np.eye(3)))*uo.T*np.mat(puo).T
        vrs.append(vr.T)
    V = np.vstack(vrs)

    err = 0.0
    n = 0.0

    for uset in pu:
        for i, j, k in uset:
            err += (k - (U[i]*V[j].T)[0, 0])**2
            n += 1
    print math.sqrt(err/n)

output_matrix = U*V.T
print"Recommendation Matrix:"
print output_matrix


