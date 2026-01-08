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
  dx = 0.2; dy = 0.2; dz = 0.2
  Kx = 1.0; Ky = 1.0; Kz = 1.0
  n = 2

  // Initial conditions
  X = 1; Y = 0.1; Z = 0.1
end
"""

if __name__ == "__main__":
  import tellurium as te
  r = te.loada(rep)
  result = r.simulate(0, 50, 200)
  print(result[:10])
  r.plot(title="represilator", xtitle="Time", ytitle="[X]")
