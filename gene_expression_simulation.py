import tellurium as te

# Define the gene expression model
model = te.loada("""
    // Species
    species I, M, P;

    // Reactions
    J1: -> M; k1*I;
    J2: M -> ; k2*M;
    J3: -> P; k3*M;

    // Initial Conditions
    I = 10; M = 0; P = 0;

    // Rate Constants
    k1 = 0.5; k2 = 0.1; k3 = 2;
""")

# Simulate and plot
result = model.simulate(0, 50, 100)
model.plot(result)