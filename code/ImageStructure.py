import numpy as np
from Fourier import *


# wrapper class for image structure functions
class ImageStructure:

    def __init__(self,inputs):
        """
        Light
        """
        self.dimensions = int(2)
        assert ((self.dimensions == 2) | (self.dimensions == 3))
        self.set_input_data( self.read_input_data(inputs, "npy") )
        self.set_structure_function("fourier")

    def set_input_data(self,data):
        self.input_data = data

    # Method to read input file data
    def read_input_data(self,data_file,data_file_type):
        if (data_file_type == 'npy'):
            input_data = np.load(data_file)
        elif (data_file_type == 'csv'):
            input_data = np.loadtxt(data_file,delimiter=',')
        else:
            sys.exit('Unsupported input data type. Supported types are: npy and csv.')
        return input_data

    # Method to set the relevant structure function
    def set_structure_function(self,structure_function_type):
        if (structure_function_type == 'fourier'):
            self.structure_function = fit_gaussian_to_average_fourier_spectrum
        else:
            sys.exit('Unsupported structure function type. Supported types are: fourier.')

    # Main method to compute data structure
    def compute_structure(self,plot_metrics=False):
        structure = self.structure_function(self.input_data, plot_metrics)
        return structure
