import tkinter as tk
from tkinter import messagebox, ttk
import os

# Simulação de estoque
estoque = {
    "MCS": {"quantidade": 500, "tamanhos": ["P", "M", "G"]},
    "MLS": {"quantidade": 300, "tamanhos": ["M", "G", "GG"]},
    "MCE": {"quantidade": 1000, "tamanhos": ["P", "M", "G", "GG"]},
    "MLE": {"quantidade": 200, "tamanhos": ["G", "GG"]},
}

# Função para verificar estoque
def verificar_estoque():
    modelo = estoque_modelo_combobox.get().strip().upper()
    if modelo in estoque:
        quantidade = estoque[modelo]["quantidade"]
        tamanhos = ", ".join(estoque[modelo]["tamanhos"])
        estoque_label.config(text=f"Quantidade disponível: {quantidade}\nTamanhos disponíveis: {tamanhos}")
    else:
        estoque_label.config(text="Modelo não encontrado no estoque.")

# Função para escolha do modelo
def escolha_modelo():
    modelo = modelo_combobox.get().strip().upper()
    if modelo == "MCS":
        return 1.80
    elif modelo == "MLS":
        return 2.10
    elif modelo == "MCE":
        return 2.90
    elif modelo == "MLE":
        return 3.20
    else:
        messagebox.showerror("Erro", "Modelo inválido. Selecione um modelo válido.")
        return None

# Função para número de camisetas com desconto
def num_camisetas():
    try:
        num = int(num_camisetas_entry.get())
        if num > 20000:
            messagebox.showerror("Erro", "Número de camisetas excede o limite aceito.")
            return None
        elif num >= 2000:
            return num * 0.88  # 12% de desconto
        elif num >= 200:
            return num * 0.93  # 7% de desconto
        elif num >= 20:
            return num * 0.95  # 5% de desconto
        elif num >= 1:
            return num  # Sem desconto
        else:
            messagebox.showerror("Erro", "Número inválido. Informe um número válido.")
            return None
    except ValueError:
        messagebox.showerror("Erro", "Entrada não numérica. Informe um número válido.")
        return None

# Função para escolha do frete
def frete():
    opcao_frete = frete_var.get()
    if opcao_frete == "1":
        return 100
    elif opcao_frete == "2":
        return 200
    elif opcao_frete == "0":
        return 0
    else:
        messagebox.showerror("Erro", "Opção de frete inválida. Selecione uma opção válida.")
        return None

# Função para calcular o total
def calcular_total():
    modelo_valor = escolha_modelo()
    if modelo_valor is None:
        return
    num_camisetas_valor = num_camisetas()
    if num_camisetas_valor is None:
        return
    frete_valor = frete()
    if frete_valor is None:
        return

    total = (modelo_valor * num_camisetas_valor) + frete_valor
    resumo_text = (
        f"Modelo: {modelo_combobox.get()}\n"
        f"Número de Camisetas: {num_camisetas_entry.get()}\n"
        f"Frete: {frete_var.get()}\n"
        f"Total a pagar: R${total:.2f}"
    )
    resultado_label.config(text=resumo_text)
    salvar_pedido(resumo_text)

# Função para salvar o pedido
def salvar_pedido(resumo_text):
    if not os.path.exists("pedidos.txt"):
        with open("pedidos.txt", "w") as f:
            f.write("Histórico de Pedidos\n")
            f.write("="*30 + "\n")
    
    with open("pedidos.txt", "a") as f:
        f.write(resumo_text + "\n")
        f.write("="*30 + "\n")

    atualizar_historico()

# Função para atualizar o histórico de pedidos
def atualizar_historico():
    if os.path.exists("pedidos.txt"):
        with open("pedidos.txt", "r") as f:
            historico_text = f.read()
            historico_text_area.config(state=tk.NORMAL)
            historico_text_area.delete(1.0, tk.END)
            historico_text_area.insert(tk.END, historico_text)
            historico_text_area.config(state=tk.DISABLED)

# Função para resetar campos
def resetar_campos():
    modelo_combobox.set("Selecione um modelo")
    num_camisetas_entry.delete(0, tk.END)
    frete_var.set("0")
    resultado_label.config(text="")
    atualizar_historico()

# Criar a janela principal
root = tk.Tk()
root.title("Fábrica de Camisetas")
root.geometry("700x600")
root.configure(bg="#f0f0f0")

