from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
from numpy import pi

qreg_q = QuantumRegister(3, 'q')
creg_crzz = ClassicalRegister(3, 'crzz')
creg_crxx = ClassicalRegister(4, 'crxx')
circuit = QuantumCircuit(qreg_q, creg_crzz, creg_crxx)


circuit.h(qreg_q[0])
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2])
circuit.h(qreg_q[1])
circuit.cx(qreg_q[1], qreg_q[2])
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2])
circuit.h(qreg_q[0])
circuit.p(pi / 4, qreg_q[0])
circuit.h(qreg_q[0])
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.h(qreg_q[0])
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2])
circuit.measure(qreg_q[0], creg_crzz[0])
circuit.measure(qreg_q[1], creg_crxx[0])
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2])
circuit.z(qreg_q[2]).c_if(creg_crzz, 1)
circuit.x(qreg_q[2]).c_if(creg_crxx, 1)

backend = Aer.get_backend("ibm_perth")
x=int(1024)
job = execute(circuit, backend, shots=x)
result = job.result()
counts = result.get_counts()
return counts
