from dataclasses import dataclass


@dataclass
class Elf:
    calories: int
    elf_id: int


def main():
    with open("input.txt") as file:
        current_elf = Elf(0, 1)
        top_elfs = [Elf(0, 0), Elf(0, 0), Elf(0, 0)]

        for line in file.readlines():
            if line.strip() != "":
                current_elf.calories += int(line.strip())
            else:
                for top in top_elfs:
                    if current_elf.calories > top.calories:
                        top_elfs.insert(top_elfs.index(top), current_elf)
                        top_elfs.pop(-1)
                        break
                current_elf = Elf(0, current_elf.elf_id+1)

    return sum([top.calories for top in top_elfs])


if __name__ == "__main__":
    print(main())
