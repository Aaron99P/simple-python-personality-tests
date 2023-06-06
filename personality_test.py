import random
import os

#Import the questionnaries
import questionnaries.NEOPIR as NEOPIR
import questionnaries.MiniIPIP as MiniIPIP


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
    print('-----------------------------')
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
        print('***************************')
        print('Error. Choose a valid option')
        print('***************************')
        print()
        return choose_test()


def choose_shuffle(test_questions):
    print()
    print('Shuffle questions:')
    print('-----------------------------')
    print('1. Yes. (Recommended)')
    print('2. No')
    print()
    response = input("Enter the number of the option: ")
    if (int(response)==1):
        random.shuffle(test_questions.questions)
    elif (int(response)==2):
        pass
    else:
        print()
        print('*****************')
        print('Error. Choose a valid option')
        print('*****************')
        print()
        return choose_shuffle()


def save_results():
    print()
    print("Saving results")
    print('-----------------------------')
    print()
    name = input("Write the name under which you want to save the results: ")
    path = "results/"
    if not os.path.exists(path):
        os.makedirs(path)
    f = open("results/results.txt", "a")

    f.write(f'{name}\n')
    f.write('*****************************\n\n')
    f.write("Results on a scale of -1 to 1\n")
    f.write('-----------------------------\n')
    for trait, score in trait_scores.items():
        min_value = score["min_score"]
        max_value = score["max_score"]
        normalized_value = 2 * (score["score"] - min_value) / (max_value - min_value) - 1
        f.write(f'{trait}: {round(normalized_value, 2)}\n')
    f.write('\n')

    f.write("Results on a scale of 0 to 1\n")
    f.write('-----------------------------\n')
    for trait, score in trait_scores.items():
        min_value = score["min_score"]
        max_value = score["max_score"]
        normalized_value = (score["score"] - min_value) / (max_value - min_value)
        f.write(f'{trait}: {round(normalized_value, 2)}\n')
    f.write('\n\n\n')


def administer_test():
    test_questions = choose_test()
    choose_shuffle(test_questions)

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
        print("-----------------------------")

    #Show results
    print("\n\n")
    print("Results (scale -1 to 1):")
    print("-----------------------------")
    for trait, score in trait_scores.items():
        min_value = score["min_score"]
        max_value = score["max_score"]
        normalized_value = 2 * (score["score"] - min_value) / (max_value - min_value) - 1
        print(f'{trait}: {round(normalized_value, 2)}')
    print("\n\n")
    print("Results (scale 0 to 1):")
    print("-----------------------------")
    for trait, score in trait_scores.items():
        min_value = score["min_score"]
        max_value = score["max_score"]
        normalized_value = (score["score"] - min_value) / (max_value - min_value)
        print(f'{trait}: {round(normalized_value, 2)}')

    #Save results
    save_results() 
    

if __name__ == "__main__":
    administer_test()