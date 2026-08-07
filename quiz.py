print("=-=-=-=-=BEM VINDO!=-=-=-=-=")

tipo_de_quiz = input("\nQual tipo de quiz você quer fazer hoje? Lembre-se, escolha matérias ESCOLARES entre: matemática, história, geografia e biologia ): ").lower()

def quiz_matematica():
        score = 0
        print("Pergunta 1: Quanto é 2 + 2?")
        resposta1 = input("Digite sua resposta: ")
        if resposta1 == "4":
            score += 1
            print("Resposta correta!")
        else:
            print("Resposta incorreta. A resposta correta é 4.")

        print("Pergunta 2: Quanto é 5 * 6?")
        resposta2 = input("Digite sua resposta: ")
        if resposta2 == "30":
            score += 1
            print("Resposta correta!")
        else:
            print("Resposta incorreta. A resposta correta é 30.")

        print(f"Você acertou {score} de 2 perguntas.")

def quiz_historia():
        
        score = 0
        print("Pergunta 1: Quem foi o primeiro presidente do Brasil?")
        resposta1 = input("Digite sua resposta: ")
        if resposta1.lower() == "deodoro da fonseca":
            score += 1
            print("Resposta correta!")
        else:
            print("Resposta incorreta. A resposta correta é Deodoro da Fonseca.")

        print("Pergunta 2: Em que ano ocorreu a Proclamação da República no Brasil?")
        resposta2 = input("Digite sua resposta: ")
        if resposta2 == "1889":
            score += 1
            print("Resposta correta!")
        else:
            print("Resposta incorreta. A resposta correta é 1889.")

        print(f"Você acertou {score} de 2 perguntas.")

def quiz_geografia():
        
        score = 0
        print("Pergunta 1: Qual é a capital do Brasil?")
        resposta1 = input("Digite sua resposta: ")
        if resposta1.lower() == "brasília":
            score += 1
            print("Resposta correta!")
        else:
            print("Resposta incorreta. A resposta correta é Brasília.")

        print("Pergunta 2: Qual é o maior país do mundo em área?")
        resposta2 = input("Digite sua resposta: ")
        if resposta2.lower() == "rússia":
            score += 1
            print("Resposta correta!")
        else:
            print("Resposta incorreta. A resposta correta é Rússia.")

        print(f"Você acertou {score} de 2 perguntas.")

def quiz_biologia():
        score = 0
        print("Pergunta 1: Qual é a unidade básica da vida?")
        resposta1 = input("Digite sua resposta: ")
        if resposta1.lower() == "célula":
            score += 1
            print("Resposta correta!")
        else:
            print("Resposta incorreta. A resposta correta é Célula.")

        print("Pergunta 2: Qual é o processo pelo qual as plantas produzem seu próprio alimento?")
        resposta2 = input("Digite sua resposta: ")
        if resposta2.lower() == "fotossíntese":
            score += 1
            print("Resposta correta!")
        else:
            print("Resposta incorreta. A resposta correta é Fotossíntese.")

        print(f"Você acertou {score} de 2 perguntas.")
    
if tipo_de_quiz == "matemática":
    print("\nvocê escolheu o quiz de Matemática. Boa sorte!") 
    quiz_matematica()

elif tipo_de_quiz == "história":
    print("\nvocê escolheu o quiz de História. Boa sorte!") 
    quiz_historia()

elif tipo_de_quiz == "geografia":
    print("\nvocê escolheu o quiz de Geografia. Boa sorte!") 
    quiz_geografia()

elif tipo_de_quiz == "biologia":
    print("\nvocê escolheu o quiz de Biologia. Boa sorte!") 
    quiz_biologia()
