import os
import json
import numpy as np
import matplotlib.pyplot as plt

class Cn3NeutronFlux():

  def __init__(self): 
    self.script_dir = os.path.dirname(__file__)
    json_path = os.path.join(self.script_dir, "../../../physicalConstants.json")
    with open(json_path, "r") as f:
     data = json.load(f)
     
    self.m = data["neutronMass"]
    self.h = data["plankConstant"]
    
    self.t0 = 1.22 # ms
    

  def main(self,filename, path_length):

    self.pathLength = path_length

    time_list, counts_list = self.readtxt(filename)
    energy_list, wave_length = self.energy(time_list)
    # energy_bin_list, counts_bin_list = self.bining(energy_list, counts_list, self.bin)


    # plt.figure()
    # plt.step(energy_list, counts_list, label = filename)
    # # plt.step(energy_bin_list, counts_bin_list, label = filename)
    # plt.xscale("log")
    # # plt.yscale("log")
    # plt.grid(True)
    # plt.show()
    # # plt.savefig(png_path)

    return np.flip(energy_list[1:]), np.flip(counts_list[1:]), time_list[1:]
  

  def readtxt(self,filename):

    txt_path = os.path.join(self.script_dir,filename)
    data = np.loadtxt(txt_path)

    ind_t0 = np.where(data[:,0] > self.t0)[0][0]

    time_list = data[ind_t0:,0]
    counts_list = data[ind_t0:,1]

    return time_list, counts_list
  

  # def bining(self, energy_list, counts_list,bin):
  #   #line 36-38 assert that the data can be divided by 5, so to do the bining.
  #   '''
  #   if len(time_list) % 5 !=0 and len(counts_list) % 5 !=0 : 
  #     time_list = time_list[:len(time_list) // 5 * 5]
  #     counts_list = counts_list[:len(counts_list) // 5 * 5]
  #   '''
  #   t = 0
  #   energy_bin_list = np.asarray([])
  #   counts_bin_list = np.asarray([])

  #   while t < len(energy_list):
  #     Ei = energy_list[t]
  #     C_bin = 0
  #     compt = 0
  #     while np.log10(energy_list[t]/Ei) < bin:
  #       C_bin += counts_list[t]
  #       compt+=1
  #       t +=1
  #       if t >= len(energy_list):
  #         break
  #     if compt!=0:
  #       counts_bin_list = np.append(counts_bin_list,C_bin/compt)
  #     else:
  #       counts_bin_list = np.append(counts_bin_list,counts_list[t])
  #     t += 1

  #     energy_bin_list = np.append(energy_bin_list,Ei)

  #   # print(energy_list)
  #   # print(energy_bin_list)

  #   return energy_bin_list, counts_bin_list
       

    # reshaped_time_list = time_list.reshape(-1,5)
    # time_bin_list = reshaped_time_list.mean(axis=1)

    # reshaped_counts_list = counts_list.reshape(-1,5)
    # counts_bin_list = reshaped_counts_list.sum(axis=1)

    # time_span = reshaped_time_list[0][-1] - reshaped_time_list[0][0]

  def energy(self, time_list):
    # print((self.h**2/(2 * self.m * (2e-10)**2))/1.6e-19)
    time_list += - self.t0
    speed = self.pathLength / time_list
    wave_length = self.h / (self.m * speed)
    
    energy_list = (1/2. * self.m * (speed) **2) / (1.6e-19) #Energy is in eV
    # energy_list = self.h**2/(2 * self.m * (wave_length)**2)/1.6e-19
    # energy_span = self.m * (self.pathLength * 10e-3 ** 2) / ((time_list * 10e-3) ** 3) / (1.6 * 10e-19) * (time_list[-1] - time_list[0])
    # counts_fixed_list = counts_list / energy_span

    return energy_list, wave_length

# Cn3NeutronFlux().main('rpmt_run8_x_[300,700]_y_[400,700]_tbin_1000.txt')
