from dataclasses import dataclass


@dataclass
class Elf:
    calories: int
    elf_id: int


def main():
    with open("input.txt") as file:
        current_elf = Elf(0, 1)
        fat_elf = None
        for line in file.readlines():
            if line.strip() != "":
                current_elf.calories += int(line.strip())
            else:
                if fat_elf is None or fat_elf.calories < current_elf.calories:
                    fat_elf = current_elf
                current_elf = Elf(0, current_elf.elf_id+1)

        return fat_elf


if __name__ == "__main__":
    print(main())
