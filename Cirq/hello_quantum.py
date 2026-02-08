import cirq

def main():
    print("Hello Quantum!")

    # Create a simple quantum circuit with one qubit
    qubit = cirq.LineQubit(0)
    circuit = cirq.Circuit(
        cirq.H(qubit),  # Apply Hadamard gate
        cirq.measure(qubit, key='result')  # Measure the qubit
    )
    print("Circuit:")
    print(circuit)

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=5)
    print("Measurement results:")
    print(result)

if __name__ == "__main__":
    main()