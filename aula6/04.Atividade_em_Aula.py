# Atividades Práticas:

# 1. Crie uma classe Conta com:
'''
Atributo _saldo (privado).
Getter saldo que retorna o valor formatado (ex: R$1000.00).
Setter que bloqueia valores negativos.
'''


class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):  # Getter para acessar o saldo
        return f"R${self._saldo:.2f}"  # duas casas decimais 
    
    @saldo.setter
    def saldo(self, valor):  # Setter para definir o saldo
        if valor >= 0:
            self._saldo = valor
        else:
            raise ValueError("O saldo não pode ser negativo")



valor = float(input("Digite o saldo: "))
conta = Conta(valor)
print(f"Saldo da conta: {conta.saldo}")  




# 2. Classes Abstratas:
'''
Crie uma classe abstrata Animal com método comum a todas as classes-filhas.
Implemente, pelo menos, as classes Cachorro e Gato com 3 métodos para cada uma.
'''
class Animal:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def brincar(self):
        return f"{self.nome} está brincando."

    def comer(self):
        return f"{self.nome} está comendo."
        


class Cachorro(Animal):
    def brincar(self):
        return f"{self.nome} está brincando!"

    def comer(self):
        return f"{self.nome} está comendo ração para cães."

    def latir(self):
        return f"{self.nome} está latindo!"



class Gato(Animal):
    def brincar(self):
        return f"{self.nome} está brincando com um novelo de lã!"

    def comer(self):
        return f"{self.nome} está comendo ração para gatos."

    def miar(self):
        return f"{self.nome} está miando!"



# 3. Padrão de Acesso a Repositórios

# Crie uma classe UsuarioRepository com os seguintes métodos:
'''
- cadastrar(usuario): cadastra um usuário (dicionário com nome e email).
- listar_todos(): retorna uma lista com todos os usuários cadastrados.
- buscar_por_email(email): retorna o usuário correspondente ao email informado.
- remover(email): remove o usuário correspondente ao email informado. 
- atualizar(usuario): atualiza os dados do usuário correspondente ao email informado.
- listar_por_nome(nome): retorna uma lista com todos os usuários que possuem o nome informado.
- listar_por_email(email): retorna uma lista com todos os usuários que possuem o email informado.
- listar_por_nome_e_email(nome, email): retorna uma lista com todos os usuários que possuem o nome e email informados.
'''



class UsuarioRepository:
    def __init__(self):
        self.usuarios = []  


    def cadastrar(self, usuario):
        self.usuarios.append(usuario)


    def listar_todos(self):
        return self.usuarios


    def buscar_por_email(self, email):
        for usuario in self.usuarios:
            if usuario['email'] == email:
                return usuario
        return None   # se o usuário não for encontrado


    def remover(self, email):
        """Remove o usuário correspondente ao email informado"""
        for usuario in self.usuarios:
            if usuario['email'] == email:
                self.usuarios.remove(usuario)
                return
        print("Usuário não encontrado.")


    def atualizar(self, usuario):
        for i in range(len(self.usuarios)):
            if self.usuarios[i]['email'] == usuario['email']:
                self.usuarios[i] = usuario  # Substitui o usuário antigo pelo novo
                return
        print("Usuário não encontrado.")


    def listar_por_nome(self, nome):
        usuarios_com_nome = []
        for usuario in self.usuarios:
            if usuario['nome'] == nome:
                usuarios_com_nome.append(usuario)  # Adiciona o usuário
        return usuarios_com_nome


    def listar_por_email(self, email):
        """Retorna uma lista com todos os usuários que possuem o email informado"""
        usuarios_com_email = []
        for usuario in self.usuarios:
            if usuario['email'] == email:
                usuarios_com_email.append(usuario)   # Adiciona o usuário
        return usuarios_com_email


    def listar_por_nome_e_email(self, nome, email):
        """Retorna uma lista com todos os usuários que possuem o nome e email informados"""
        usuarios_com_nome_email = []
        for usuario in self.usuarios:
            if usuario['nome'] == nome and usuario['email'] == email:
                usuarios_com_nome_email.append(usuario)   # Adiciona o usuário
        return usuarios_com_nome_email





repo = UsuarioRepository()


repo.cadastrar({'nome': 'paulo', 'email': 'paulofg@gmail.com'})
repo.cadastrar({'nome': 'Alyfer', 'email': 'alyferlindo@gmail.com'})
repo.cadastrar({'nome': 'jota', 'email': 'jotinha@gmail.com'})


print("\n Todos os usuários cadastrados ")
print(repo.listar_todos())


print("\nBuscando usuário por email 'alyferlindo@gmail.com' ")
print(repo.buscar_por_email('alyferlindo@gmail.com'))

# Atualizar um usuário
print("\n Atualizando o usuário 'João' para 'João Pedro' ")
repo.atualizar({'nome': 'João Pedro', 'email': 'jpmaluco@gmail.com'})
print(repo.listar_todos())

# Remover um usuário
print("\n Removendo o usuário 'Alyfer' ")
repo.remover('alyferlindo@gmail.com')
print(repo.listar_todos())


print("\n Listando usuários com nome 'jota fernades'")
print(repo.listar_por_nome('jota fernandes'))


print("\n Listando usuários com email 'jotinha@gmail.com' ")
print(repo.listar_por_email('jotinha@gmail.com'))


print("\n Listando usuários com nome 'paulo' e email 'paulofg@gmail.com' ")
print(repo.listar_por_nome_e_email('paulo', 'paulofg@gmail.com'))








# 4. DESAFIO: retorne às atividades 2 e 3 e implemente uma metaclasse dentro de seus respectivos contextos.