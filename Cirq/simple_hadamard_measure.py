import cirq

# Create a qubit
qubit = cirq.LineQubit(0)

# Create a simple circuit: apply Hadamard, then measure
circuit = cirq.Circuit(
    cirq.H(qubit),
    cirq.measure(qubit, key='result')
)

# Simulate the circuit
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=10)

print("Results of measuring a Hadamard-applied qubit:")
print(result)
