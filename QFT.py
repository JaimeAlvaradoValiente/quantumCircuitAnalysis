from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
from numpy import pi

qreg_q = QuantumRegister(3, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[2])
circuit.h(qreg_q[1])
circuit.h(qreg_q[0])
circuit.h(qreg_q[2])
circuit.cp(pi / 2, qreg_q[2], qreg_q[1])
circuit.cp(pi / 4, qreg_q[2], qreg_q[0])
circuit.h(qreg_q[1])
circuit.cp(pi / 2, qreg_q[1], qreg_q[0])
circuit.h(qreg_q[0])
circuit.swap(qreg_q[0], qreg_q[2])
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2])
circuit.measure(qreg_q[1], creg_c[1])
circuit.measure(qreg_q[0], creg_c[0])
circuit.measure(qreg_q[2], creg_c[1])

backend = Aer.get_backend("ibmq_guadalupe")
x=int(1024)
job = execute(circuit, backend, shots=x)
result = job.result()
counts = result.get_counts()
return counts