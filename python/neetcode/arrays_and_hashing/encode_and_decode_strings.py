def encode(strs: list[str]) -> str:
    return "".join([f"{len(char)}#{char}" for char in strs])


def decode(string: str) -> list[str]:
    result = []
    i = 0

    while i < len(string):
        j = i
        while string[j] != "#":
            j += 1

        length = int(string[i:j])
        i = j + 1
        j = i + length

        result.append(string[i:j])
        i = j

    return result
