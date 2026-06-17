import time

# ==========================
# DETECTIVE CHRONICLES
# ==========================

total_score = 0
cases_solved = 0


def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()


def line():
    print("=" * 60)


def case_101():
    global total_score, cases_solved

    score = 0

    line()
    print("CASE FILE #101 - THE MISSING DIAMOND")
    line()

    slow_print("A priceless diamond has been stolen from the Royal Mansion.")
    slow_print("Your mission is to identify the thief.")

    print("\nSuspects:")
    print("1. Butler")
    print("2. Gardener")
    print("3. Chef")

    choice = input("\nWho do you investigate first? ")

    if choice == "2":
        slow_print("\nThe Gardener appears nervous.")
        slow_print("You notice mud on his boots.")
        score += 1
    elif choice == "1":
        slow_print("\nThe Butler has a solid alibi.")
    elif choice == "3":
        slow_print("\nThe Chef was preparing dinner.")
    else:
        slow_print("\nInvalid choice.")

    print("\nChoose a clue:")
    print("1. Security Camera")
    print("2. Fingerprints")
    print("3. Garden Shed")

    clue = input("Select clue: ")

    if clue == "1":
        slow_print("\nCamera footage shows movement near the greenhouse.")
        score += 1
    elif clue == "2":
        slow_print("\nFingerprints are inconclusive.")
    elif clue == "3":
        slow_print("\nFreshly dug soil is discovered.")
        score += 1

    line()
    print("FINAL ACCUSATION")
    line()

    accuse = input("Who stole the diamond? (1/2/3): ")

    if accuse == "2":
        slow_print("\nCorrect!")
        slow_print("The Gardener buried the diamond in the greenhouse.")
        slow_print("CASE SOLVED!")
        cases_solved += 1
        total_score += score + 3
    else:
        slow_print("\nWrong accusation.")
        slow_print("The thief escaped.")
        total_score += score

    print(f"\nCase Score: {score}/2")


def case_102():
    global total_score, cases_solved

    score = 0

    line()
    print("CASE FILE #102 - THE MUSEUM HEIST")
    line()

    slow_print("A famous painting has disappeared from the city museum.")

    print("\nSuspects:")
    print("1. Security Guard")
    print("2. Curator")
    print("3. Electrician")

    suspect = input("\nInvestigate: ")

    if suspect == "3":
        slow_print("\nThe Electrician recently requested unusual access.")
        score += 1
    elif suspect == "1":
        slow_print("\nThe Guard appears cooperative.")
    elif suspect == "2":
        slow_print("\nThe Curator has no suspicious history.")

    print("\nChoose evidence:")
    print("1. CCTV Logs")
    print("2. Maintenance Records")
    print("3. Visitor Book")

    evidence = input("Select evidence: ")

    if evidence == "2":
        slow_print("\nUnauthorized maintenance request found.")
        score += 1
    elif evidence == "1":
        slow_print("\nCameras were disabled for five minutes.")
        score += 1
    elif evidence == "3":
        slow_print("\nNothing suspicious discovered.")

    line()
    print("FINAL ACCUSATION")
    line()

    accuse = input("Who stole the painting? (1/2/3): ")

    if accuse == "3":
        slow_print("\nExcellent work Detective!")
        slow_print("The Electrician disabled the security system.")
        slow_print("CASE SOLVED!")
        cases_solved += 1
        total_score += score + 3
    else:
        slow_print("\nIncorrect accusation.")
        total_score += score

    print(f"\nCase Score: {score}/2")


def case_103():
    global total_score, cases_solved

    score = 0

    line()
    print("CASE FILE #103 - THE ANONYMOUS MURDER")
    line()

    slow_print("A wealthy businessman has been found dead.")

    print("\nSuspects:")
    print("1. Business Partner")
    print("2. Personal Assistant")
    print("3. Brother")

    suspect = input("\nInvestigate: ")

    if suspect == "1":
        slow_print("\nThe Business Partner avoids eye contact.")
        score += 1
    elif suspect == "2":
        slow_print("\nThe Assistant seems shocked.")
    elif suspect == "3":
        slow_print("\nThe Brother has a weak motive.")

    print("\nChoose evidence:")
    print("1. Phone Records")
    print("2. Financial Documents")
    print("3. Witness Statement")

    evidence = input("Select evidence: ")

    if evidence == "2":
        slow_print("\nFraudulent transactions discovered.")
        score += 1
    elif evidence == "1":
        slow_print("\nThreatening messages found.")
        score += 1
    elif evidence == "3":
        slow_print("\nWitness testimony is unclear.")

    line()
    print("FINAL ACCUSATION")
    line()

    accuse = input("Who committed the murder? (1/2/3): ")

    if accuse == "1":
        slow_print("\nOutstanding investigation!")
        slow_print("The Business Partner committed the murder.")
        slow_print("CASE SOLVED!")
        cases_solved += 1
        total_score += score + 3
    else:
        slow_print("\nWrong accusation.")
        total_score += score

    print(f"\nCase Score: {score}/2")


def detective_rank():
    if cases_solved == 3:
        return "MASTER INVESTIGATOR"
    elif cases_solved == 2:
        return "SENIOR DETECTIVE"
    elif cases_solved == 1:
        return "JUNIOR DETECTIVE"
    else:
        return "TRAINEE DETECTIVE"


def show_stats():
    line()
    print("DETECTIVE REPORT")
    line()
    print(f"Cases Solved : {cases_solved}/3")
    print(f"Total Score  : {total_score}")
    print(f"Rank         : {detective_rank()}")
    line()


def main():
    while True:

        line()
        print("      DETECTIVE CHRONICLES")
        print("   Solve Crimes. Catch Criminals.")
        line()

        print("1. Case File #101 - Missing Diamond")
        print("2. Case File #102 - Museum Heist")
        print("3. Case File #103 - Anonymous Murder")
        print("4. Detective Report")
        print("5. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            case_101()

        elif choice == "2":
            case_102()

        elif choice == "3":
            case_103()

        elif choice == "4":
            show_stats()

        elif choice == "5":
            line()
            print("Thank you for playing Detective Chronicles!")
            print(f"Final Rank: {detective_rank()}")
            line()
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
    