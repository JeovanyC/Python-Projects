import re

def main() -> None:
    print(parse(input("HTML: ")))

def parse(htmlURL: str) -> str:
    youtubeURL = re.search(r"https?://(www\.)?youtube\.com/embed/[a-zA-Z0-9_-]+", htmlURL)
    
    if youtubeURL:

        originalURL = youtubeURL.group(0)

        shortURL = re.sub(r"(www\.)?youtube\.com/embed", "youtu.be", originalURL)
        return shortURL


if __name__ == "__main__":
    main()