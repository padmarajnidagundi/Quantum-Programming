# Simple Quantum Cryptography Example: Quantum Key Distribution (BB84 Protocol)
# This is a conceptual simulation of the BB84 protocol using Cirq.
# In real-world quantum cryptography, this protocol is used for secure key exchange.

import cirq
import numpy as np

# Number of bits/qubits to send
num_bits = 8

# Randomly generate sender's bits and bases
alice_bits = np.random.randint(2, size=num_bits)
alice_bases = np.random.randint(2, size=num_bits)  # 0: Z-basis, 1: X-basis

# Randomly generate receiver's bases
bob_bases = np.random.randint(2, size=num_bits)

# Prepare and measure qubits
key = []
for i in range(num_bits):
    qubit = cirq.LineQubit(0)
    circuit = cirq.Circuit()
    # Prepare qubit in Alice's basis
    if alice_bases[i] == 0:
        if alice_bits[i] == 1:
            circuit.append(cirq.X(qubit))
    else:
        if alice_bits[i] == 1:
            circuit.append(cirq.X(qubit))
        circuit.append(cirq.H(qubit))
    # Bob measures in his basis
    if bob_bases[i] == 1:
        circuit.append(cirq.H(qubit))
    circuit.append(cirq.measure(qubit, key='m'))
    # Simulate
    result = cirq.Simulator().run(circuit, repetitions=1)
    measured_bit = int(result.measurements['m'][0][0])
    # If bases match, keep the bit
    if alice_bases[i] == bob_bases[i]:
        key.append(measured_bit)

print("Simulated BB84 Quantum Key (shared bits):", key)
