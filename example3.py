#Generate a 8 bit random number from 3 qubits

import qiskit
import sys, time

logging.getLogger('qiskit.transpiler').setLevel(logging.DEBUG)

# create a 3 qubit circuit,
circuit = QuantumCircuit(3,3)

# apply hadamard gate on all three qubits 
for i in range(3):
    circuit.h(i)

for i in range(3):
    circuit.measure(i,i)
    
# execute circuit for 1000 times
shots = 1024
# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=shots)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count:",counts)

# shots/2**3 is average count for 8 states and all are equally likely
# if the frequency of a particular state is greater than above value spit out 1
# random number is generated concatenating the bits from each state
# e.g if following counts are generated after measurement
# Total count are: {'011': 132, '001': 141, '000': 118, '101': 126, '110': 117, '111': 131, '010': 129, '100': 130}
# and average frequency is 1024/2**3 = 128
# spit out '1' for each value where frequency > 128 else 0 -  11000111 (199 in decimal)
bits = ""
for val in counts.values():
    if val > shots /2**3 :
        bits += "1"
    else :
        bits += "0"
        
print(bits)

# Draw the circuit
circuit.draw()

plot_histogram(counts)
