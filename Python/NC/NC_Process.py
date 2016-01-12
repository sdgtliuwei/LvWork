# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 22:50:37 2016
For nc file processing.
@author: sdgtliuwei
"""

import numpy
from netCDF4 import Dataset

class NC_Process:
    #打开NC
    def OpenNCFile(filename):
        rootgrp = Dataset(filename,"r")
        print("\nOpen Success...")
        return rootgrp
    
    def GetVarValues(rootgrp_old, var_name):    
        var_values = rootgrp_old.variables[var_name]
        return var_values
        
    def CreatNCFile(filename_new):
        rootgrp_new = Dataset(filename_new, "w", format="NETCDF3_CLASSIC")
        print("Creat Success...")
        return rootgrp_new
        
    def CreatNCDim(rootgrp_new, dim_name, dimvaluesnumber):
        rootgrp_new.createDimension(dim_name, dimvaluesnumber)
        
    def CreatNCVar(rootgrp_new, var_name, var_valuetype, var_dims, fill_values, long_name, standard_name, units):
        var_values = rootgrp_new.createVariable(var_name, var_valuetype, var_dims, fill_value = 3.4E38)    
        var_values.long_name = long_name
        var_values.standard_name = standard_name
        var_values.units = units
        #wave_udir.scale_factor = 0.0001   
        return var_values
    
    def CreatMatrix(dims, valuetype):
        return numpy.empty(dims, valuetype)
        
    def Matrix3Assignment(var_values, valuetype, dim3, range9):
        newMatrix = numpy.empty(dim3, numpy.float32)
        m = -1
        for i in range(range9[0], range9[1], range9[2]):
            for j in range(range9[3], range9[4], range9[5]):
                m = m + 1
                n = -1
                for k in range(range9[6], range9[7], range9[8]):
                    n = n + 1
                    newMatrix[i][m][n] = var_values[i][j][k]
        return newMatrix
    
    def Var_valuesAssignment(var_values, newMatrix):
        var_values[:] = newMatrix
        return var_values
    
    def Var_values_rangeAssignment(var_values, old_values, valuerange0, valuerange1):
        var_values[:] = old_values[valuerange0:valuerange1]
        return var_values
    
    def CloseNCFile(rootgrp):
        rootgrp.close()
        print("Close Success...")

if __name__ == "__main__":
    nc_p = NC_Process
    filepath_old = "../../data/ocean_snap_temp_2015_01_01.nc"#os.path.pardir + "/" + os.path.pardir +
    filepath_new = "../../data/ocean_snap_temp_new.nc"
    rootgrp_old = nc_p.OpenNCFile(filepath_old)
    rootgrp_new = nc_p.CreatNCFile(filepath_new)
    
    varvalues_time_old = nc_p.GetVarValues(rootgrp_old, "time")
    varvalues_lat_old = nc_p.GetVarValues(rootgrp_old, "lat")
    varvalues_lon_old = nc_p.GetVarValues(rootgrp_old, "lon")
    varvalues_temp_old = nc_p.GetVarValues(rootgrp_old, "water_temp_china")
    
    dims_new = ["time", "lat", "lon"]
    dims_num_new = [1,280,230]
    
    dim_time_new = nc_p.CreatNCDim(rootgrp_new, dims_new[0], dims_num_new[0])
    dim_lat_new = nc_p.CreatNCDim(rootgrp_new, dims_new[1], dims_num_new[1])
    dim_lon_new = nc_p.CreatNCDim(rootgrp_new, dims_new[2], dims_num_new[2])
    
    varvalues_time_new = nc_p.CreatNCVar(rootgrp_new, "time", "f4", dims_new[0], 3.4E38, "time", "Time", "s")
    varvalues_lat_new = nc_p.CreatNCVar(rootgrp_new, "lat", "f4", dims_new[1], 3.4E38, "lat", "Lat", "deg")
    varvalues_lon_new = nc_p.CreatNCVar(rootgrp_new, "lon", "f4", dims_new[2], 3.4E38, "lon", "Lon", "deg")
    varvalues_temp_new = nc_p.CreatNCVar(rootgrp_new, "temp", "f4", dims_new, 3.4E38, "temp", "Temp", "k")
    
    ranges = [0, 1, 1, 0, 280, 1, 0, 230, 1]
    
    varvalues_temp_newtemp = nc_p.Matrix3Assignment(varvalues_temp_old, numpy.float32, dims_num_new, ranges)
    
    varvalues_time_new = nc_p.Var_valuesAssignment(varvalues_time_new, varvalues_time_old)
    varvalues_lat_new = nc_p.Var_valuesAssignment(varvalues_lat_new, varvalues_lat_old)
    varvalues_lon_new = nc_p.Var_valuesAssignment(varvalues_lon_new, varvalues_lon_old)
    varvalues_temp_new = nc_p.Var_valuesAssignment(varvalues_temp_new, varvalues_temp_newtemp)
    
    nc_p.CloseNCFile(rootgrp_old)
    nc_p.CloseNCFile(rootgrp_new)