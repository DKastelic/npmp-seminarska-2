import tellurium as te

#"C-1 FFL A"
c_1_FFL_AND = """
model C_1_FFL_AND
  species X, Y, Z

  // X and Y dynamics
  J0: -> X; kx
  J1: X -> X + Y; ky*(X/Kx)^n/(1 + (X/Kx)^n)
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



# Load model
r = te.loada(c_1_FFL_AND)

# Simulate from t=0 to t=50 with 200 points
result = r.simulate(0, 50, 200)

# Print first few results
print(result[:10])

# Plot dynamics
r.plot(title="C-1 type FFL with AND", xtitle="Time", ytitle="[X]")