# Criar abas
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# Aba de Pedidos
pedidos_frame = tk.Frame(notebook, bg="#f0f0f0", padx=20, pady=20)
notebook.add(pedidos_frame, text="Pedidos")

# Adicionar widgets na aba de pedidos
tk.Label(pedidos_frame, text="Escolha o modelo:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
modelos = ["MCS", "MLS", "MCE", "MLE"]
modelo_combobox = ttk.Combobox(pedidos_frame, values=modelos, state="readonly", width=20)
modelo_combobox.pack(pady=5)
modelo_combobox.set("Selecione um modelo")

tk.Label(pedidos_frame, text="Informe o número de camisetas:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
num_camisetas_entry = tk.Entry(pedidos_frame, width=20)
num_camisetas_entry.pack(pady=5)

tk.Label(pedidos_frame, text="Escolha o tipo de frete:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
frete_var = tk.StringVar(value="0")
frete_frame = tk.Frame(pedidos_frame, bg="#f0f0f0")
tk.Radiobutton(frete_frame, text="Transportadora (R$100)", variable=frete_var, value="1", bg="#f0f0f0").pack(anchor="w")
tk.Radiobutton(frete_frame, text="Sedex (R$200)", variable=frete_var, value="2", bg="#f0f0f0").pack(anchor="w")
tk.Radiobutton(frete_frame, text="Retirar na fábrica (Grátis)", variable=frete_var, value="0", bg="#f0f0f0").pack(anchor="w")
frete_frame.pack(pady=5)

tk.Label(pedidos_frame, text="Personalização da Camiseta:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
tk.Label(pedidos_frame, text="Cor:", bg="#f0f0f0").pack(pady=5)
cor_entry = tk.Entry(pedidos_frame, width=20)
cor_entry.pack(pady=5)

tk.Label(pedidos_frame, text="Tamanho:", bg="#f0f0f0").pack(pady=5)
tamanho_combobox = ttk.Combobox(pedidos_frame, values=["P", "M", "G", "GG"], state="readonly", width=20)
tamanho_combobox.pack(pady=5)
tamanho_combobox.set("Selecione um tamanho")

buttons_frame = tk.Frame(pedidos_frame, bg="#f0f0f0")
calcular_button = tk.Button(buttons_frame, text="Calcular Total", command=calcular_total, bg="#4a90e2", fg="#ffffff", font=("Helvetica", 12, "bold"))
calcular_button.pack(side=tk.LEFT, padx=5)
resetar_button = tk.Button(buttons_frame, text="Resetar", command=resetar_campos, bg="#e94e77", fg="#ffffff", font=("Helvetica", 12, "bold"))
resetar_button.pack(side=tk.LEFT, padx=5)
buttons_frame.pack(pady=10)

resultado_label = tk.Label(pedidos_frame, text="", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
resultado_label.pack(pady=10)

# Frame para histórico de pedidos
historico_frame = tk.Frame(pedidos_frame, bg="#f0f0f0", padx=20, pady=20)
historico_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

historico_label = tk.Label(historico_frame, text="Histórico de Pedidos", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
historico_label.pack(pady=10)

historico_text_area = tk.Text(historico_frame, height=10, width=70, wrap=tk.WORD, state=tk.DISABLED)
historico_text_area.pack(pady=10)

# Inicializar histórico de pedidos
atualizar_historico()

# Aba de Estoque
estoque_frame = tk.Frame(notebook, bg="#f0f0f0", padx=20, pady=20)
notebook.add(estoque_frame, text="Estoque")

# Adicionar widgets na aba de estoque
tk.Label(estoque_frame, text="Verificar Estoque de Camisetas:", font=("Helvetica", 14, "bold"), bg="#f0f0f0").pack(pady=10)
tk.Label(estoque_frame, text="Modelo:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
modelos_estoque = ["MCS", "MLS", "MCE", "MLE"]
estoque_modelo_combobox = ttk.Combobox(estoque_frame, values=modelos_estoque, state="readonly", width=20)
estoque_modelo_combobox.pack(pady=5)
estoque_modelo_combobox.set("Selecione um modelo")

verificar_estoque_button = tk.Button(estoque_frame, text="Verificar Estoque", command=verificar_estoque, bg="#4a90e2", fg="#ffffff", font=("Helvetica", 12, "bold"))
verificar_estoque_button.pack(pady=10)

estoque_label = tk.Label(estoque_frame, text="", font=("Helvetica", 12), bg="#f0f0f0")
estoque_label.pack(pady=10)

# Rodar a aplicação
root.mainloop()
