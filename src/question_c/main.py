from question_c import get_most_likely_ancestor_consensus

def main():
    running = True
    while running:
        try:
            dna_string1 = input("Enter a dna string (8-16 characters upper case)")
            if not (8 <= len(dna_string1) <= 16):
                raise ValueError("Invalid Entry. Entry must be between 8 to 16 characters.")
            if not dna_string1.isupper():
                raise TypeError("Invalid Entry. Entry must be upper case characters.")
            break
        except TypeError as te:
            print("Error:", te)
        except ValueError as ve:
            print("Error:", ve)
        
    running = True
    while running:
        try:
            dna_string2 = input("Enter a dna string (4 characters upper case)")
            if not (len(dna_string2) == 4):
                raise ValueError("Invalid Entry. Entry must be 4 characters.")
            if not dna_string2.isupper():
                raise TypeError("Invalid Entry. Entry must be upper case characters.")
            break
        except TypeError as te:
            print("Error:", te)
        except ValueError as ve:
            print("Error:", ve)


    positions = get_most_likely_ancestor_consensus(dna_string1, dna_string2)

    if positions:
        print("Substring found at positions:", *positions)

    else:
        print("Substring not found in dna string.")

if __name__ == '__main__':
    main()

    
