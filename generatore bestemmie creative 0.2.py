import random
gruppo_a = ["dio", "gesù", "giuda" "cristo"]
gruppo_b = [
    "Pennarello", "bistecca", "lampadario", "cane", "disonesto", "cane", "smerdarolo", 
"porco", "boscaiolo", "radioattivo", "coleroso", "troione", "ricchione", "merda",
 "maialone", "puttaniere", "acquario", "polente", "cacciavite", "ingordo", "sborrato", 
 "polacco", "prezzemolo", "cipresso", "prosciutto", "ippopotamo", "elefante", "gelato",
  "canceelino", "quaderno", "aragosta", "philadelphia", "carota", "porcaccio", "lenzuola",
   "piatto", "gorilla", "falena", "ciliegia", "canguro"
]
print(f"--- GENERATORE PRONTO ---")
print(f"Caricate {len(gruppo_a)} parole in A e {len(gruppo_b)} in B.")
print("Premi INVIO per generare, scrivi 'esci' per chiudere.")

while True:
    comando = input("\n> ").lower().strip()
    
    if comando == "esci":
        break
    
    if gruppo_a and gruppo_b:
        # Sceglie a caso e stampa
        print(f"{random.choice(gruppo_a)} {random.choice(gruppo_b)}")
    else:
        print("Errore: Assicurati di aver riempito entrambi i gruppi!")