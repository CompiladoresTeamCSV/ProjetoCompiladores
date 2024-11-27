import os
from main import tabelinhas

def tabelinha_exists(): 
    return os.path.exists('dados/dados.csv')

def get_num_tabelinhas():
    if tabelinha_exists():
        return len(tabelinhas)
    else:
        return 0
    
