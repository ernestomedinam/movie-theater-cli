
# función que verifica la elección del usuario con respecto
# al menú principal
def get_choice(text = None):
    """ gets users choice from a numbered list """
    try:
        choice = int(input(text if text else "Choose something...\n"))
        return choice
    except Exception as error:
        print("Please don't be a douche, input a valid number.")
        return 0