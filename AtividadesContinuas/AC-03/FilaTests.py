import unittest
import Fila

class TestFila(unittest.TestCase):

    '''
    O método setUp roda uma vez antes de cada método de teste.
    Nele você pode colocar comandos que se repetiriam em todos os teste, como criar a Fila.
    '''
    def setUp(self):
        self.fila = Fila.Fila()

    '''
    O método test_isInstanceOfFila garente que o objeto testado é uma instânicia da classe Fila.
    Nele, usamos assertIsInstance para saber se self.fila é instância (objeto criado a partir) da classe Fila.
    Leia assert como "certifique-se", no caso certifique-se que fila(objeto) é instânicia de Fila(classe).
    '''
    def test_isInstanceOfFila(self):
        self.assertIsInstance(self.fila, Fila.Fila,"Objeto de testes não é uma Fila")

    '''
    O método test_isEmptyOnStart garante que a fila seja criada vazia.
    Nele, usamos assertEquals para comparar a lista interna da Fila com uma lista vazia [].
    Certifique-se que fila.valores é igual (equals) lista vazia.
    '''
    def test_isEmptyOnStart(self):
        self.assertEqual(self.fila.valores, [], "Fila não está sendo criada vazia")

    '''
    O método test_addsValue garante que a fila adiciona o valor à lista interna quando usamos enfileirar.
    Nele, usamos assertIn para garantir que o valor está presente na lista interna da Fila.
    Leia como certifique-se que fila.valores contém (In) o valor 1.
    '''
    def test_addsValue(self):
        self.fila.enfileirar(1)
        self.assertIn(1, self.fila.valores, "Fila não está adicionando valores à lista interna")

    '''
    O método test_enfileirarAddsToEnd garante que a fila adiciona o valor à lista interna quando usamos enfileirar na posição correta.
    Nele, não usamos assertIn, por que já sabemos pelo teste anterior que ela adiciona, agora queremos saber se na posição correta.
    Leia como certifique-se que fila.valores é (equals) a lista [1,2].
    '''
    def test_enfileirarAddsToEnd(self):
        self.fila.enfileirar(1)
        self.fila.enfileirar(2)
        self.assertEqual(self.fila.valores, [1,2], "Fila não está enfileirando na ordem correta")

    '''
    O método test_desenfileirarIsCorrectAndReturns garante que a fila remove o valor da posição correta e o retorna.
    Nele, usamos assertEqual para garantir que o valor correto foi retornado.
    Usamos assertNotIn, para garantir que o valor retornado não está na lista interna da Fila.
    E usamos assertIn, para garantir o outro valor continua na lista lista interna da Fila.
    Leia como certifique-se que:
        valor é igual (equal) a 1 
        fila.valores não contém (NotIn) 1 
        fila.valores contém (In) 2 
    '''
    def test_desenfileirarIsCorrectAndReturns(self):
        self.fila.enfileirar(1)
        self.fila.enfileirar(2)
        valor = self.fila.desenfileirar()
        self.assertEqual(valor, 1, "Fila não está retornando o valor correto ao desenfileirar")
        self.assertNotIn(valor, self.fila.valores, "O valor desenfileirado continua na fila")
        self.assertIn(2, self.fila.valores, "Fila não está desenfileirando na ordem correta")

    '''
    O método test_popOnEmptyFilaRaises garante que desenfileirar em uma fila vazia dê erro.
    Nele, usamos assertRaises para garantir que dê um erro do tipo IndexError ao desenfileirar a fila vazia.
    Observe que assertRaises é usado com with e a operação que dará erro está dentro do with.
    Assim, o erro é capturado e não irá parar o programa.
    Leia como certifique-se que desenfileirar em uma fila vazia dê um erro do tipo IndexError.
    '''
    def test_popOnEmptyFilaRaises(self):
        with self.assertRaises(IndexError):
            self.fila.desenfileirar()


unittest.main()