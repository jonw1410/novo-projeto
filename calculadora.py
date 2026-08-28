import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("360x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2f")

        self.expressao = ""
        self.historico_resultados = []  # Pilha de resultados anteriores
        self.indice_historico = -1

        # Display Frame
        display_frame = tk.Frame(root, bg="#1e1e2f", padx=16, pady=12)
        display_frame.pack(fill="both")

        # Sub-display (Expressão / Histórico)
        self.sub_display_var = tk.StringVar(value="")
        self.sub_display = tk.Label(
            display_frame,
            textvariable=self.sub_display_var,
            font=("Segoe UI", 11),
            bg="#13131f",
            fg="#94a3b8",
            anchor="e",
            padx=16,
            pady=4,
            relief="flat",
            bd=0
        )
        self.sub_display.pack(fill="both")

        # Display Principal
        self.display_var = tk.StringVar(value="0")
        self.display = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=("Segoe UI", 26, "bold"),
            bg="#13131f",
            fg="#ffffff",
            anchor="e",
            padx=16,
            pady=12,
            relief="flat",
            bd=0
        )
        self.display.pack(fill="both", expand=True)

        # Grade de Botões
        botoes = [
            ('AC', '#ef4444', 1, 0), ('C', '#f59e0b', 1, 1), ('ANS', '#8b5cf6', 1, 2), ('÷', '#6366f1', 1, 3),
            ('7', '#2d2d42', 2, 0), ('8', '#2d2d42', 2, 1), ('9', '#2d2d42', 2, 2), ('×', '#6366f1', 2, 3),
            ('4', '#2d2d42', 3, 0), ('5', '#2d2d42', 3, 1), ('6', '#2d2d42', 3, 2), ('-', '#6366f1', 3, 3),
            ('1', '#2d2d42', 4, 0), ('2', '#2d2d42', 4, 1), ('3', '#2d2d42', 4, 2), ('+', '#6366f1', 4, 3),
            ('0', '#2d2d42', 5, 0), ('.', '#2d2d42', 5, 1), ('%', '#3b82f6', 5, 2), ('=', '#10b981', 5, 3)
        ]

        btn_frame = tk.Frame(root, bg="#1e1e2f", padx=16, pady=6)
        btn_frame.pack(fill="both", expand=True)

        for col in range(4):
            btn_frame.columnconfigure(col, weight=1)
        for row in range(1, 6):
            btn_frame.rowconfigure(row, weight=1)

        for item in botoes:
            texto = item[0]
            cor = item[1]
            linha = item[2]
            coluna = item[3]
            colspan = item[4] if len(item) > 4 else 1

            btn = tk.Button(
                btn_frame,
                text=texto,
                font=("Segoe UI", 12, "bold"),
                bg=cor,
                fg="#ffffff",
                activebackground="#4338ca",
                activeforeground="#ffffff",
                relief="flat",
                bd=0,
                cursor="hand2",
                command=lambda t=texto: self.clicar(t)
            )
            btn.grid(row=linha, column=coluna, columnspan=colspan, padx=4, pady=4, sticky="nsew")

        # Vincular teclas do teclado
        self.root.bind("<Key>", self.tecla_pressionada)
        self.root.bind("<Control-z>", lambda e: self.voltar_resultado_anterior())

    def voltar_resultado_anterior(self):
        """Recupera o resultado anterior da pilha de histórico."""
        if not self.historico_resultados:
            self.sub_display_var.set("Sem histórico anterior")
            return

        # Pega o último resultado salvo
        ultimo = str(self.historico_resultados[-1])
        
        # Se estiver no meio de uma operação (ex: '5+'), anexa o ANS
        if self.expressao and self.expressao[-1] in "+-*/÷×":
            self.expressao += ultimo
            self.display_var.set(self.expressao)
        else:
            self.expressao = ultimo
            self.display_var.set(self.expressao)
        
        self.sub_display_var.set(f"ANS = {ultimo}")

    def clicar(self, valor):
        if valor == "AC":
            self.expressao = ""
            self.display_var.set("0")
            self.sub_display_var.set("")
        elif valor == "C":
            self.expressao = self.expressao[:-1]
            self.display_var.set(self.expressao if self.expressao else "0")
        elif valor == "ANS":
            self.voltar_resultado_anterior()
        elif valor == "%":
            try:
                resultado = str(eval(self.expressao.replace('×', '*').replace('÷', '/')) / 100)
                self.display_var.set(resultado)
                self.expressao = resultado
            except Exception:
                self.display_var.set("Erro")
                self.expressao = ""
        elif valor == "=":
            self.calcular()
        else:
            if self.display_var.get() == "0" and valor not in "+-×÷*/%":
                self.expressao = valor
            else:
                self.expressao += valor
            self.display_var.set(self.expressao)

    def calcular(self):
        if not self.expressao:
            return
        try:
            exp_formatada = self.expressao.replace('×', '*').replace('÷', '/')
            resultado = eval(exp_formatada)

            if isinstance(resultado, float):
                resultado = round(resultado, 8)
                if resultado.is_integer():
                    resultado = int(resultado)

            # Salva no histórico de resultados
            self.historico_resultados.append(resultado)
            if len(self.historico_resultados) > 30:
                self.historico_resultados.pop(0)

            self.sub_display_var.set(f"{self.expressao} =")
            self.display_var.set(str(resultado))
            self.expressao = str(resultado)
        except ZeroDivisionError:
            self.display_var.set("Erro (Divisão por 0)")
            self.expressao = ""
        except Exception:
            self.display_var.set("Erro")
            self.expressao = ""

    def tecla_pressionada(self, evento):
        tecla = evento.char
        if tecla in "0123456789+-*/.":
            mapa = {'*': '×', '/': '÷'}
            self.clicar(mapa.get(tecla, tecla))
        elif evento.keysym in ("Return", "equal"):
            self.calcular()
        elif evento.keysym == "BackSpace":
            self.clicar("C")
        elif evento.keysym == "Escape":
            self.clicar("AC")
        elif tecla in ("a", "A", "v", "V"):
            self.voltar_resultado_anterior()

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
