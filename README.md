# Gestão de Pedidos e Estoque de Camisetas  

Este projeto é um Trabalho da faculdade **UNINTER**, do curso **Gestão de Tecnologia da Informação**. Trata-se de uma aplicação desktop desenvolvida com Python e a biblioteca **Tkinter**.  

A aplicação tem como objetivo gerenciar pedidos e verificar o estoque de camisetas em uma fábrica, proporcionando uma interface simples e funcional para esses processos.  

## 🎯 Funcionalidades  
- **Gerenciamento de Pedidos:**  
  - Inserir quantidade de camisetas.  
  - Selecionar o tipo de frete.  
  - Calcular o valor total do pedido, com descontos automáticos baseados na quantidade.  

- **Controle de Estoque:**  
  - Consultar o estoque atual de camisetas disponíveis.  
  - Atualizar os itens conforme os pedidos são realizados.  

## ⚙️ Regras de Negócio  
1. O valor total dos pedidos é calculado automaticamente com base na quantidade e nos descontos aplicáveis.  
2. Descontos progressivos:  
   - **5%** para pedidos acima de 50 camisetas.  
   - **10%** para pedidos acima de 100 camisetas.  
3. Opções de frete:  
   - **Expresso**  
   - **Padrão** (com valores distintos no cálculo final).  

## 🛠️ Tecnologias Utilizadas  
- **Python**  
- **Tkinter**  

## 📂 Estrutura do Projeto  
```plaintext
├── main.py             # Arquivo principal da aplicação  
├── pedido_manager.py   # Lógica de gerenciamento de pedidos  
├── estoque_manager.py  # Lógica de controle de estoque  
├── assets/             # Recursos visuais (ícones, imagens)  
└── README.md           # Documentação do projeto

🖥️ Interface do Usuário
Aba de Pedidos:
Permite realizar pedidos, calcular o valor total, aplicar descontos e escolher o tipo de frete.

Aba de Estoque:
Exibe as camisetas disponíveis no estoque e registra as atualizações automaticamente.

📈 Melhorias Futuras
Adicionar relatórios detalhados de vendas.
Implementar funcionalidade de cadastro de novos produtos.
Adicionar suporte para exportação de dados em Excel.
📜 Licença
Este projeto foi desenvolvido para fins acadêmicos e está sob os direitos autorais de Andre Amorim Liberatto.

Desenvolvido por:
Andre Amorim Liberatto
