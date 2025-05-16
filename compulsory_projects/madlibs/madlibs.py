def mad_libs():
    """
    A simple Mad Libs game that prompts the user for various types of words
    and then generates a more fun, adventurous, and engaging story using those words.
    """
    print("Welcome to the Mad Libs adventure!")
    
    # Prompt the user for various types of words
    name = input("Enter a name: ").strip().capitalize()
    place = input("Enter a place: ").strip().capitalize()
    adj = input("Enter an adjective: ").strip()
    random_object = input("Enter a random object: ").strip()
    animal = input("Enter an animal name: ").strip()
    verb = input("Enter a verb: ").strip()
    funny_exclamation = input("Enter a funny exclamation: ").strip()

    # Generate the story
    story = (
        f"In the magical land of {place}, there lived a brave adventurer named {name}.\n"
        f"One day, while exploring the {adj} forest, {name} stumbled upon an ancient {random_object}.\n"
        f"As they reached out to touch it, a mystical {animal} suddenly appeared, soaring through the air!\n"
        f"The {animal} spoke, \"Thank you for freeing me from the {random_object}! I have been trapped here for centuries.\"\n"
        f"With a mix of excitement and disbelief, {name} couldn't help but {verb} in amazement.\n"
        f"\"This is unbelievable!\" {name} gasped. \"{funny_exclamation}! What happens next?\""
    )

    # Print the story
    print("\nHere is your Mad Libs adventure:\n")
    print(story)

if __name__ == "__main__":
    mad_libs()
