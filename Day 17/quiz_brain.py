class QuizzBrain:
    
    def __init__(self, q_list):
        self.numero_pergunta = 0
        self.lista_de_perguntas = q_list
        self.score = 0
    
    def proxima_pergunta(self):
        pergunta_atual = self.lista_de_perguntas[self.numero_pergunta]
        self.numero_pergunta += 1
        resposta = input(f"Q.{self.numero_pergunta}: {pergunta_atual.texto} (Verdade/Mentira): ")
        self.checa_resposta(resposta, pergunta_atual.resposta)
        
    def ainda_tem_perguntas(self):
        if self.numero_pergunta < len(self.lista_de_perguntas):
            return True
        else:
            False
            
    def checa_resposta(self, resposta_usuario, resposta_real):
        if resposta_usuario.lower() == resposta_real.lower():
            self.score += 1
            print("Você acertou!")
        else: 
            print("Você errou!")
        print(f"A resposta certa era: {resposta_real}.")
        print(f"A sua pontução é: {self.score}/{self.numero_pergunta}.")
        print("-----------------------------------------------------------------")
        
    def final_do_quiz(self):
            print("Você completou o quiz.")
            print("Parabens!")
            print(f"A sua pontuação final foi: {self.score}/{self.numero_pergunta}.")
            print("-----------------------------------------------------------------")