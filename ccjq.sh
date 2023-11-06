# add this code in either bash_profile file or zshrc file depending on where the command line tools looks for the custom commands

ccjq() {
    # Read the input from stdin
    input=$(cat)

    # Execute your Python program, passing the input and the filter as arguments
    python3 '/Users/Arjun/Documents/personal/proof of concepts/john crickett/jq clone/ccjq.py' "$input" "$1"
}