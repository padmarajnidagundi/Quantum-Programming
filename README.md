# Quantum Programming: Learning Notes & Resources

![Quantum Computing Badge](https://img.shields.io/badge/Quantum-Programming-blueviolet)
![License](https://img.shields.io/github/license/padmarajnidagundi/Quantum-Programming)
![Last Commit](https://img.shields.io/github/last-commit/padmarajnidagundi/Quantum-Programming)

> **Keywords:** quantum computing, quantum programming, Qiskit, Cirq, Q#, PyQuil, PennyLane, quantum algorithms, quantum circuits, quantum learning, quantum frameworks


## 🚀 Overview

## 🗂️ Repository Structure

```
Quantum-Programming/
│
├── Qiskit/        # Programs and notes for IBM Qiskit
├── Cirq/          # Programs and notes for Google Cirq
├── QSharp/        # Programs and notes for Microsoft Q#
├── PyQuil/        # Programs and notes for Rigetti PyQuil
├── PennyLane/     # Programs and notes for PennyLane
├── LICENSE
├── README.md
```

Welcome to **Quantum Programming** — a curated collection of learning notes, guides, and resources for anyone interested in quantum computing and quantum programming. This repository is designed to help beginners and enthusiasts understand the basics, explore top frameworks, and start coding for quantum computers.

---

## 📚 Table of Contents

1. [What Are Quantum Computers?](#what-are-quantum-computers)
2. [Quantum Programming Basics](#quantum-programming-basics)
3. [Top Quantum Programming Languages & Frameworks](#top-quantum-programming-languages--frameworks)
4. [Recommended IDEs & Tools](#recommended-ides--tools)
5. [Contributing](#contributing)
6. [Author & Contact](#author--contact)

---

## What Are Quantum Computers?

**Classical computers** (phones, laptops) work with bits that are either 0 or 1, solving problems step-by-step.

**Quantum computers** use qubits, which can be 0, 1, or both at the same time (a quantum phenomenon called *superposition*). This allows them to explore many possible solutions simultaneously.

**Quantum computers excel at:**

- Simulating molecules and materials (e.g., cleaner fertilizers, better batteries)
- Testing chemical reactions virtually (faster drug discovery)
- Solving complex problems that would take classical computers years or centuries

---

## Quantum Programming Basics

**Quantum programming** means writing instructions for a quantum computer instead of a classical one.

- In classical programming, you tell the computer what to do with 0s and 1s.
- In quantum programming, you instruct the computer how to work with qubits, which can be 0 and 1 at the same time.

**Key differences:**
- You set up a problem; the quantum computer explores many answers at once
- You measure the system to get the final result

---


## Top Quantum Programming Languages & Frameworks

1. **Qiskit (IBM)** – *Python-based*
   - Most popular framework for writing quantum programs (Python)
   - Free: Open source, free IBM quantum hardware access (cloud)
   - Paid: Optional premium compute credits
   - Good for: Beginners, learning quantum circuits

2. **Cirq (Google)** – *Python library*
   - Python for defining quantum circuits, especially for Google’s hardware
   - Free: Open source
   - Paid: Hardware access may cost
   - Good for: Low-level circuit design control

## 📝 Your First Quantum Program: Hello Quantum (Cirq Example)

Here's how to write and run your first quantum program using Cirq:

1. **Create a file:**
    - Go to the `Cirq/` folder.
    - Create a new file named `hello_quantum.py`.

2. **Paste this code:**

    ```python
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
    ```

3. **Run the program:**
    - Open a terminal in the `Cirq/` folder.
    - Run: `python hello_quantum.py`

You should see output like:

```
Hello Quantum!
Circuit:
0: ───H───M('result')───
Measurement results:
result=...
```

This is your first step in quantum programming!

3. **Q# (Microsoft Q-Sharp)** – *Standalone language*
   - Quantum-only language (not Python) by Microsoft
   - Free: Part of Quantum Development Kit
   - Paid: Azure Quantum hardware access may cost
   - Good for: Learning quantum algorithms with full tooling

4. **PyQuil & Quil (Rigetti)** – *Python + low-level backend*
   - Python interface (PyQuil) for the Quil instruction language (Rigetti systems)
   - Free: Libraries and simulators
   - Paid: Real Rigetti hardware access may cost
   - Good for: Hybrid quantum/classical programs

5. **Other Useful Tools**
   - **PennyLane** – Python for quantum machine learning (free)
   - **OpenQASM** – Low-level assembly language for quantum tools
   - **Guppy** – New Python-based language to simplify quantum coding (free)

   ---

## 🖥️ Top 5 Free Remote Online Quantum Computers for Program Execution

1. **IBM Quantum Experience (Qiskit Cloud)**  
   Free access to real IBM quantum computers and simulators for running quantum programs.  
   [https://quantum-computing.ibm.com/](https://quantum-computing.ibm.com/)

2. **Microsoft Azure Quantum (Free Tier)**  
   Free credits for running quantum programs on IonQ, Quantinuum, and simulators via Azure Quantum.  
   [https://azure.microsoft.com/en-us/products/quantum/](https://azure.microsoft.com/en-us/products/quantum/)

3. **Amazon Braket (Free Tier)**  
   Free access to quantum hardware (IonQ, Rigetti, OQC) and simulators with AWS Free Tier credits.  
   [https://aws.amazon.com/braket/](https://aws.amazon.com/braket/)

4. **QuTech Quantum Inspire**  
   Free access to real quantum processors and simulators for program execution (Netherlands-based).  
   [https://www.quantum-inspire.com/](https://www.quantum-inspire.com/)

5. **Rigetti Forest Cloud (PyQuil)**  
   Free access to Rigetti’s quantum virtual machine and limited real hardware for program execution.  
   [https://www.rigetti.com/forest](https://www.rigetti.com/forest)


---

## 🧮 Top 15 Quantum Algorithms & Use Cases

| Algorithm | Use Case |
|-----------|---------|
| **Shor’s Algorithm** | Integer factorization (breaking RSA encryption) |
| **Grover’s Algorithm** | Unstructured search (database search, NP-complete problems) |
| **Quantum Fourier Transform (QFT)** | Basis for many quantum algorithms (period finding, phase estimation) |
| **Quantum Phase Estimation** | Estimating eigenvalues (chemistry, physics simulations) |
| **Deutsch-Jozsa Algorithm** | Distinguishing between constant and balanced functions (demonstrates quantum speedup) |
| **Simon’s Algorithm** | Finding hidden periods in functions (precursor to Shor’s) |
| **Quantum Approximate Optimization Algorithm (QAOA)** | Solving combinatorial optimization problems (e.g., Max-Cut) |
| **Variational Quantum Eigensolver (VQE)** | Finding ground state energies in molecules (quantum chemistry) |
| **Quantum Machine Learning (QML) Algorithms** | Pattern recognition, classification, regression (quantum-enhanced ML) |
| **Quantum Walks** | Graph traversal, search, and optimization |
| **Amplitude Amplification** | Generalization of Grover’s (speeding up probabilistic algorithms) |
| **Quantum Counting** | Counting the number of solutions to a problem (database, search) |
| **Harrow-Hassidim-Lloyd (HHL) Algorithm** | Solving systems of linear equations (quantum linear algebra) |
| **Quantum Principal Component Analysis (qPCA)** | Dimensionality reduction in quantum data (quantum ML) |
| **Quantum Error Correction Codes** | Protecting quantum information from decoherence and errors |

---

## Recommended IDEs & Tools

- **VS Code** — Free, popular for quantum coding (Qiskit, Q# extensions)
- **Jupyter Notebooks** — Free, interactive browser notebooks (great for Python frameworks)
- **Visual Studio** — Free Community Edition supports Q#; paid versions offer more features
- **Quantum Development Kit (QDK)** — Free Microsoft toolset with Q# debugging


Most quantum languages are Python-based or run in free environments like VS Code/Jupyter. Paid options are mainly for access to real quantum hardware.

---

## 🌐 Top 5 Free Online Quantum Computer Resources

1. **IBM Quantum Experience (Qiskit)**  
   Free access to real quantum computers and simulators, with tutorials and a vibrant community.  
   [https://quantum-computing.ibm.com/](https://quantum-computing.ibm.com/)

2. **Microsoft Quantum Development Kit (QDK) & Q#**  
   Free tools, documentation, and online simulators for learning and coding quantum algorithms.  
   [https://learn.microsoft.com/en-us/azure/quantum/](https://learn.microsoft.com/en-us/azure/quantum/)

3. **Google Quantum AI (Cirq)**  
   Free Python library, code labs, and cloud simulators for building and running quantum circuits.  
   [https://quantumai.google/](https://quantumai.google/)

4. **Quantum Country**  
   Free interactive essays and spaced-repetition flashcards for deeply learning quantum computing concepts.  
   [https://quantum.country/](https://quantum.country/)

5. **Qiskit Textbook**  
   Free, open-source online textbook with hands-on quantum programming exercises and theory.  
   [https://qiskit.org/textbook/](https://qiskit.org/textbook/)

---

## Contributing

We welcome first-time contributors! If you’re new to open source, look for issues tagged with `good-first-issue` or `help-wanted`. We provide mentorship and guidance to help you succeed.

**How to contribute:**
- Fork this repo and create your branch
- Make your changes and submit a pull request
- For questions, open a [GitHub Discussion](https://github.com/padmarajnidagundi/Quantum-Programming/discussions)
- Report bugs via [GitHub Issues](https://github.com/padmarajnidagundi/Quantum-Programming/issues)

---

## Author & Contact

**Padmaraj Nidagundi**  
*Quantum Computing Enthusiast, Open Source Mentor*  
📧 Email: padmaraj.nidagundi@gmail.com  
🌐 [LinkedIn](https://www.linkedin.com/in/padmarajnidagundi/)  
📝 [Personal Blog](https://padmarajnidagundi.medium.com/)  

**Response time:** Typically 24-48 hours

---

## ⭐ Why Star This Repo?

- Stay updated with the latest in quantum programming
- Access curated learning resources
- Join a growing community of quantum enthusiasts

**Thank you for making quantum programming accessible to everyone!** 🚀
