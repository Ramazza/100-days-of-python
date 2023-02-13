from data import question_data
from question_model import QuestionModel
from quiz_brain import QuizzBrain

banco_de_perguntas = []

for i in question_data:
    texto = i["text"]
    resposta = i["answer"]
    nova_pergunta = QuestionModel(q_texto=texto, q_resposta=resposta)
    banco_de_perguntas.append(nova_pergunta)

quiz = QuizzBrain(banco_de_perguntas)

while quiz.ainda_tem_perguntas():
    quiz.proxima_pergunta()

quiz.final_do_quiz()