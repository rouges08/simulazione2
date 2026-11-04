class LaboratorioBiotecnologico:
    def __init__(self) -> None:
        self.test: list[Test-Biologico] = []
        self.esisti: dict[str,str] = {}
        
    def registra_test(self, test: TestBiologico) -> None:
        if test.codice in self.esisti:      
            raise ValueError(f"Il codice {test.codice} è gia presente")
        self.test.append(test)
        self.esisti[test.codice] = test.esisto()