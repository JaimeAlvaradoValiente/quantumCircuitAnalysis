from qiskit import execute, QuantumRegister, ClassicalRegister, QuantumCircuit, Aer
from numpy import pi

q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)
#Grover circuit
qc.h(q[0])
qc.h(q[1])
qc.x(q[1])
qc.h(q[1])
qc.cx(q[0], q[1])
qc.h(q[1])
qc.x(q[1])
qc.h(q[1])
qc.measure(q, c)

backend = Aer.get_backend("ibmq_guadalupe")
x=int(1024)
job = execute(qc, backend, shots=x)
result = job.result()
counts = result.get_counts()
return counts
