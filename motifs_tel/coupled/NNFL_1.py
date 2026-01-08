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

if __name__ == "__main__":
  import tellurium as te
  r = te.loada(NNFL_1)
  result = r.simulate(0, 50, 200)
  print(result[:10])
  r.plot(title="NNFL", xtitle="Time", ytitle="[X]")
