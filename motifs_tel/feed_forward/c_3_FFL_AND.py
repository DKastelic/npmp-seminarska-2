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

if __name__ == "__main__":
  import tellurium as te
  r = te.loada(c_3_FFL_AND)
  result = r.simulate(0, 50, 200)
  print(result[:10])
  r.plot(title="C_3_FFL_AND", xtitle="Time", ytitle="[X]")
