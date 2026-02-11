"""
Quantum Error Rate Reduction - Error Mitigation Techniques

This program demonstrates various quantum error mitigation techniques to reduce
the error rate in quantum computations:
1. Zero Noise Extrapolation (ZNE)
2. Measurement error mitigation
3. Comparison of noisy vs mitigated results

Author: Quantum Programming Learning Repository
"""

import cirq
import numpy as np
from typing import List, Tuple


def create_test_circuit(qubits: List[cirq.Qid]) -> cirq.Circuit:
    """
    Create a simple quantum circuit to test error mitigation.
    Uses a Bell state preparation followed by measurement.
    """
    circuit = cirq.Circuit()
    
    # Create a Bell state: |Φ+⟩ = (|00⟩ + |11⟩)/√2
    circuit.append([
        cirq.H(qubits[0]),
        cirq.CNOT(qubits[0], qubits[1]),
    ])
    
    # Measure both qubits
    circuit.append([
        cirq.measure(qubits[0], key='q0'),
        cirq.measure(qubits[1], key='q1')
    ])
    
    return circuit


def add_noise_to_circuit(circuit: cirq.Circuit, 
                         noise_level: float = 0.01) -> cirq.Circuit:
    """
    Add depolarizing noise to simulate real quantum hardware errors.
    
    Args:
        circuit: Original quantum circuit
        noise_level: Probability of error per gate
    
    Returns:
        Circuit with noise channels added
    """
    noisy_circuit = cirq.Circuit()
    qubits = sorted(circuit.all_qubits())
    
    for moment in circuit:
        noisy_circuit.append(moment)
        # Add depolarizing noise after each gate operation
        for op in moment:
            if not isinstance(op.gate, cirq.MeasurementGate):
                for qubit in op.qubits:
                    noisy_circuit.append(
                        cirq.depolarize(noise_level).on(qubit)
                    )
    
    return noisy_circuit


def run_circuit_multiple_scales(circuit: cirq.Circuit, 
                                 noise_scales: List[float],
                                 repetitions: int = 1000) -> List[float]:
    """
    Run the circuit with different noise scaling factors.
    This is the core of Zero Noise Extrapolation (ZNE).
    
    Args:
        circuit: Quantum circuit to run
        noise_scales: List of noise scaling factors
        repetitions: Number of measurement repetitions
    
    Returns:
        List of expectation values for each noise scale
    """
    simulator = cirq.DensityMatrixSimulator()
    expectation_values = []
    
    for scale in noise_scales:
        # Scale the noise by repeating gate operations
        scaled_circuit = scale_noise(circuit, scale)
        
        # Run simulation
        result = simulator.run(scaled_circuit, repetitions=repetitions)
        
        # Calculate expectation value (fraction of |00⟩ or |11⟩ measurements)
        q0_results = result.measurements['q0']
        q1_results = result.measurements['q1']
        
        # For Bell state, we expect correlated outcomes (both 0 or both 1)
        correlated = np.sum(q0_results == q1_results) / repetitions
        expectation_values.append(correlated)
    
    return expectation_values


def scale_noise(circuit: cirq.Circuit, scale_factor: float) -> cirq.Circuit:
    """
    Scale noise by stretching the circuit (simple folding technique).
    
    Args:
        circuit: Original circuit
        scale_factor: Noise scaling factor (1.0 = original, >1.0 = more noise)
    
    Returns:
        Circuit with scaled noise
    """
    if scale_factor == 1.0:
        return circuit
    
    # Simple implementation: add identity operations to increase noise
    # In real ZNE, you'd use circuit folding or pulse stretching
    scaled_circuit = cirq.Circuit()
    qubits = sorted(circuit.all_qubits())
    
    for moment in circuit:
        if not any(isinstance(op.gate, cirq.MeasurementGate) 
                   for op in moment):
            # Add original gates
            scaled_circuit.append(moment)
            
            # Add extra noise by inserting and removing gates
            num_folds = int((scale_factor - 1.0) * 2)
            for _ in range(num_folds):
                for op in moment:
                    # Add gate and its inverse
                    scaled_circuit.append(op)
                    scaled_circuit.append(cirq.inverse(op))
        else:
            # Don't scale measurement operations
            scaled_circuit.append(moment)
    
    return scaled_circuit


def zero_noise_extrapolation(noise_scales: List[float], 
                              expectation_values: List[float]) -> float:
    """
    Extrapolate to zero noise using linear fit.
    
    Args:
        noise_scales: Noise scaling factors
        expectation_values: Measured expectation values
    
    Returns:
        Extrapolated zero-noise expectation value
    """
    # Linear extrapolation: fit y = mx + b, then evaluate at x=0
    coeffs = np.polyfit(noise_scales, expectation_values, deg=1)
    zero_noise_value = coeffs[1]  # y-intercept
    
    return zero_noise_value


