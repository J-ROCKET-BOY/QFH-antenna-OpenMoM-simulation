# QFH-antenna-OpenMoM-simulation
QFH antenna model generator for OpenMoM

How to use

1. Make a parameter file
Please refer parameter.csv
* File Name     : File name of the model, folder name where it will be stored.
* BaseModel     : The original model. Simulation parameters other than object shape, such as frequency range, are inherited from this model file.
* d[m]          : Thickness of the elements.
* Dl[m], Ds[m]  : Diameter of the helices (Dl: larger, Ds: smaller)
* Hl[m], Hs[m]  : Helical height (Hl: the larger one, Hs: the smaller one)
* Ht[m]         : Height of upper element above ground
* Div           : Number of divisions of helical section (if 36, divide 180/36 = 5 degrees each)
 
2. Run python script to make QFH antenna model
e.g. python QFHgenerator.py parameter.csv

3. Run ommRun.bat for simulating all models or simulate manually
* ommRun.bat is assuming openMoM is on "C:¥OpenMOM¥omm.exe". You need to change 3rd row of ommRun.bat if there are in different location.
* ommRun.bat is assuming CPU has 16 threads. You need to change 22th row if you want to run with different number of threads.

4. Simulation is done. you can check the result by opening ev2d.htm and ev3d.htm
