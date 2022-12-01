from dataclasses import dataclass


@dataclass
class Elf:
    calories: int
    elf_id: int


def main():
    with open("input.txt") as file:
        current_elf = Elf(0, 1)
        top_elf = Elf(0, 0)
        for line in file.readlines():
            if line.strip() != "":
                current_elf.calories += int(line.strip())
            else:
                if top_elf.calories < current_elf.calories:
                    top_elf = current_elf
                current_elf = Elf(0, current_elf.elf_id+1)

        return top_elf.calories


if __name__ == "__main__":
    print(main())