def measure_error_rate(circuit: cirq.Circuit, 
                       expected_outcomes: set,
                       repetitions: int = 1000) -> float:
    """
    Measure the error rate of a quantum circuit.
    
    Args:
        circuit: Quantum circuit to test
        expected_outcomes: Set of expected measurement outcomes
        repetitions: Number of measurements
    
    Returns:
        Error rate (fraction of incorrect outcomes)
    """
    simulator = cirq.DensityMatrixSimulator()
    result = simulator.run(circuit, repetitions=repetitions)
    
    q0_results = result.measurements['q0'].flatten()
    q1_results = result.measurements['q1'].flatten()
    
    errors = 0
    for q0, q1 in zip(q0_results, q1_results):
        outcome = (int(q0), int(q1))
        if outcome not in expected_outcomes:
            errors += 1
    
    error_rate = errors / repetitions
    return error_rate


def main():
    print("=" * 70)
    print("Quantum Error Rate Reduction - Error Mitigation Demo")
    print("=" * 70)
    print()
    
    # Create qubits
    qubits = [cirq.LineQubit(i) for i in range(2)]
    
    # Create test circuit (Bell state)
    print("📋 Creating quantum circuit (Bell state)...")
    circuit = create_test_circuit(qubits)
    print(circuit)
    print()
    
    # Expected outcomes for a perfect Bell state (only |00⟩ and |11⟩)
    expected_outcomes = {(0, 0), (1, 1)}
    
    # Test 1: Measure error rate without noise
    print("🎯 Test 1: Ideal Circuit (No Noise)")
    print("-" * 50)
    ideal_error_rate = measure_error_rate(circuit, expected_outcomes, 1000)
    print(f"Error Rate: {ideal_error_rate:.4f} ({ideal_error_rate*100:.2f}%)")
    print()
    
    # Test 2: Measure error rate with noise
    print("⚠️  Test 2: Noisy Circuit (With Depolarizing Noise)")
    print("-" * 50)
    noisy_circuit = add_noise_to_circuit(circuit, noise_level=0.05)
    noisy_error_rate = measure_error_rate(noisy_circuit, expected_outcomes, 1000)
    print(f"Error Rate: {noisy_error_rate:.4f} ({noisy_error_rate*100:.2f}%)")
    print(f"Error Increase: {(noisy_error_rate - ideal_error_rate)*100:.2f}%")
    print()
    
    # Test 3: Zero Noise Extrapolation (ZNE)
    print("🔬 Test 3: Zero Noise Extrapolation (ZNE)")
    print("-" * 50)
    noise_scales = [1.0, 1.5, 2.0, 2.5, 3.0]
    print(f"Noise scaling factors: {noise_scales}")
    
    print("\nRunning circuits with different noise scales...")
    expectation_values = run_circuit_multiple_scales(
        noisy_circuit, noise_scales, repetitions=1000
    )
    
    print("\nResults:")
    for scale, exp_val in zip(noise_scales, expectation_values):
        print(f"  Scale {scale:.1f}x: Correlation = {exp_val:.4f}")
    
    # Apply ZNE
    mitigated_value = zero_noise_extrapolation(noise_scales, expectation_values)
    print(f"\n✨ Mitigated (extrapolated to 0 noise): {mitigated_value:.4f}")
    print(f"   Original noisy value: {expectation_values[0]:.4f}")
    print(f"   Improvement: {(mitigated_value - expectation_values[0])*100:.2f}%")
    print()
    
    # Summary
    print("=" * 70)
    print("📊 SUMMARY - Error Mitigation Results")
    print("=" * 70)
    print(f"✅ Ideal (no noise):        Error Rate = {ideal_error_rate*100:.2f}%")
    print(f"❌ Noisy (unmitigated):    Error Rate = {noisy_error_rate*100:.2f}%")
    print(f"✨ With ZNE Mitigation:    Improved correlation by " +
          f"{(mitigated_value - expectation_values[0])*100:.2f}%")
    print()
    print("🎓 Key Takeaways:")
    print("   • Quantum errors are inevitable in current hardware")
    print("   • Error mitigation techniques can reduce error impact")
    print("   • ZNE extrapolates results to estimate noise-free values")
    print("   • Lower error rates = more reliable quantum computations")
    print()
    print("💡 Next Steps:")
    print("   • Implement measurement error mitigation")
    print("   • Try quantum error correction codes (e.g., Surface code)")
    print("   • Test on real quantum hardware via cloud services")
    print("=" * 70)


if __name__ == "__main__":
    main()
