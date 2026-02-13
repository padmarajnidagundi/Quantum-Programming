"""
Quantum Addition Program using Cirq
Demonstrates a simple quantum adder circuit to add two numbers
"""

import cirq

def quantum_half_adder():
    """
    Implements a quantum half adder circuit.
    Adds two bits (a, b) and produces sum and carry.
    """
    # Create qubits
    a = cirq.NamedQubit('a')  # First input bit
    b = cirq.NamedQubit('b')  # Second input bit
    sum_qubit = cirq.NamedQubit('sum')  # Sum output
    carry = cirq.NamedQubit('carry')  # Carry output
    
    # Create circuit
    circuit = cirq.Circuit()
    
    # Half adder logic:
    # Sum = a XOR b (CNOT gates)
    # Carry = a AND b (Toffoli gate)
    
    # For sum: XOR operation
    circuit.append(cirq.CNOT(a, sum_qubit))
    circuit.append(cirq.CNOT(b, sum_qubit))
    
    # For carry: AND operation (Toffoli/CCNOT gate)
    circuit.append(cirq.CCNOT(a, b, carry))
    
    # Measure the results
    circuit.append(cirq.measure(sum_qubit, key='sum'))
    circuit.append(cirq.measure(carry, key='carry'))
    
    return circuit, [a, b, sum_qubit, carry]


def add_two_bits(bit_a, bit_b):
    """
    Add two bits using quantum circuit.
    
    Args:
        bit_a: First bit (0 or 1)
        bit_b: Second bit (0 or 1)
    
    Returns:
        Tuple of (sum, carry)
    """
    circuit, qubits = quantum_half_adder()
    a, b, sum_qubit, carry = qubits
    
    # Initialize input qubits based on input values
    init_circuit = cirq.Circuit()
    if bit_a == 1:
        init_circuit.append(cirq.X(a))
    if bit_b == 1:
        init_circuit.append(cirq.X(b))
    
    # Combine initialization and adder circuit
    full_circuit = init_circuit + circuit
    
    # Simulate
    simulator = cirq.Simulator()
    result = simulator.run(full_circuit, repetitions=1)
    
    # Extract results
    sum_result = result.measurements['sum'][0][0]
    carry_result = result.measurements['carry'][0][0]
    
    return sum_result, carry_result


def main():
    """
    Demonstrate quantum addition for all possible 2-bit inputs.
    """
    print("Quantum Half Adder - Adding Two Bits")
    print("=" * 40)
    print()
    
    # Test all possible combinations
    for a in [0, 1]:
        for b in [0, 1]:
            sum_bit, carry_bit = add_two_bits(a, b)
            classical_result = a + b
            print(f"{a} + {b} = {carry_bit}{sum_bit} (binary)")
            print(f"   Classical result: {classical_result}")
            print(f"   Quantum result: {carry_bit * 2 + sum_bit}")
            print()
    
    # Display the circuit
    print("\nQuantum Half Adder Circuit:")
    print("=" * 40)
    circuit, _ = quantum_half_adder()
    print(circuit)


if __name__ == "__main__":
    main()
