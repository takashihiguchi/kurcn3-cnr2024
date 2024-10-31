import os
import numpy as np
import matplotlib.pyplot as plt
from cn3NeutronFlux import Cn3NeutronFlux

class Drawgraph():
    
    def __init__(self,title,xlabel,ylabel):
        self.script_dir = os.path.dirname(__file__)
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.cn3_neutron_flux = Cn3NeutronFlux()
        plt.figure()

    def main(self):
        png_path = os.path.join(self.script_dir, "cn3_flux.png")
        energy_count_list = self.collect_alldata()
        for i in range(self.length_file):
            plt.plot(energy_count_list[i][0],energy_count_list[i][1], label = self.files[i])
        plt.xscale("log")
        plt.yscale("log")
        self.add_labels()
        plt.show()
        # plt.savefig(png_path)
    
    def collect_alldata(self):
        files = [
            "rpmt_run8_x_[300,700]_y_[400,550]_tbin_1000.txt",
            # "rpmt_run8_x_[300,700]_y_[400,550]_tbin_10000.txt",
            "rpmt_run8_x_[300,700]_y_[550,700]_tbin_1000.txt"
        ]
        self.files = files
        self.length_file = len(files)
        energy_count_list = []
        for file_name in files:
            E,C = self.cn3_neutron_flux.main(file_name)
            energy_count_list.append([E,C])
        return energy_count_list

    def add_labels(self):
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend()

Drawgraph(title="Count = f(Energy)", xlabel = "Energy (eV)", ylabel = "Counts").main()