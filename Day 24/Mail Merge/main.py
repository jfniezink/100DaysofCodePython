with open("Input\Letters\starting_letter.txt") as start_file:
    letter = start_file.read()

with open("Input\\Names\invited_names.txt") as invited_file:
    lines = invited_file.readlines()
    for line in lines:
        toname = line.strip()
        readyletter = letter.replace("[name]", toname)
        #Replace the [name] placeholder with the actual name.
        with open(f"Output\ReadyToSend\Letter_for_{toname}.txt", mode="w") as output:
            output.write(readyletter)

