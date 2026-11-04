from test_biologico import TestBiologico
from laboratorio import LaboratorioBiotecnologico

def stampa_test(elenco: list[Test-Biologico]) -> None:
    for test in elenco:
        print(
            f"{test.codice}: "
            f"{test.parametro} ="
            f"{test.valore} {test.unita} "
            f"-> {test.esito()}"
            )
        
def main() -> None:
    lab = laboratorioBiotecnologico()
    dati = [
        TestBiologico("QC-01", "BIO-24A", "endotossine", 0.8, 1.0, "EU/mL"),
        TestBiologico("QC-02", "BIO-24A", "DNA residuo", 4.2, 10.0, "ng/mL"),
        TestBiologico("QC-03", "BIO-24B", "carica microbica", 120, 100, "CFU/mL"),
        TestBiologico("QC-04", "BIO-24B", "endotossine", 1.0, 1.0, "EU/mL"),
        TestBiologico("QC-05", "BIO-24C", "DNA residuo", 12, 10.0, "ng/mL"),
    ]
    
    for codice, campione, prametro, limite, unita in dati:
        test = TestBilogico(
            codice, campione, parametro, valore, limite, unita
            )
        lab.registro_test(test)
        lab.riepilogo()
        
    trovati = lab.cerca_per_campione("BIO-24B")
    stampa_test(trovati)
    
    
    duplicato = TestBiologico("QC-05", "BIO-24C", "DNA residuo", 12, 10.0, "ng/mL")
    try:
        lab.registra_test(duplicato)
    except  ValueError as errore:
        print("Impossibile registrare il test:", errore)
            
    nessuno = lab.cerca_per_campione("BIO-94C")
    if len(nessuno) == 0:
        print("Nessun test trovato")
    else:
        stampa_test(nessuno)
              
    if __name__ == "__main__":
              main()