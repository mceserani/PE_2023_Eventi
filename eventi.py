eventi = []

# EVENTO
# Nome
# Data
# Elenco di partecipanti (come lista)
# Luogo (default = Online)
# Caratteristiche aggiuntive varie

def crea_evento(nome, data, *args, luogo="Online", **kwargs):
    evento = {}
    evento["nome"] = nome
    evento["data"] = data
    evento["partecipanti"] = list(args)
    evento["luogo"] = luogo
    evento["caratteristiche"] = kwargs
    eventi.append(evento)


crea_evento("Python Essentials","2023-05-05","Matteo Ceserani","Roberto Feola", "Chiara Chinetti", "Federico Nosella",argomento="Modulo 4",durata="4",ospite="Alberto Cassinari")

print(eventi)