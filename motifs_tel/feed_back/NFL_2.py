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

if __name__ == "__main__":
  import tellurium as te
  r = te.loada(NFL_2)
  result = r.simulate(0, 50, 200)
  print(result[:10])
  r.plot(title="NFL_2", xtitle="Time", ytitle="[X]")
