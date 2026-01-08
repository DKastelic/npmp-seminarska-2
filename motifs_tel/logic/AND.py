AND = """
model AND
  species X, Y, Z

  // X and Y dynamics
  J0: X -> ; dx*X
  J1: Y -> ; dy*Y
  J2: Z -> ; dz*Z
  
  J3: -> Z; kz * (X/Kx)^n/(1 + (X/Kx)^n) * (Y/Ky)^n/(1 + (Y/Ky)^n)

  // Parameters
  kz = 2
  dx = 0; dy = 0; dz = 0.5
  Kx = 1.0; Ky = 1.0; Kz = 1.0
  n = 2

  // Initial conditions
  X = 1; Y = 0.99; Z = 0.5
end
"""

if __name__ == "__main__":
  import tellurium as te
  r = te.loada(AND)
  result = r.simulate(0, 50, 200)
  print(result[:10])
  r.plot(title="AND (X=1, Y=0.99)", xtitle="Time", ytitle="[X]")