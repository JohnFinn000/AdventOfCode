import java.io.*;
import java.util.*;

class FuelCalc {
  // Not the most efficient, but on to the next!!
  private static int CalculateFuel(int mass) {
    if (mass < 0) {
      return 0;
    }
    int fuel = (mass / 3) - 2;
    fuel += CalculateFuel(fuel);
    if (fuel < 0) {
      return 0;
    }
    return fuel;
  }

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
    String[] str_list = contentBuilder.toString().split("\n");
    List<Integer> mass_list = new ArrayList<Integer>();
    for (String temp : str_list) {
      int num = Integer.parseInt(temp);
      mass_list.add(num);
    }   
    return mass_list;
  }

  public static void main(String args[]) {
    List<Integer> mass_list = ReadInput("1_input.txt");
    int total_fuel = 0;
    for (int index = 0; index < mass_list.size(); index++) {
      total_fuel += CalculateFuel(mass_list.get(index));
    }   
    System.out.println("Total Fuel: " + total_fuel);
  }
}
