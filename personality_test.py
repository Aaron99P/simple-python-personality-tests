import NEOPIR
import MiniIPIP


trait_scores = {
    "Openness": {"score": 0, "max_score": 0, "min_score": 0},
    "Conscientiousness": {"score": 0, "max_score": 0, "min_score": 0},
    "Extraversion": {"score": 0, "max_score": 0, "min_score": 0},
    "Agreeableness": {"score": 0, "max_score": 0, "min_score": 0},
    "Neuroticism": {"score": 0, "max_score": 0, "min_score": 0}
}


def update_score(trait, response, value):
    trait_scores[trait]["score"] += int(response) * value
    trait_scores[trait]["max_score"] += max(5 * value, 1 * value)
    trait_scores[trait]["min_score"] += min(5 * value, 1 * value)


def choose_test():
    print()
    print('Choose one of the available questionnaries:')
    print('------------')
    print('1. NEO-PI-R')
    print('2. Mini-IPIP')
    print()
    response = input("Enter the number of the questionnaire: ")
    if (int(response)==1):
        return NEOPIR
    elif (int(response)==2):
        return MiniIPIP
    else:
        print()
        print('*****************')
        print('Error. Choose a valid questionnarie')
        print('*****************')
        print()
        return choose_test()


def administer_test():
    test_questions = choose_test()

    #Test
    for trait, question, value in test_questions.questions:
        print()
        print(f'Question: {question}')
        print()
        print("5 - Very accurate")
        print("4 - Moderately accurate")
        print("3 - Neither Accurate Nor Inaccurate")
        print("2 - Moderately inaccurate")
        print("1 - Very inaccurate")
        print()
        response = input("Enter your response (1-5): ")
        update_score(trait, response, value)
        print()
        #print(trait_scores)
        print('-------------------------')
            

    #Show results
    print("\n\n")
    print("Results (scale -1/1):")
    print("-----------------------------")
    for trait, score in trait_scores.items():
        min_value = score["min_score"]
        max_value = score["max_score"]
        normalized_value = 2 * (score["score"] - min_value) / (max_value - min_value) - 1
        #print(f'{trait}: {score["score"]} -> {normalized_value}')
        print(f'{trait}: {normalized_value}')
    

if __name__ == "__main__":
    administer_test()