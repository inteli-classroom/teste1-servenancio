import exercicio1
import exercicio2
import exercicio3
import exercicio4




def test_multiplas_operacoes():

    # soma, subtração, multiplicação e divisão
    assert exercicio1.multiplas_operacoes(6, 2) == (8, 4, 12, 3)
    assert exercicio1.multiplas_operacoes(2, 4) == (6, -2, 8, 0.5)
    assert exercicio1.multiplas_operacoes(9, 0) == (9, 9, 0, 0)


def test_cumulativo():

    # soma cumulativa
    assert exercicio2.cumulativo([1, 2, 3]) == [1, 3, 6]
    assert exercicio2.cumulativo([1, -2, 3]) == [1, -1, 2]
    assert exercicio2.cumulativo([3, 3, -2, 408, 3, 0]) == [3, 6, 4, 412, 415, 415]


def test_soma_dos_aninhados():

    # soma dos aninhados
    lista = [[11, 22], [33], [44, 55, 66]]
    outra_lista = [[1, 2, 3, 4], [3, 3], [4, 6]]
    assert exercicio3.soma_dos_aninhados(lista) == 231
    assert exercicio3.soma_dos_aninhados(outra_lista) == 26


def test_tem_duplicados():

    # tem duplicados
    assert exercicio4.tem_duplicados([1, 2, 3, 2]) == True
    assert exercicio4.tem_duplicados([1, 2, 3, 4]) == False
    assert exercicio4.tem_duplicados([]) == False
    assert exercicio4.tem_duplicados([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    assert exercicio4.tem_duplicados([0, 0, 0, 0, 0]) == True
