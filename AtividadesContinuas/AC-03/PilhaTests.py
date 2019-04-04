import unittest
import Pilha

class TestPilha(unittest.TestCase):

    '''
    O método setUp roda uma vez antes de cada método de teste.
    Nele você pode colocar comandos que se repetiriam em todos os teste, como criar a Pilha.
    '''
    def setUp(self):
        self.__pilha = Pilha.Pilha()

    '''
    O método test_isInstanceOfPilha garente que o objeto testado é uma instânicia da classe Pilha.
    Nele, usamos assertIsInstance para saber se self.pilha é instância (objeto criado a partir) da classe Pilha.
    Leia assert como "certifique-se", no caso certifique-se que pilha(objeto) é instânicia de Pilha(classe).
    '''
    def test_isInstanceOfPilha(self):
        self.assertIsInstance(self.__pilha, Pilha.Pilha,"Objeto de testes não é uma Pilha")

    
    '''
    O método test_isEmptyOnStart garante que a pilha seja criada vazia.
    Nele, usamos assertEquals para comparar a lista interna da Pilha com uma lista vazia [].
    Certifique-se que pilha.valores é igual (equals) lista vazia.
    '''
    def test_isEmptyOnStart(self):
        self.assertEqual(self.__pilha.get_valores(), [], "Pilha não está sendo criada vazia")

    '''
    O método test_addsValue garante que a pilha adiciona o valor à lista interna quando usamos empilhar(1).
    Nele, usamos assertIn para garantir que o valor 1 está presente na lista interna da Pilha.
    Leia como certifique-se que pilha.valores contém (In) o valor 1.
    '''
    def test_addsValue(self):
        self.__pilha.empilhar(1)
        self.assertIn(1, self.__pilha.get_valores(), "Pilha não está adicionando valores à lista interna")

    '''
    O método test_empilharAddsToEnd garante que a pilha adiciona o valor à lista interna na posição correta quando usamos empilhar.
    Nele, não usamos assertIn, por que já sabemos pelo teste anterior que ela adiciona, só queremos saber se na posição correta.
    Empilhe os valores 1 e 2.
    Leia como certifique-se que pilha.valores é (equals) a lista [1,2].
    '''

    def test_empilharAddsToEnd(self):
        self.__pilha.empilhar(1)
        self.__pilha.empilhar(2)
        self.assertEqual(self.__pilha.get_valores(), [1, 2], "Fila não está enfileirando na ordem correta")

    '''
    O método test_desempilharIsCorrectAndReturns garante que a pilha remove o valor da posição correta e o retorna.
    Nele, empilhamos os valores 1 e 2. 
    Usamos assertEqual para garantir que o valor correto foi retornado.
    Usamos assertNotIn, para garantir que o valor retornado não está na lista interna da Pilha.
    E usamos assertIn, para garantir o outro valor continua na lista lista interna da Pilha.
    Leia como certifique-se que:
        valor é igual (equal) a 2 
        pilha.valores não contém (NotIn) 2 
        pilha.valores contém (In) 1
    '''
    def test_desempilharIsCorrectAndReturns(self):
        self.__pilha.empilhar(1)
        self.__pilha.empilhar(2)
        valor = self.__pilha.desempilhar()
        self.assertEqual(valor, 1, "Pilha não está retornando o valor correto ao desenfileirar")
        self.assertNotIn(valor, self.__pilha.get_valores(), "O valor desenfileirado continua na fila")
        self.assertIn(2, self.__pilha.get_valores(), "Pilha não está desenfileirando na ordem correta")

    '''
    O método test_popOnEmptyPilhaRaises garante que desempilhar em uma pilha vazia dê erro.
    Nele, usamos assertRaises para garantir que dê um erro do tipo IndexError ao desempilhar a pilha vazia.
    Observe que assertRaises é usado com with e a operação que dará erro está dentro do with.
    Assim, o erro é capturado e não irá parar o programa.
    Leia como certifique-se que desempilhar em uma pilha vazia dê um erro do tipo IndexError.
    '''

    def test_popOnEmptyPilhaRaises(self):
        with self.assertRaises(IndexError):
            self.__pilha.desempilhar()


unittest.main()
