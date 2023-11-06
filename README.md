# Build your own jq tool - Python
jq is a lightweight and powerful command line tool for handling json parsing. It is used a tool to perform JSON parsing, filtering, transformation, pretty printing etc.

This is a python implementation of jq tool


## Installation
1. Set up the bash_profile or zshrc to trigger a python program upon a command execution
```sh
sudo nano ~/.bash_profile
```

or 
```sh
sudo nano ~/.zshrc
```

Alternatively we can use vim or other editors

2. paste below code.
```sh
ccjq() {
    # Read the input from stdin
    input=$(cat)

    # Execute your Python program, passing the input and the filter as arguments
    #change the folder path as necessary
    python3 '/Users/Arjun/Documents/jq clone/ccjq.py' "$input" "$1"
}
```
3. save the file. `Esc` + `:wq` in nano or  `ctrl+o` in vim.

4. Open command prompt or terminal(in mac) and run the below test commands.

## Test commands

```sh

curl -s 'https://dummyjson.com/quotes?limit=2' | ccjq
curl -s 'https://api.github.com/repos/CodingChallegesFYI/SharedSolutions/commits?per_page=3' | ccjq '.[0]'
curl -s 'https://dummyjson.com/quotes?limit=2' | ccjq '.quotes'
curl -s 'https://dummyjson.com/quotes?limit=2' | ccjq '.code'
curl -s 'https://api.github.com/repos/CodingChallegesFYI/SharedSolutions/commits?per_page=3' | ccjq '.[0] | .commit.message'
curl -s 'https://dummyjson.com/quotes?limit=2' | ccjq '[.quotes[].quote]'

```