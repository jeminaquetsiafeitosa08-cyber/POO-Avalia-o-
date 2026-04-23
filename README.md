# POO-Avalia-o-
Sistema de Caixa Eletrônico (ATM) -  Atividade Acadêmica 

Neste programa apresento um sistema de Caixa eletrônico básico que apresenta as seguintes funções : 
Criar Conta
Depositar 
Sacar 
Consultar Saldo 
Ver Histórico de transações 

Para realizá-lo utilizei conceitos aprendidos em aulas com base em Programação Orientada a Objeto com Python :
-  Polimorfismo 
-  Herança 
-  Composição 
-  Agregação 
-  Encapsulamento 
-  Classe e Objetos

Vejamos, defini as seguintes classes : Conta , Cliente e Histórico. 
Temos por herança de Conta : Conta corrente e conta poupança.

Polimorfismo, temos Sacar() assumindo diferentes comportamento dependendo do tipo de conta, definindo eu que há taxa para conta corrente enquanto a conta poupança não há taxa.

Em agregação definir uma lista onde o cliente pode ter mais de uma conta atribuído ao mesmo cliente. 

Para a composição observamos a criação da classe histórico, a partir do momento em que criamos essa classe importamos diretamente dentro da nossa classe Conta.


ESTRUTURAÇÃO DO CÓDIGO :

banco/
 ├── contas/
 │    ├── conta.py
 │    ├── corrente.py
 │    └── poupanca.py
 ├── clientes/
 │    └── cliente.py
 ├── operacoes/
 │    └── historico.py
 └── main.py

- [x] Definição do Menu Principal em Main.py 

1 - Criar Conta
2 - Depositar
3 - Sacar
4 - Consultar Saldo
5 - Histórico
0 - Sair


As regras foram implementadas para manter a ordem e lógica de funcionamento do sistema tal que, 	
  - Não é permitido sacar valores maiores que o saldo
 - Não é permitido inserir valores negativos
 - Todas as operações são registradas no histórico.


Autor: Jemina Quetsia Feitosa Teixeira 

