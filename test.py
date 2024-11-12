def penn_state_equation(T_c, RH):
    """
    Calculates additional water requirement using Penn State Equation.
    
    Parameters:
    - T_c: Ambient temperature in degrees Celsius
    - RH: Relative humidity in percent
    
    Returns:
    - E_res: Additional water requirement due to environmental conditions and physical activity
    """
    if T_c < -10:
        E_res = 0
    if T_c < 25:
        E_res = (0.033 * (T_c - 50) + 0.0025 * (T_c - 10)**2 + 0.8148) * (1 + 0.02 * (RH - 50) * 0.01) / 3
    else:
        E_res = (0.033 * (T_c - 25) + 0.8148) * (1 + 0.02 * (RH - 50) * 0.01) / 3
    return E_res

i=60
for j in range(0, 100):
    # for j in range(0, 100):
    add = penn_state_equation(i, j)
    print("T_c:", i, "RH:", j, "Add:", add)
