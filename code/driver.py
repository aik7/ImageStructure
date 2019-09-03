##############################################################################
# Description: Compute structure vectors (mean, sd) of the Gaussian fit to the average Fourier magnitude
# INPUT:  a gray-scale image
# OUTPUT: a figure and a structured vector [m, sig, mean, sd]
##############################################################################

import numpy as np
from ImageStructure import *
from Fourier import *
from inputArgs import *


def main():

    # Compute structure function
    structure_analysis = ImageStructure(input)
    structure_metrics  = structure_analysis.compute_structure(plot_metrics=False)

    results = np.array([m, sig, structure_metrics[0], structure_metrics[1]] )
    f=open('structured_vectors.dat','a')
    np.savetxt(f,np.transpose(results))
    f.close()
    #print(results)

if __name__ == '__main__':
    main()
