from summarizer import summarize

INPUT_FILE_PATH = "./input.txt"
OUTPUT_FILE_PREFIX = "./output"

def main():
    print("summarizing")
    with open(INPUT_FILE_PATH, "r") as f:
        text = f.read()
    for depth in range(0,2):
        summary = summarize(text, depth=depth)
        print(f'processing... depth #{depth}')
        with open(OUTPUT_FILE_PREFIX + str(depth) + ".txt", "w") as f:
            f.write(summary)

if __name__ == '__main__':
    main()
