import os
import pickle
import json
from urllib.parse import urljoin
from typing import Tuple
from html import escape as html_escape

import requests
from qiskit import QuantumCircuit
from qiskit.qobj import Qobj
from qiskit.assembler import disassemble
from IPython.display import display, HTML
import numpy as np

bb84_data = np.load(os.path.join(os.path.dirname(__file__), 'bb84_data.npy'))

def check_message(message: str) -> None:
    if(message == bb84_data[5]):
        print("Congratulations 🎉! You have succesfully decrypted the message which is "+message+". Do go ahead and try the link. Its worth it ;)")
    else:
        print("Looks like the message that you have devrypted isn't actually correct 😕 (could there be evasdroppers? probably not). Try again!")


def initialize_circuit() -> QuantumCircuit:
    circuit = QuantumCircuit(16)


    return circuit

def get_message():
    return bb84_data[0]

def alice_prepare_qubit(qubit_index: int) -> QuantumCircuit:
    qc = QuantumCircuit(1, 1)

    x_indices = [0, 4, 6, 10, 15]  # noqa
    if qubit_index in x_indices:
        qc.x(0)

    h_indices = [1, 7, 9, 11, 12, 13]  # noqa
    if qubit_index in h_indices:
        qc.h(0)

    return qc


def check_bits(bits: str) -> None:
    b = bb84_data[3]
    a = bb84_data[4]
    key = ''
    for i in range(16):
        if a[i]==b[i]:
            key = key + bits[i]
    if (key == bb84_data[2]):
        print('So far, so good 🎉! You got the right bits!')
    else:
        print('Oops 😕! Not the right bits.')


def check_key(key: str) -> None:
    if (key == bb84_data[2]):
        print('So far, so good 🎉! You got the right key!')
    else:
        print('Oops 😕! Not the right bits.')

def check_decrypted(decrypted: str) -> None:
    if (decrypted == bb84_data[1]):
        print('So far, so good 🎉! You got the right decrypted message!')
    else:
        print('Oops 😕! Not the right bits.')
