import tellurium as te

#feed forward loops
c_1_FFL_AND = """
model C_1_FFL_AND
  species X, Y, Z

  // X and Y dynamics
  J0: -> X; kx
  J1: -> Y; ky*(X/Kx)^n/(1 + (X/Kx)^n)
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y

  // Z production
  // Uncomment one of these lines:

  // AND logic: Z requires both X and Y
  J4: -> Z; kz*((X/Kx)^n/(1+(X/Kx)^n))*((Y/Ky)^n/(1+(Y/Ky)^n))

  // OR logic: Z can be produced by either X or Y
  //J4: -> Z; kz*((X/Kx)^n/(1+(X/Kx)^n) + (Y/Ky)^n/(1+(Y/Ky)^n))

  J5: Z -> ; dz*Z

  // Parameters
  kx = 1.0; ky = 1.5; kz = 1.2
  dx = 0.5; dy = 0.5; dz = 0.5
  Kx = 1.0; Ky = 1.0
  n = 2

  // Initial conditions
  X = 0.1; Y = 0.1; Z = 0.1
end
"""
c_1_FFL_OR = """
model C_1_FFL_OR
  species X, Y, Z

  // X and Y dynamics
  J0: -> X; kx
  J1: -> Y; ky*(X/Kx)^n/(1 + (X/Kx)^n)
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y

  // Z production
  // Uncomment one of these lines:

  // AND logic: Z requires both X and Y
  //J4: -> Z; kz*((X/Kx)^n/(1+(X/Kx)^n))*((Y/Ky)^n/(1+(Y/Ky)^n))

  // OR logic: Z can be produced by either X or Y
  J4: -> Z; kz*((X/Kx)^n/(1+(X/Kx)^n) + (Y/Ky)^n/(1+(Y/Ky)^n))

  J5: Z -> ; dz*Z

  // Parameters
  kx = 1.0; ky = 1.5; kz = 1.2
  dx = 0.5; dy = 0.5; dz = 0.5
  Kx = 1.0; Ky = 1.0
  n = 2

  // Initial conditions
  X = 0.1; Y = 0.1; Z = 0.1
end
"""
c_2_FFL_AND = """
model C_2_FFL_AND
  species X, Y, Z

  // X and Y dynamics
  J0: -> X; kx
  J1: -> Y; ky*1/(1 + (X/Kx)^n)
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y

  J4: -> Z; kz*(1/(1+(X/Kx)^n))*(Y/Ky)^n/(1+(Y/Ky)^n))
  J5: Z -> ; dz*Z

  // Parameters
  kx = 1.0; ky = 1.5; kz = 1.2
  dx = 0.5; dy = 0.5; dz = 0.5
  Kx = 1.0; Ky = 1.0
  n = 2

  // Initial conditions
  X = 0.1; Y = 0.1; Z = 0.1
end
"""
c_2_FFL_OR = """
model C_2_FFL_OR
  species X, Y, Z

  // X and Y dynamics
  J0: -> X; kx
  J1: -> Y; ky*1/(1 + (X/Kx)^n)
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y

  J4: -> Z; kz*(1/(1+(X/Kx)^n) + (Y/Ky)^n/(1+(Y/Ky)^n))
  J5: Z -> ; dz*Z

  // Parameters
  kx = 1.0; ky = 1.5; kz = 1.2
  dx = 0.5; dy = 0.5; dz = 0.5
  Kx = 1.0; Ky = 1.0
  n = 2

  // Initial conditions
  X = 0.1; Y = 0.1; Z = 0.1
end
"""
c_3_FFL_AND = """
model C_3_FFL_AND
  species X, Y, Z

  // X and Y dynamics
  J0: -> X; kx
  J1: -> Y; ky*(X/Kx)^n/(1 + (X/Kx)^n)
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y

  J4: -> Z; kz*(1/(1+(X/Kx)^n) * 1/(1+(Y/Ky)^n))
  J5: Z -> ; dz*Z

  // Parameters
  kx = 1.0; ky = 1.5; kz = 1.2
  dx = 0.5; dy = 0.5; dz = 0.5
  Kx = 1.0; Ky = 1.0
  n = 2

  // Initial conditions
  X = 0.1; Y = 0.1; Z = 0.1
end
"""
c_3_FFL_OR = """
model C_3_FFL_OR
  species X, Y, Z

  // X and Y dynamics
  J0: -> X; kx
  J1: -> Y; ky*(X/Kx)^n/(1 + (X/Kx)^n)
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y

  J4: -> Z; kz*(1/(1+(X/Kx)^n) + 1/(1+(Y/Ky)^n))
  J5: Z -> ; dz*Z

  // Parameters
  kx = 1.0; ky = 1.5; kz = 1.2
  dx = 0.5; dy = 0.5; dz = 0.5
  Kx = 1.0; Ky = 1.0
  n = 2

  // Initial conditions
  X = 0.1; Y = 0.1; Z = 0.1
end
"""
c_4_FFL_AND = """
model C_4_FFL_AND
  species X, Y, Z

  // X and Y dynamics
  J0: -> X; kx
  J1: -> Y; ky*1/(1 + (X/Kx)^n)
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y

  J4: -> Z; kz*((X/Kx)^n/(1+(X/Kx)^n) * 1/(1+(Y/Ky)^n))
  J5: Z -> ; dz*Z

  // Parameters
  kx = 1.0; ky = 1.5; kz = 1.2
  dx = 0.5; dy = 0.5; dz = 0.5
  Kx = 1.0; Ky = 1.0
  n = 2

  // Initial conditions
  X = 0.1; Y = 0.1; Z = 0.1
end
"""
c_4_FFL_AND = """
model C_4_FFL_OR
  species X, Y, Z

  // X and Y dynamics
  J0: -> X; kx
  J1: -> Y; ky*1/(1 + (X/Kx)^n)
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y

  J4: -> Z; kz*((X/Kx)^n/(1+(X/Kx)^n) + 1/(1+(Y/Ky)^n))
  J5: Z -> ; dz*Z

  // Parameters
  kx = 1.0; ky = 1.5; kz = 1.2
  dx = 0.5; dy = 0.5; dz = 0.5
  Kx = 1.0; Ky = 1.0
  n = 2

  // Initial conditions
  X = 0.1; Y = 0.1; Z = 0.1
end
"""

