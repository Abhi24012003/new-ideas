print("welcome to the kbc show".center(110))
A = input("Enter your first name: ")
B = input("Writer your last name")
DOB = input("Enter your date of birth(DD/MM/YYYY):").split("/")
C = input("Enter your city name")
print("Do you want to play the game?")
print("1. Yes")
print("2. No")
response = int(input("1 or 2"))
if response == 1:
    print("1) Jalgaon")
    print("2) Mumbai")
    print("3) pune")
    akash = int(input("Enter you choice"))
    if akash == 1:
        print("Level 1 Easy")
        print("Level 2 Medium")
        print("Level 3 Hard")
        abhi = int(input("Enter your choice 1, 2, 3 = "))
        if abhi == 1:
            # Easy questions
            questions = [
                {
                    "question": " 1.Which is the Winter Capital of Maharashtra?",
                    "options": ["a. Nagpur", "b. pune", "c. delhi", "d. Nashik"],
                    "answer": "a"
                },
                {
                    "question": "Which one of the following ports is the oldest port in India?",
                    "options": ["a. Mumbai Port", "b. Chennai Port", "c. Kolkata Port", "d. Vishakhapatnam Port"],
                    "answer": "b"
                },
                {
                    "question": "The unit of electrical resistance of a conductor is_____",
                    "options": ["a. farad", "b. volt", "c. ampere", "d. ohm"],
                    "answer": "d"
                },

            ]
            score = 0
            for q in questions:
                print(q["question"])
                for o in q["options"]:
                    print(o)
                answer = input("Enter your answer: ")
                if answer == q["answer"]:
                    print("Your answer is correct!")
                    score += 1
                else:
                    print("Your answer is incorrect.")

                print("Your final score is ", score)

    elif akash == 2:
        print("Level Easy")
        print("Level Medium")
        print("Level Hard")
        akash = int(input("Enter your choice"))
        kirti == 2:

        # Medium questions
        questions = [
            {
                "question": "Which of the following is the largest air pollutant?",
                "options": ["a. Carbon dioxide", "b. Carbon monoxide", "c. Sulphur dioxide", "d. Hydrocarbons"],
                "answer": "b"
            },
            {
                "question": "In binary code, the number 7 is written by___",
                "options": ["a. 110", "b. 111", "c. 101", "d. 100"],
                "answer": "d"
            },
            {
                "question": "Fathometer is used to measure",
                "options": ["a. Rainfall", "b. Ocean depth", "c. Sound intensity", "d. Earthquakes"],
                "answer": "b"
            },
        ]
        score = 0
        for q in questions:
            print(q["question"])
            for o in q["options"]:
                print(o)
            answer = input("Enter your answer: ")
            if answer == q["answer"]:
                print("Your answer is correct!")
                score += 1
            else:
                print("Your answer is incorrect.\n your game was over")
                break
            print("Your final score is ", score)



    elif akash == 3:
        print("Level 7")
        print("Level 8")
        print("Level 9")
        akash = int(input("Enter yur choice"))
        if akash == 1:
        #hard questions
        questions = [
            {
                "question": "In which country is the World Bank headquarters located?",
                "options": ["a. Mount Rainier MD", "b. Silver Spring MD", "c. Washington DC", "d. Hyattsville MD"],
                "answer": "c"
            },
            {
                "question": "Who wrote “Hindutva and National Renaissance”?",
                "options": ["a. Who wrote “Hindutva and National Renaissance”?", "b. P.C.Mehalonibis",
                            "c. Subramanian Swamy", "d. Kaushik Basu"],
                "answer": "c"
            },
            {
                "question": "Which country is the largest medical device exporter to India?",
                "options": ["a. China", "b. US", "c. Japan", "d. Australia"],
                "answer": "b"
            },
        ]
        score = 0
        for q in questions:
            print(q["question"])
            for o in q["options"]:
                print(o)
            answer = input("Enter your answer: ")
            if answer == q["answer"]:
                print("Your answer is correct!")
                score += 1
            else:
                print("Your answer is incorrect.")

            print("your final score is ", score)

    elif response == 2:
        print("Level Easy")
        print("Level Medium")
        print("Level Hard")
        tejas = int(input("Enter your choice 1, 2, 3"))
        akash ==

       # easy
        questions = [
            {
                "question": "HHow many seats does Maharashtra have in the Rajya Sabha",
                "options": ["a. 09 Seats ", "b. 12 Seats ", "c. 16 Seats ", "d. 19 Seats "],
                "answer": "d"
            },
            {
                "question": "2. How many seats does Maharashtra have in the Lok Sabha? ",
                "options": ["a. 28 Seats ", "b. 48 Seats ", "c. 58 Seat ", "d. 68 Seats "],
                 "answer": "b"

            },

            {
                "question": "3. What is the State Code of Maharashtra? ",
                "options": ["a.  MA ", "b. MH ", "c. MHA ", "d. MUM "],
                "abswer":"b"
            }

        ]
        score=0
        for q in questions:
            print(q["question"])
            for o in q["options"]:
                print(o)
            answer = input("Enter your answer: ")
            if answer == q["answer"]:
                print("Your answer is correct!")
                score+=1
            else:
                print("Your answer is incorrect.")
            print("Your final score is ",score)

    elif response == 3:
        print("Level Easy")
        print("Level Medium")
        print("Level Hard")
        akash = int(input("Enter your choice 1, 2, 3 = "))
        if akash == 1:

        #medium
        questions = [
            {
                "question": "HHow many seats does Maharashtra have in the Rajya Sabha",
                "options": ["a. 09 Seats ", "b. 12 Seats ", "c. 16 Seats ", "d. 19 Seats "],
                "answer": "d"
            },
            {
                "question": "2. How many seats does Maharashtra have in the Lok Sabha? ",
                "options": ["a. 28 Seats ", "b. 48 Seats ", "c. 58 Seat ", "d. 68 Seats "],
                "answer": "b"

            },

            {
                "question": "3. What is the State Code of Maharashtra? ",
                "options": ["a.  MA ", "b. MH ", "c. MHA ", "d. MUM "],
                "abswer": "b"
            }

        ]
        score = 0
        for q in questions:
            print(q["question"])
            for o in q["options"]:
                print(o)
            answer = input("Enter your answer: ")
            if answer == q["answer"]:
                print("Your answer is correct!")
                score += 1
            else:
                print("Your answer is incorrect.")
            print("Your final score is ", score)

