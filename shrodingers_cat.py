import qiskit
import sys

# 5 Qubit system (the radioactive source (alpha decay), the giger counter (registered decay)
# # The hammer (moved), the vial of poison (glass broken) and... the cat (dead or alive!)
qr = qiskit.QuantumRegister(5)
cr = qiskit.ClassicalRegister(5)

# Create the quantum circuit
c = qiskit.QuantumCircuit(qr, cr)

# Hadamard the 5th bit (radioactive source).
c.h(qr[4])

# CNOT the radiation source to the Giger counter
c.cx(qr[4], qr[3])

# CNOT the giger to the hammer
c.cx(qr[3], qr[2])

# CNOT the hammer movement to the poison vial being broken
c.cx(qr[2], qr[1])

# Finally, the poison vial to the cat
c.cx(qr[1], qr[0])

# Measure the circuit.
c.measure(qr, cr)

# Execute locally.
print(qiskit.execute(c, qiskit.BasicAer.get_backend('qasm_simulator')).result().get_counts())

# All qubits are created in their lowest energy state (0) so for the purpose of this experiment:
# 5 Zeros is a non-emitting radioactive source and an alive cat etc.
# All Ones means the source has decayed, the giger counter picked it up... and the cat is dead.