i_1_FFL_AND = """
model I_1_FFL_AND
  species X, Y, Z

  // X and Y dynamics
  J0: -> X; kx
  J1: -> Y; ky*(X/Kx)^n/(1 + (X/Kx)^n)
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y

  J4: -> Z; kz*((X/Kx)^n/(1+(X/Kx)^n) * 1/(1+(Y/Ky)^n))
  J5: Z -> ; dz*Z

  // Parameters
  kx = 1.0; ky = 1.5; kz = 1.2
  dx = 0.5; dy = 0.5; dz = 0.5
  Kx = 1.0; Ky = 1.0
  n = 2

  // Initial conditions
  X = 0.1; Y = 0.1; Z = 0.1
end
"""
i_2_FFL_AND = """
model I_2_FFL_AND
  species X, Y, Z

  // X and Y dynamics
  J0: -> X; kx
  J1: -> Y; ky*1/(1 + (X/Kx)^n)
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y

  J4: -> Z; kz*(1/(1+(X/Kx)^n) * 1/(1+(Y/Ky)^n))
  J5: Z -> ; dz*Z

  // Parameters
  kx = 1.0; ky = 1.5; kz = 1.2
  dx = 0.5; dy = 0.5; dz = 0.5
  Kx = 1.0; Ky = 1.0
  n = 2

  // Initial conditions
  X = 0.1; Y = 0.1; Z = 0.1
end
"""
i_3_FFL_AND = """
model I_3_FFL_AND
  species X, Y, Z

  // X and Y dynamics
  J0: -> X; kx
  J1: -> Y; ky*(X/Kx)^n/(1 + (X/Kx)^n)
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y

  J4: -> Z; kz*(1/(1+(X/Kx)^n) * (Y/Ky)^n/(1+(Y/Ky)^n))
  J5: Z -> ; dz*Z

  // Parameters
  kx = 1.0; ky = 1.5; kz = 1.2
  dx = 0.5; dy = 0.5; dz = 0.5
  Kx = 1.0; Ky = 1.0
  n = 2

  // Initial conditions
  X = 0.1; Y = 0.1; Z = 0.1
end
"""
i_4_FFL_AND = """
model I_4_FFL_AND
  species X, Y, Z

  // X and Y dynamics
  J0: -> X; kx
  J1: -> Y; ky*1/(1 + (X/Kx)^n)
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y

  J4: -> Z; kz*((X/Kx)^n/(1+(X/Kx)^n) * (Y/Ky)^n/(1+(Y/Ky)^n))
  J5: Z -> ; dz*Z

  // Parameters
  kx = 1.0; ky = 1.5; kz = 1.2
  dx = 0.5; dy = 0.5; dz = 0.5
  Kx = 1.0; Ky = 1.0
  n = 2

  // Initial conditions
  X = 0.1; Y = 0.1; Z = 0.1
end
"""

