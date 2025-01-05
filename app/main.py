import sys


def main():
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()


    # Uncomment this block to pass the first stage
    if file_contents:
        output = []
        error_output = []
        for c in file_contents:
            if c == '(':
                output.append("LEFT_PAREN ( null")
            elif c == ')':
                output.append("RIGHT_PAREN ) null")
            elif c == '{':
                output.append("LEFT_BRACE { null")
            elif c == '}':
                output.append("RIGHT_BRACE } null")
            elif c == ',':
                output.append("COMMA , null")
            elif c == '.':
                output.append("DOT . null")
            elif c == '-':
                output.append("MINUS - null")
            elif c == '+':
                output.append("PLUS + null")
            elif c == ';':
                output.append("SEMICOLON ; null")
            elif c == '*':
                output.append("STAR * null")
            else:
                error_output.append(f"[line 1] Error: Unexpected character: {c}")
        output.append("EOF  null")
        
        for err_out in error_output:
            print(err_out, file=sys.stderr)
        for out in output:
            print(out)
            
    else:
        print("EOF  null") # Placeholder, remove this line when implementing the scanner


if __name__ == "__main__":
    main()
