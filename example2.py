#using single bit gate u2 and u3 in a circuit

import sys, time, math
import qiskit
import logging

# Create a Quantum Circuit acting on the q register, 5 qubits and 5 classical bits
circuit = QuantumCircuit(5, 5)

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')


logging.getLogger('qiskit.transpiler').setLevel(logging.DEBUG)

circuit.u2(-4 * math.pi/3, 2*math.pi, 0)
circuit.u2(-3 * math.pi/2, 2*math.pi, 0)
circuit.u3(-math.pi,0, -math.pi, 0)
circuit.u3(-math.pi,0, -math.pi/2, 0)
circuit.u2(math.pi, -math.pi/2, 0)
circuit.u3(-math.pi,0, -math.pi/2, 0)


circuit.measure(0,0)
circuit.measure(1,1)
circuit.measure(2,2)
#circuit.measure(3,3)
#circuit.measure(4,4)
# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)

# Draw the circuit
circuit.draw()

plot_histogram(counts)
