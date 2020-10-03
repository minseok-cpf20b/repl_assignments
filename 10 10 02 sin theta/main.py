import numpy as np
import math
from root_finding import sequential


def g(theta_deg:float) -> float:
  return math.sin(math.radians(theta_deg))**2 - 0.5
  
  
  if "__main__" == __name__:
    
    theta_deg_seq = sequential(g, 0.0, 1e-5, 1e-3, 180)
    theta_rad_seq = np.deg2rad(theta_deg_seq)
    print(f"sin({theta_deg_seq:g}[deg]) ** 2 =" , np.sin(theta_rad_seq) ** 2)