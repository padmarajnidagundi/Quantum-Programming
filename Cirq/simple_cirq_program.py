# Simple Cirq Program: Create and Measure a Qubit

import cirq

# Create a qubit
qubit = cirq.LineQubit(0)

# Create a circuit
circuit = cirq.Circuit(
    cirq.H(qubit),      # Apply Hadamard gate
    cirq.measure(qubit) # Measure the qubit
)

# Simulate the circuit
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=10)

print("Measurement results:")
print(result)
