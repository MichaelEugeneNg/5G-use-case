# 5G-use-case

# Description
This simulation is a demonstration of a 5G use case that locates User Equipments (UE) without GPS. The method used is cell tower trilateration,  which utilizes the COST-Hata Model or Friis Transmission Equation to convert Reference Signal Received Strength (RSRP) measurements to an estimation of distance from nearby cell towers. In a similar mechanism to GPS trilateration, knowing the distance to 3 or more nearby cell towers enables us to gain an estimation of the UE location. Because the distances calculated are such that they practically never intersect perfectly, I linearized the distances and performed least squares approximation to find the least squares optimized position of the UE.

# Step-by-step use
1. Use "Network Guru" or any other app to scan the RSRP value to the nearest 3 cell towers to the user
2. Run the main file and when prompted, input the RSRP values in the order of strongest signal strength first
3. In the graphic that pops up, the red, blue and green circles are the estimated distances from cell tower 1, 2, and 3 respectively. The red dot is the true user location (which needs to be hardcoded) and the green dot is where the algorithm / simulation estimates the location to be.

# Notes
Limited functionality: 
- The location of the 3 nearest cell towers was manually inputted beforehand using cellmapper's edition of cell site locations. Thus, this simulation is only accurate to the region of the inputted cell towers. (In this use case, the DSTA building at Depot Road, Singapore.) To test out alternative locations, the 3 nearest towers to that location will need to be found beforehand and their coordinate values inputted into the simulation
- Instead of lat/long values, the towers' coordinates are based on Euclidean Distance from a reference cell tower
