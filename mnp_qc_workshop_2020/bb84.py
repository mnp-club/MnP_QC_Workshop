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


def check_message(message: str) -> None:
    if(message == "https://www.youtube.com/watch?v=ub82Xb1C8os"):
        print("Congratulations 🎉! You have succesfully decrypted the message which is "+message+". Do go ahead and try the link. Its worth it ;)")
    else:
        print("Looks like the message that you have devrypted isn't actually correct 😕 (could there be evasdroppers? probably not). Try again!")


def initialize_circuit() -> QuantumCircuit:
    circuit = QuantumCircuit(16)


    return circuit

def get_message():
    return "11111000111001001110010011100000111000111010101010111111101111111110011111100111111001111011111011101001111111111110010111100100111001011111001011110101101111101111001111111111111111011011111111100111111100011110010011110011111110001010111111100110101011011110010111110010101010001010001011001000111100101010000111010011101010001111111111100011"

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
    b = '0111100111100101'
    a = '0100000101011100'
    key = ''
    for i in range(16):
        if a[i]==b[i]:
            key = key + bits[i]
    if (key == "10010000"):
        print('So far, so good 🎉! You got the right bits!')
    else:
        print('Oops 😕! Not the right bits.')


def check_key(key: str) -> None:
    if (key == "10010000"):
        print('So far, so good 🎉! You got the right key!')
    else:
        print('Oops 😕! Not the right bits.')

def check_decrypted(decrypted: str) -> None:
    if (decrypted == "01101000011101000111010001110000011100110011101000101111001011110111011101110111011101110010111001111001011011110111010101110100011101010110001001100101001011100110001101101111011011010010111101110111011000010111010001100011011010000011111101110110001111010111010101100010001110000011001001011000011000100011000101000011001110000110111101110011"):
        print('So far, so good 🎉! You got the right decrypted message!')
    else:
        print('Oops 😕! Not the right bits.')
