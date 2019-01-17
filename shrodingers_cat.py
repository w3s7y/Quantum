import qiskit

# 5 Qubit system (the radioactive source, the giger counter, the hammer, the vial of poison and... the cat)
qr = qiskit.QuantumRegister(4)
cr = qiskit.ClassicalRegister(4)
c = qiskit.QuantumCircuit(qr, cr)

# Hadamard the 4th bit (radioactive source).
c.h(qr[3])

# CNOT the radiation source to the hammer.
c.cx(qr[3], qr[2])

# CNOT the hammer to the vial
c.cx(qr[2], qr[1])

# CNOT the poison vial to the poor cat!
c.cx(qr[1], qr[0])

# Measure!!!
c.measure(qr, cr)

# get a backend (sim), execute it, print result.
print(qiskit.execute(c, qiskit.BasicAer.get_backend('qasm_simulator')).result().get_counts())
