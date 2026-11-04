class LaboratorioBiotecnologico:
    def __init__(self) -> None:
        self.test: list[Test-Biologico] = []
        self.esisti: dict[str,str] = {}
        
    def registra_test(self, test: TestBiologico) -> None:
        if test.codice in self.esisti:      
            raise ValueError(f"Il codice {test.codice} è gia presente")
        self.test.append(test)
        self.esisti[test.codice] = test.esisto()
        
    def cerca_per_campione(self,campione: str) -> list[Test-Biologico]:
        risultati = []
        for test in self.test:
            if test.campione.lower() == campione.lower():
                risultati.append(test)
                return risultati
            
    def riepilogo(self) -> None:
        print("RIEPILOGO TEST REGISTRATI")
        conforrmi = 0
        fuori_specifica = 0
        for test in self.test:
            esisto = self.esiti[test.codice]
            print(
                f"{test.codice} | {test.campione} | "
                f"{test.parametro} | "
                f"{test.valore} {test.unita} "
                f"(max {test.limite_massimo} ) -> {esito}"
                )
            if esito == "CONFORME":
                conformi += 1
            else:
                fuori_specifica =+ 1
                
            print(f"Conformi : {conformi}")
            
            print(f"Fuori specifica:{fuori_specifica}")
            
