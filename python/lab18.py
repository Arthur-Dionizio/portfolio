###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - A Caçada I
# Nome: Arthur Dionizio Martins da Silva
# RA: 250814
###################################################

def hunt_simulation(levels, n, m):
    collected_petiscos = 0
    current_level = 0
    current_pos = 0
    direction = 1
    traversed_positions = [[] for _ in range(levels)]

    while current_level < levels:
        platform = platforms[current_level]

        if platform[current_pos] == '*':
            collected_petiscos += 1
            platform[current_pos] = '_'
        if platform[current_pos] == '.':
            current_level += 1
            if current_level >= levels:
                break
            platform = platforms[current_level]
            if platform[current_pos] == '*':
                collected_petiscos += 1
                platform[current_pos] = '_'

        traversed_positions[current_level].append(current_pos)

        if current_pos == 0 and direction == -1:
            direction = 1
            current_pos += 1
        elif current_pos == m - 1 and direction == 1:
            current_pos -= 1
            direction = -1
        else:
            if platform[current_pos] != '.':
                current_pos += direction

        if len(traversed_positions[current_level]) == n*m and platform[current_pos] != '.':
            break

    return collected_petiscos


# Read the number of levels
levels = int(input())

# Read the platforms representation
platforms = [list(input()) for _ in range(levels)]

# Get the dimensions of the platforms
n = len(platforms)
m = len(platforms[0])

# Calculate the number of collected petiscos
collected_petiscos = hunt_simulation(levels, n, m)

# Print the result
print(collected_petiscos)
