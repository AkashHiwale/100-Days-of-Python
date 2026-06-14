with open("./Input/Letters/starting_letter.txt") as invitation_file:
    invitation = invitation_file.read()

    with open("./Input/Names/invited_names.txt") as invited_names_file:
        invited_names = invited_names_file.readlines()

        for name in invited_names:
            name = name.replace("\n", "")
            invitation_text = invitation
            invitation_text = invitation_text.replace("[name]", name)
            with open(f"./Output/ReadyToSend/{name}_Invitation.txt", "w") as file:
                file.write(invitation_text)