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
  X = 1.2; Y = 1.1
  // X = 1.2; Y = 1.3
end
"""

if __name__ == "__main__":
  import tellurium as te

  # Load and simulate PFL_2
  r2 = te.loada(PFL_2)
  result2 = r2.simulate(0, 50, 200)
  print("PFL_2:", result2[:10])

  r2.plot(title="Positive feedback loop, mutual repression (switch)", xtitle="Time", ytitle="[X]")