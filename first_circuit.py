import qiskit

run_on_real_quantum_computer = True
simulate = True

# 2 qubits and bits in registers
qr = qiskit.QuantumRegister(2)

cr = qiskit.ClassicalRegister(2)

# create the quantum circuit
c = qiskit.QuantumCircuit(qr, cr)

# Perform 'H' gate on qubit (superposition state)
c.h(qr[0])

# CNOT gate
c.cx(qr[0], qr[1])

# c.x(qr[1])

# Measure the circuit
c.measure(qr, cr)

job = qiskit.execute(c, qiskit.BasicAer.get_backend('qasm_simulator'))

print(job.result().get_counts())

if run_on_real_quantum_computer:
    qiskit.IBMQ.backends(simulator=simulate)
    qiskit.IBMQ.load_accounts()
    backend = qiskit.providers.ibmq.least_busy(qiskit.IBMQ.backends(simulator=simulate))
    print(f"We'll use the least busy device: {backend.name()}")
    job = qiskit.execute(c, backend)
    print(job.result().get_counts())
