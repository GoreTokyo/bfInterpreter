import sys

def run_brainfuck(code):
    code = ''.join(filter(lambda c: c in ['<', '>', '+', '-', '.', ',', '[', ']'], code))
    memory = [0] * 30000
    pointer = 0
    pc = 0
    while pc < len(code):
        cmd = code[pc]
        if cmd == '>':
            pointer += 1
        elif cmd == '<':
            pointer -= 1
        elif cmd == '+':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif cmd == '-':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif cmd == '.':
            print(chr(memory[pointer]), end="")
        elif cmd == ',':
            memory[pointer] = ord(input())
        elif cmd == '[':
            if memory[pointer] == 0:
                open_brackets = 1
                while open_brackets > 0:
                    pc += 1
                    if code[pc] == '[':
                        open_brackets += 1
                    elif code[pc] == ']':
                        open_brackets -= 1
        elif cmd == ']':
            if memory[pointer] != 0:
                close_brackets = 1
                while close_brackets > 0:
                    pc -= 1
                    if code[pc] == '[':
                        close_brackets -= 1
                    elif code[pc] == ']':
                        close_brackets += 1
        pc += 1

if __name__ == '__main__':
    # コマンドライン引数でファイルパスを指定
    if len(sys.argv) != 2:
        print("Usage: python brainfuck_interpreter.py <path_to_bf_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    
    try:
        # 指定したファイルを読み込む
        with open(file_path, 'r') as file:
            bf_code = file.read()
        
        # 読み込んだコードを実行
        run_brainfuck(bf_code)
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
