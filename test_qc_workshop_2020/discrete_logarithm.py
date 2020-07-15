from qiskit import *
from qiskit.compiler import *
from qiskit.tools.jupyter import *
import scipy
import numpy as np
from IPython.display import display, Math, Latex
import qiskit.quantum_info as qi
from cmath import sqrt

def qft_dagger(n):
	"""n-qubit QFTdagger the first n qubits in circ"""
	qc = QuantumCircuit(n)
	# Don't forget the Swaps!
	for qubit in range(n//2):
		qc.swap(qubit, n-qubit-1)
	for j in range(n):
		for m in range(j):
			qc.cu1(-np.pi/float(2**(j-m)), m, j)
		qc.h(j)
	qc.name = "QFT†"
	return qc

def __c_amod15(power):
	"""Controlled multiplication by a mod 15"""
	U = QuantumCircuit(4)        
	for iteration in range(power):
		U.swap(0,1)
		U.swap(1,2)
		U.swap(2,3)
	U = U.to_gate()
	U.name = "a^%i mod 15" % (power)
	c_U = U.control()
	return c_U

def __c_bmod15(power):
	"""Controlled multiplication by b mod 15"""
	U = QuantumCircuit(4)        
	for iteration in range(power):
		U.swap(2,3)
		U.swap(1,2)
		U.swap(0,1)
	U = U.to_gate()
	U.name = "b^%i mod 15" % (power)
	c_U = U.control()
	return c_U

def oracle():
	qc = QuantumCircuit(10)
	for q in range(3):
	    qc.append(__c_amod15(2**q), [q] + [i+6 for i in range(4)])
	for q in range(3,6):
	    qc.append(__c_bmod15(2**(q-3)), [q] + [i+6 for i in range(4)])
	g = qc.to_gate()
	g.name = "Oracle"
	return g

def __checkerdl(s,a,b):
	val = True
	reason = "The following value(s) failed to match:"
	if s != 3:
		val = False
		reason += " s"	
	if a != 2:
		if(val == False):
			reason += ", a"
		else:
			reason += " a"
		val = False		
	if b != 8:
		if(val == False):
			reason += ", b"
		else:
			reason += " b"
		val = False
	return val,reason

def check_answer(s,a,b):
	val, reason = __checkerdl(s,a,b)
	if val == True:
		print("All your values are correct :) You may go ahead and submit the notebook")
	else:
		print("Whoops, your answer seems off. "+reason)