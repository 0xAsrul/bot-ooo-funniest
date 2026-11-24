"""Out-of-office entry: one funny line, written to /output/entry.txt."""

LINE = "I'm out of office until Monday. My inbox quit too, left a note saying it finally feels seen, and hasn't replied since."

MAX_CHARS = 140

assert isinstance(LINE, str)
assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, must be 1-140"
assert LINE == LINE.strip(), "line must not have leading/trailing whitespace"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE.strip(), "line must not be blank"


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
