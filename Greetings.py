def run_quiz():
    questions =[
        {
            "question": "What is the Spanish word for 'Hello'?",
            "options" : ["1. Hola", "2. Adiós", "3. Gracias", "4. Por favor"],
            "answer" :  "1"
            
        },
        {
            "question" : "what is the capital city of kenya? ",
            "options" :["1. Nairobi", "2. Kisumu", "3. Mombasa", "4. Eldoret"],
            "answer":  "1"
        },
        {
            "question" : "who won the grammy last year ",
            "options":["1. Kendrick", "2. Drake", "3. Toxic lyrikali", "4. key glock"],
            "answer": "1"
        },
        {
            "question" : "who is the fourth president of kenya? ",
            "options" : ["1. Moi", "2. Uhuru", "3. Mwai Kibaki", "4. Jomo Kenyatta"],
            "answer":  "2"
        }
    ]
    
    score = 0
    
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("your answer? ").strip().lower()
        
        if answer == q["answer"] or answer == q["answer"][-1]:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {q['answer']}")
            
def main():
    while True:
        print("Welcome to the quiz!")
        run_quiz()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("thanks for playing")
            break
        
main()
    

        
        
    