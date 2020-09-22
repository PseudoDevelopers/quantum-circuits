def loadAccount():
    from qiskit import IBMQ

    IBMQ.save_account(open('token.txt', 'r').read())
    IBMQ.load_account()
