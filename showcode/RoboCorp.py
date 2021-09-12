class CalculationChip:

    def SHIFT(R1, R2):
        pass
    
    def ADD():
        pass
    
    def MULTIPLY():
        pass
    
    def DIVIDE():
        pass
    
    def LOAD():
        pass
    
    def COPY():
        pass
    
    def TEST():
        pass
    
    def FINISH(R1):
        return R1

    def run(instruction):
        instr = ['SHIFT', 'ADD', 'MULTIPLY', 'DIVIDE', 'LOAD', 'COPY', 'TEST', 'FINISH']
        for i in instruction.split():
            if i in instr: 
                print('true')
    
CalculationChip.run('SHIFT $1 $2')