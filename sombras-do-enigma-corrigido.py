import tkinter as tk
from tkinter import messagebox
import random

class SombrasdoEnigma:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sombras do Enigma")
        self.window.geometry("800x600")
        
        self.caso_atual = 0
        self.inventario_jogador = []
        self.pontuacao_moralidade = 50
        
        self.casos = [
            {
                "titulo": "A Herança Perdida",
                "local": "Mansão Antiga",
                "descricao": "O testamento desapareceu. Encontre pistas escondidas.",
                "pistas": ["Retrato antigo", "Chave do escritório", "Documento rasgado"],
                "passos_solucao": 3
            },
            {
                "titulo": "Crime na Estação",
                "local": "Estação de Trem",
                "descricao": "Um assassinato ocorre em um vagão. Interrogue passageiros.",
                "pistas": ["Bilhete suspeito", "Mapa da viagem", "Relógio quebrado"],
                "passos_solucao": 4
            }
        ]
        
        self.criar_menu_inicial()
        
    def criar_menu_inicial(self):
        self.limpar_janela()
        
        tk.Label(self.window, text="Sombras do Enigma", font=("Arial", 24)).pack(pady=50)
        
        tk.Button(self.window, text="Novo Jogo", command=self.iniciar_novo_jogo).pack(pady=10)
        tk.Button(self.window, text="Continuar", command=self.carregar_jogo).pack(pady=10)
        tk.Button(self.window, text="Configurações", command=self.mostrar_configuracoes).pack(pady=10)
        tk.Button(self.window, text="Créditos", command=self.mostrar_creditos).pack(pady=10)
        
    def iniciar_novo_jogo(self):
        self.caso_atual = 0
        self.iniciar_caso()
        
    def iniciar_caso(self):
        self.limpar_janela()
        caso = self.casos[self.caso_atual]
        
        tk.Label(self.window, text=caso["titulo"], font=("Arial", 18)).pack(pady=20)
        tk.Label(self.window, text=caso["local"], font=("Arial", 14)).pack(pady=10)
        tk.Label(self.window, text=caso["descricao"], wraplength=600).pack(pady=20)
        
        tk.Button(self.window, text="Investigar", command=self.investigar_caso).pack(pady=10)
        
    def investigar_caso(self):
        caso = self.casos[self.caso_atual]
        pistas_disponiveis = caso["pistas"].copy()
        
        def encontrar_pista():
            if pistas_disponiveis:
                pista = random.choice(pistas_disponiveis)
                pistas_disponiveis.remove(pista)
                messagebox.showinfo("Pista Encontrada", f"Você encontrou: {pista}")
                self.inventario_jogador.append(pista)
                
                if len(self.inventario_jogador) >= caso["passos_solucao"]:
                    messagebox.showinfo("Caso Resolvido", "Parabéns! Você resolveu o caso.")
                    self.caso_atual += 1
                    if self.caso_atual < len(self.casos):
                        self.iniciar_caso()
                    else:
                        messagebox.showinfo("Fim do Jogo", "Você completou todos os casos!")
            else:
                messagebox.showinfo("Sem Pistas", "Não há mais pistas para encontrar neste local.")
        
        tk.Button(self.window, text="Procurar Pista", command=encontrar_pista).pack(pady=10)
        
    def carregar_jogo(self):
        messagebox.showinfo("Carregar Jogo", "Função de carregamento não implementada nesta versão.")
        
    def mostrar_configuracoes(self):
        messagebox.showinfo("Configurações", "Opções de configuração serão adicionadas em versões futuras.")
        
    def mostrar_creditos(self):
        messagebox.showinfo("Créditos", "Sombras do Enigma\nDesenvolvido como protótipo")
        
    def limpar_janela(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        
    def executar(self):
        self.window.mainloop()

if __name__ == "__main__":
    jogo = SombrasdoEnigma()
    jogo.executar()
