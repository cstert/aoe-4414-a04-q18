# eci_to_ecef.py
#
# Usage: python3 eci_to_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km
# Converts from ECI coordinates to ECEF coordinates
# Parameters:
# year: year of date
# month: month of date
# day: day of date
# hour: hour of date
# minute: minute of date
# second: second of date
# eci_x_km: ECI x-coordinate in km
# eci_y_km: ECI y-coordinate in km
# eci_z_km: ECI z-coordinate in km
# Output:
# Prints ECEF coordinates in km
#
# Written by Celia Sterthous
# Other contributors: None
#
# See the LICENSE file for the license.
# import Python modules
import sys # argv
import math
# "constants"
W = 7.292115*10**-5
# helper functions
## function description
# def calc_something(param1, param2):
# pass


# parse script arguments
if len(sys.argv)==10:
 year = int(sys.argv[1])
 month = int(sys.argv[2])
 day = int(sys.argv[3])
 hour = int(sys.argv[4])
 minute = int(sys.argv[5])
 second = float(sys.argv[6])
 eci_x_km = float(sys.argv[7])
 eci_y_km = float(sys.argv[8])
 eci_z_km = float(sys.argv[9])

else:
   print(\
      'Usage: '\
      'python3 eci_to_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km'
     )
   exit()

# write script below this line
jd = day - 32075 + 1461*(year+4800+(month-14)/12)/4+367*(month-2-(month-14)/12*12)/12-3*((year+4900+(month-14)/12)/100)/4
JDmidnight = jd-0.5
Dfrac = (second+60*(minute+60*hour))/86400
jd_frac = JDmidnight+Dfrac
Tut1 = (jd-2451545.0)/36525
gmst_ang = 67310.54841+(876600*60*60+8640184.812866)*Tut1+0.093104*(Tut1**2)+(-6.2*0.000001*(Tut1**3))
gmst_rad = math.fmod(gmst_ang%86400*W+2*math.pi,2*math.pi)
ecef_x_km = eci_x_km*math.cos(-gmst_rad)-eci_y_km*math.sin(-gmst_rad)
ecef_y_km = eci_y_km*math.cos(-gmst_rad)+eci_x_km*math.sin(-gmst_rad)
ecef_z_km = eci_z_km

print(jd_frac)
print(gmst_rad)
print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)
