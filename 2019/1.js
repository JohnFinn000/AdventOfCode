var fs = require('fs');
var path = require('path');

function calc_fuel(mass) {
  if (mass < 0) {
    return 0
  }
  var fuel = Math.floor(mass / 3) - 2 
  if (fuel > 0) {
    return fuel + calc_fuel(fuel)
  }
  return 0
}

function parse_input(filepath) {
  return fs.readFileSync(path.join(__dirname, filepath)).toString();
}

function calculate_fuel(filepath) {
  var mass_list = parse_input(filepath).trim().split('\n')
  var total_fuel = 0 
  for (index in mass_list) {
    total_fuel += calc_fuel(parseInt(mass_list[index], 10))
  }
  return total_fuel
}

console.log('Total fuel: ' + calculate_fuel('1_input.txt'))
