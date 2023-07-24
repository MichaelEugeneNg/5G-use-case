# Cell Phone Trilateration Algorithm - www.101computing.net/cell-phone-trilateration-algorithm/
import draw
import numpy as np
from math import pi, log10, sqrt
import _tkinter

# Define all global variables
  
# M1 (taking the centre cell tower as the origin point of reference, the other centres are the distance wrt the origin)
# x1 = 0 # longitude 103.8131344
# y1 = 0 # latitude 1.2816705
# x2 = -143.32 # longitude 103.8118452
# y2 = -96.16 # latitude 1.2808057
# x3 = 230.26 # longitude 103.8152057
# y3 = 200.8 # latitude 1.2834765
# DSTA_x = 466.8 # longitude 103.81604422154209
# DSTA_y = -143.9 # latitude 1.2803763776682942

# Singtel (taking the centre cell tower as the origin point of reference, the other centres are the distance wrt the origin)
x1 = 0 # longitude 103.8159188
y1 = 0 # latitude 1.2811630
x2 = -166.5 # longitude 103.814421
y2 = -72.05 # latitude 1.280515
x3 = 136.54 # 103.817147
y3 = -248.74 # 1.278926
DSTA_x = 13.94 # longitude 103.81604422154209
DSTA_y = -87.47 # latitude 1.2803763776682942

def distanceModel(rsrp1,rsrp2,rsrp3):
  # ******************** FRIIS TRANSMISSION EQUATION ********************
  # Convert all RSRP values from dBm to Watts
  # power1 = (10**(rsrp1/10))/1000
  # power2 = (10**(rsrp2/10))/1000
  # power3 = (10**(rsrp3/10))/1000
  # Calculate distances to cell towers assuming transmit power as 0.0005 W after performing a calibration measurement
  # r1 = (3*(10**8)/(4*pi*1.8*(10**9)))*(0.0005/power1)**0.5
  # r2 = (3*(10**8)/(4*pi*1.8*(10**9)))*(0.0005/power2)**0.5
  # r3 = (3*(10**8)/(4*pi*1.8*(10**9)))*(0.0005/power3)**0.5

  # ******************** COST-HATA MODEL ********************
  # Path loss (dB) = transmit power (assume 1 W (30 dBm)) - received power (dBm), and
  # Assuming we receive a 5G signal which has f = 3500 MHz, and
  # Assuming effective height of cell tower antenna is 50 m, and
  # Assuming effective height of mobile phone antenna is 2 m above ground, then by COST-Hata Model:
  numerator1 = 30 - rsrp1 - 54.27 - 33.9 * log10(3500) + 13.82*log10(50) + 3.82*((log10(11.75 * 2))**2)
  denominator1 = 44.9 - 6.55 * log10(50)
  r1 = 10**(3 + numerator1/denominator1) # The integer 3 converts r1 from km to m

  numerator2 = 30 - rsrp2 - 54.27 - 33.9 * log10(3500) + 13.82*log10(50) + 3.82*((log10(11.75 * 2))**2)
  denominator2 = 44.9 - 6.55 * log10(50)
  r2 = 10**(3 + numerator2/denominator2) # The integer 3 converts r2 from km to m

  numerator3 = 30 - rsrp3 - 54.27 - 33.9 * log10(3500) + 13.82*log10(50) + 3.82*((log10(11.75 * 2))**2)
  denominator3 = 44.9 - 6.55 * log10(50)
  r3 = 10**(3 + numerator3/denominator3) # The integer 3 converts r3 from km to m
  return r1,r2,r3


# A function to apply trilateration formulas to return the (x,y) intersection point of three circles
def trackPhone(x1,y1,r1,x2,y2,r2,x3,y3,r3):
  A = 2*x2 - 2*x1
  B = 2*y2 - 2*y1
  C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
  D = 2*x3 - 2*x2
  E = 2*y3 - 2*y2
  F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2
  x = (C*E - F*B) / (E*A - B*D)
  y = (C*D - A*F) / (B*D - A*E)
  return x,y

# A function to apply least squares to return the best (x,y) value for the phone
def leastSquaresSolution(x1,y1,r1,x2,y2,r2,x3,y3,r3):
  A = 2*x2 - 2*x1
  B = 2*y2 - 2*y1
  C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
  D = 2*x3 - 2*x2
  E = 2*y3 - 2*y2
  F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2

  M = np.array([[A,B], [D,E]])
  b_vector = np.array([C,F]).reshape((2,1))
  x,y = np.linalg.lstsq(M, b_vector, rcond=None)[0]


  # # Circle centers and radii
  # centers = np.array([(x1, y1), (x2, y2), (x3, y3)])
  # radii = np.array([r1, r2, r3])

  # # Coefficient matrix A
  # A = np.hstack((2 * centers, np.ones((3, 1))))

  # # Constant vector b
  # b = centers[:, 0]**2 + centers[:, 1]**2 - radii**2

  # # Solve the least squares problem
  # solution, residuals, rank, singular_values = np.linalg.lstsq(A, b, rcond=None)

  # # Extract the x and y coordinates of the best solution
  # x_solution, y_solution = solution[:2]

  # # Print the best solution
  # print("Best solution (x, y):", x_solution, y_solution)

  return x,y
  

# Generate and represent data to be used by the trilateration algorithm
rsrp1 = float(input("Signal Strength (RSRP) 1 (dBm):"))
rsrp2 = float(input("Signal strength (RSRP) 2 (dBm):"))
rsrp3 = float(input("Signal strength (RSRP) 3 (dBm):"))
r1,r2,r3 = distanceModel(rsrp1,rsrp2,rsrp3)

# Apply trilateration algorithm to locate phone
# x,y = trackPhone(x1,y1,r1,x2,y2,r2,x3,y3,r3)
x,y = leastSquaresSolution(x1,y1,r1,x2,y2,r2,x3,y3,r3)

# Output phone location / coordinates
print("Cell Phone Location (plotted as a green dot):")
print("x:" + str(x[0]))
print("y:" + str(y[0]))

euclideanDistance = sqrt((x[0]+abs(DSTA_x))**2 + (y[0]+abs(DSTA_y))**2)
print("Distance from actual:" + str(euclideanDistance) + " m")

latitude = y[0]/110574.827 + 1.2811630 # Based on Singtel reference point
longitude = x[0]/111291.866 + 103.8159188 # Based on Singtel reference point
print("Latitude and Longitude of UE:" + str(latitude) + "º N, " + str(longitude) + "º E")

draw.drawCellTowers(x1,y1,r1,x2,y2,r2,x3,y3,r3,x[0],y[0],DSTA_x,DSTA_y)
