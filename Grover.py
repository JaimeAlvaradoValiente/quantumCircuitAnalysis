from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

qc.h(q[0])
qc.h(q[1])
qc.x(q[1])
qc.h(q[1])
qc.cx(q[0], q[1])
qc.h(q[1])
qc.x(q[1])
qc.h(q[1])
qc.measure(q, c)
