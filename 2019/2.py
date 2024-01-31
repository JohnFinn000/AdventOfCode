def execute(sequence):
  memory = {i: s for i, s in enumerate(sequence)}

  memory[1] = 12
  memory[2] = 2 

  index = 0 
  while True:
    opcode = sequence[index]
    if opcode == 99: 
      return memory[0]

    left = sequence[index+1]
    right = sequence[index+2]
    result = sequence[index+3]

    if opcode == 1:
      print("%d + %d" % (memory[left], memory[right]))
      memory[result] = memory[left] + memory[right]

    elif opcode == 2:
      print("%d * %d" % (memory[left], memory[right]))
      memory[result] = memory[left] * memory[right]

    index += 4

def read(filepath):
  with open(filepath, "r") as f:
    for line in f.readlines():
      sequence = line.split(",")
      result = execute([int(s) for s in sequence])
      print("Result: %d" % result)

read("2_input.txt")
