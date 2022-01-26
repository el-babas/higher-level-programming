#!/usr/bin/python3
""" This page content.

    Functions
        lazy_matrix_mul
"""
import numpy as npy


def lazy_matrix_mul(m_a, m_b):
    """ Function - That multiplies 2 matrices
    by using the module NumPy

    Args:
        m_a([[],[]]): matriz a
        m_b([[],[]]): matriz b

    Returns:
        Result of the multiplication

    """

    return (npy.matmul(m_a, m_b))
