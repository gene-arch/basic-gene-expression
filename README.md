# Gene Expression Simulation using Tellurium

This is a beginner-level synthetic biology project that uses the Tellurium library in Python to simulate a basic gene expression system. The model tracks the dynamics of mRNA and protein concentration over time, providing a foundation for more advanced biological circuit modeling.

## Project Overview

This project simulates a single gene expression system where:
- A gene is transcribed into mRNA
- mRNA is translated into protein
- Both mRNA and protein degrade over time

This is a basic foundational model used in synthetic biology studies.

## Files

- `gene_expression_simulation.py`: The main script that sets up and runs the simulation using Tellurium.
- `README.md`: This documentation file describing the project.
- `requirements.txt.`

## Requirements

Install Tellurium using the following command:

```bash
pip install tellurium
```

Make sure Python 3.7 to 3.11 is installed. Tellurium does not currently support Python 3.12+.

## How to Run

1. Open your terminal or Anaconda prompt.
2. Navigate to the project directory.
3. Run the script:

```bash
python gene_expression_simulation.py
```

This will generate a plot showing the mRNA and protein concentration over time.

## Output

The output of the simulation is a graph showing the concentration profiles of mRNA and protein. The simulation uses deterministic modeling (ODE-based) with Tellurium's Antimony and roadrunner backend.

## License

This project is open-source and free to use for educational and learning purposes. You may modify and build upon it for personal or academic use.

## Reference

Inspired by synthetic biology foundational material and hands-on modeling using Tellurium, and based on introductory Coursera courses such as "Engineering Genetic Ciruits" on Coursera.