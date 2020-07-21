# Importing standard Qiskit libraries and configuring account
from qiskit import *
from qiskit.compiler import *
from qiskit.tools.jupyter import *
import scipy
import numpy as np
import qiskit.quantum_info as qi
from cmath import sqrt
import os
#Defining required functions for giving unitary and checking circuit


epsilon = 0.01
max_cost = 1200

def without_global_phase(matrix: np.ndarray, atol: float = 1e-8) :
    phases1 = np.angle(matrix[abs(matrix) > atol].ravel(order='F'))
    if len(phases1) > 0:
        matrix = np.exp(-1j * phases1[0]) * matrix
    return matrix

def get_unitary() :
    m = np.array(np.load(os.path.join(os.path.dirname(__file__), 'U.npy'))).reshape(16,16)
    return m

def norm(unitary_a: np.ndarray, unitary_b: np.ndarray) :
    return np.linalg.norm(without_global_phase(unitary_b)-without_global_phase(unitary_a), ord=2)

def cost_of_circuit(circuit: QuantumCircuit):
    complexity = 0
    for instr, _, _ in circuit.data :
        if instr.name == 'u3':
            complexity += 1
        elif instr.name == 'cx':
            complexity += 10
        else:
            None
            raise ValueError(f'unexpected instruction {instr}. '
                             'Only u3 or cnot gates can be taken into '
                             'consideration')
    return complexity

def check_circuit(circuit: QuantumCircuit) :
    V = qi.Operator(circuit).data
    circuit2 = QuantumCircuit(4)
    circuit2.unitary(get_unitary(),circuit2.qubits)
    U = qi.Operator(circuit2).data
    diff = norm(V,U)
    cost = cost_of_circuit(circuit)
    print("||U - V||^2 = "+str(diff))
    print("Cost of your circuit is "+str(cost))
    if diff <= epsilon and cost <= max_cost :
        print("Good news! Your circuit satisfies the bounds and seems right :) , you may go ahead and submit this notebook or you can also try to lower the cost even more.")
    if diff <= epsilon and cost > max_cost :
        print("Unfortunately, it looks like the circuit you have made is a tad bit costlier than it should have been. Try again!")
    if diff > epsilon :
        print("Looks like your circuit is not executing the given unitary without a noticable error. Try again!")
