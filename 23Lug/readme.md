Benvenuti!

Per prima cosa usiamo il terminale (Anaconda Prompt, ad esempio) per creare una cartella ed entrarci dentro

```bash
mkdir primaprova
cd primaprova
```

adesso stampiamo un messaggio a schermo

```bash
echo ciao
```
`ciao`

invece che stampare, possiamo savare il messaggio su un file di testo

```bash
echo ciao > file.txt
```

se non vogliamo sovrascrivere l'intero file ma solo aggiungere nuove righe il comando cambia


```bash
echo Hello World! > prova.txt
echo Hello World2 >> prova.txt
```

possiamo esportare su di un file il risultato di qualsiasi comando. Con `dir` ad esempio (`ls` su Unix) ottengo l'elenco dei files e cartelle presenti nella cartella in cui mi trovo

```bash
dir > prova2.txt
dir >> prova2.txt
```

Come si può vedere la seconda volta che esporto i risultati, la dimensione del file prova2.txt cambia.

**Assignment**: creare una nuova cartella e all'interno di essa creare un fie di testo con il proprio nome e cognome, seguito dall'elenco di files e cartelle contenuti della cartella stessa


Adesso che abbiamo familiarità con la riga di comando lanciamo il comando `python` e proviamo i primi comandi
somma
```python
1+1
```
`2`

prodotto
```python
2*3
```
`6`

potenza
```python
2**3
```
`8`

stampa a schermo
```python
print("ciao!")
```
`ciao`

Possiamo anche assegnare a una variabile un valore per usarlo successivamente. Per fare il teorema di Pitagora:

```python
a=3
b=4
c=(a**2+b**2)**.5
print(c)
```
`5.0`
Usciamo dalla shell python con il comando `quit()` 
Quando i comandi sono tanti conviene scriverli su un file di testo, preferibilmente di estensione `.py`, e lanciare uno script con il comando

```
python nomescript.py
```

eventualmente posso salvare i risultati dei comandi `print` nel solito modo

```
python nomescript.py > fileditesto.txt
```

Quando usiamo uno script è bene chiedere all'utente di volta in volta quali input intende utilizzare. Per fare ciò posso utilizzare il comando `a = input("scrivi l'input: ")`, il quale restituisce sempre una stringa, convertibile in numero con il comando `a=float(a)` o `a=int(a)` se si vuole un intero.
In alternativa usando il pacchetto sys, gli input si possono dichiarare al momento del lancio dello script, ad esempio:

```
python secondoscript.py 3 4
```
`5.0`


