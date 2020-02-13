#create a circuit with 1 qubit and 1 classical bit
# apply Pauli X gate on qubit q[0] 
# Measure the state - 

import sys
import logging
from qiskit import(
  QuantumCircuit,
  execute,
  Aer)
from qiskit.visualization import plot_histogram
# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Create a Quantum Circuit acting on the q register
# 1 qubit and 1 classical bit
circuit = QuantumCircuit(1, 1)

#Pauli gate on qubit 0
circuit.x(0)
circuit.measure(0,0)

# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count for 0 and 1 are:",counts)

# Draw the circuit
circuit.draw()


# plot the histogram, 0 flipped to 1 in all 1000 iterations
plot_histogram(job.result().get_counts(), color='midnightblue', title="New Histogram")
