import java.io.*;
import java.util.*;

class IntCode {
  private static List<Integer> ReadInput(String filepath) {
    StringBuilder contentBuilder = new StringBuilder();
    try (BufferedReader br = new BufferedReader(new FileReader(filepath))) {
      String line;
      while ((line = br.readLine()) != null) {
        contentBuilder.append(line).append("\n");
      }   
    } catch (IOException e) {
      e.printStackTrace();
    }   
    String[] str_list = contentBuilder.toString().replace("\n", "").split(",");
    List<Integer> intCode = new ArrayList<Integer>();
    for (String temp : str_list) {
      int num = Integer.parseInt(temp);
      intCode.add(num);
    }   
    return intCode;
  }

  private static int Calculate(List<Integer> intCode) {
    Map<Integer, Integer> memory = new Hashtable<Integer, Integer>();
    for (int i = 0; i < intCode.size(); i++) {
      memory.put(i, intCode.get(i));
    }   
    memory.put(1, 12);
    memory.put(2, 2); 

    for (int index = 0; index < intCode.size(); index += 4) {                                                                                                                                                                                                                                                                                    
      int opcode = intCode.get(index);
      if (opcode == 99) {
        break;
      }   
      int left = intCode.get(index + 1); 
      int right = intCode.get(index + 2); 
      int result = intCode.get(index + 3); 
      if (opcode == 1) {
        System.out.println(memory.get(left) + " + " + memory.get(right));
        memory.put(result, memory.get(left) + memory.get(right));
      } else if (opcode == 2) {
        System.out.println(memory.get(left) + " * " + memory.get(right));
        memory.put(result, memory.get(left) * memory.get(right));
      }   
    }   
    return memory.get(0);
  }

  public static void main(String args[]) {
    List<Integer> intCode = ReadInput("2_input.txt");
    System.out.println("ArrayList: " + intCode);
    System.out.println(Calculate(intCode));
  }
}