#feedback loops
PFL_1 = """
model PFL_1
  species X, Y

  // X and Y dynamics
  J0: -> X; kx*(Y/Ky)^n/(1 + (Y/Ky)^n)
  J1: -> Y; ky*(X/Kx)^n/(1 + (X/Kx)^n)
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y

  // Parameters
  kx = 1.5; ky = 1.5 
  dx = 0.5; dy = 0.5
  Kx = 1.0; Ky = 1.0
  n = 2

  // Initial conditions
  X = 1; Y = 0.1
end
"""
PFL_2 = """
model PFL_2
  species X, Y

  // X and Y dynamics
  J0: -> X; kx*1/(1 + (Y/Ky)^n)
  J1: -> Y; ky*1/(1 + (X/Kx)^n)
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y

  // Parameters
  kx = 1.5; ky = 1.5 
  dx = 0.5; dy = 0.5
  Kx = 1.0; Ky = 1.0
  n = 2

  // Initial conditions
  X = 1; Y = 0.1
end
"""
NFL_1 = """
model NFL_1
  species X, Y

  // X and Y dynamics
  J0: -> X; kx*(Y/Ky)^n/(1 + (Y/Ky)^n)
  J1: -> Y; ky*1/(1 + (X/Kx)^n)
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y

  // Parameters
  kx = 1.5; ky = 1.5 
  dx = 0.5; dy = 0.5
  Kx = 1.0; Ky = 1.0
  n = 2

  // Initial conditions
  X = 0.1; Y = 0.1
end
"""
NFL_2 = """
model NFL_2
  species X, Y

  // X and Y dynamics
  J0: -> X; kx*1/(1 + (Y/Ky)^n)
  J1: -> Y; ky*(X/Kx)^n/(1 + (X/Kx)^n)
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y

  // Parameters
  kx = 1.5; ky = 1.5 
  dx = 0.5; dy = 0.5
  Kx = 1.0; Ky = 1.0
  n = 2

  // Initial conditions
  X = 0.1; Y = 0.1
end
"""

#coupled feedback loops
#AND
PPFL_1 = """
model PPFL
  species X, Y, Z

  // X and Y dynamics
  J0: -> X; kx*(Y/Ky)^n/(1 + (Y/Ky)^n)
  J1: -> Y; ky*((X/Kx)^n/(1 + (X/Kx)^n) + (Z/Kz)^n/(1 + (Z/Kz)^n))
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y
  J4: -> Z; kz*(Y/Ky)^n/(1 + (Y/Ky)^n)
  J5: Z -> ; dz*Z

  // Parameters
  kx = 1.5; ky = 1.5; kz = 1.5
  dx = 0.5; dy = 0.5; dz = 0.5
  Kx = 1.0; Ky = 1.0; Kz = 1.0
  n = 2

  // Initial conditions
  X = 1; Y = 0.1; Z = 0.1
end
"""
PNFL_1 = """
model PNFL
  species X, Y, Z

  // X and Y dynamics
  J0: -> X; kx*(Y/Ky)^n/(1 + (Y/Ky)^n)
  J1: -> Y; ky*((X/Kx)^n/(1 + (X/Kx)^n) + 1/(1 + (Z/Kz)^n))
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y
  J4: -> Z; kz*(Y/Ky)^n/(1 + (Y/Ky)^n)
  J5: Z -> ; dz*Z

  // Parameters
  kx = 1.5; ky = 1.5; kz = 1.5
  dx = 0.5; dy = 0.5; dz = 0.5
  Kx = 1.0; Ky = 1.0; Kz = 1.0
  n = 2

  // Initial conditions
  X = 0.1; Y = 0.1; Z = 0.1
end
"""
NNFL_1 = """
model NNFL
  species X, Y, Z

  // X and Y dynamics
  J0: -> X; kx*(Y/Ky)^n/(1 + (Y/Ky)^n)
  J1: -> Y; ky*(1/(1 + (X/Kx)^n) + (Z/Kz)^n/(1 + (Z/Kz)^n))
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y
  J4: -> Z; kz*1/(1 + (Y/Ky)^n)
  J5: Z -> ; dz*Z

  // Parameters
  kx = 1.5; ky = 1.5; kz = 1.5
  dx = 0.5; dy = 0.5; dz = 0.5
  Kx = 1.0; Ky = 1.0; Kz = 1.0
  n = 2

  // Initial conditions
  X = 1; Y = 0.1; Z = 0.1
end
"""

#represilator
rep = """
model represilator
  species X, Y, Z

  // X and Y dynamics
  J0: -> X; kx*1/(1 + (Z/Kz)^n)
  J1: -> Y; ky*1/(1 + (X/Kx)^n)
  J2: X -> ; dx*X
  J3: Y -> ; dy*Y
  J4: -> Z; kz*1/(1 + (Y/Ky)^n)
  J5: Z -> ; dz*Z

  // Parameters
  kx = 1.5; ky = 1.5; kz = 1.5
  dx = 0.5; dy = 0.5; dz = 0.5
  Kx = 1.0; Ky = 1.0; Kz = 1.0
  n = 2

  // Initial conditions
  X = 1; Y = 0.1; Z = 0.1
end
"""

# Load model
r = te.loada(rep)

# Simulate from t=0 to t=50 with 200 points
result = r.simulate(0, 50, 200)

# Print first few results
print(result[:10])

# Plot dynamics
r.plot(title="C-1 type FFL with AND", xtitle="Time", ytitle="[X]")