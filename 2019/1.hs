import System.IO
import Control.Monad

fuel_calc mass = (floor (mass / 3)) - 2 

-- fuel_calc mass 

readInt :: String -> Int 
readInt = read

main  = do
        contents <- readFile "1_input.txt"
        print . map readInt  . words $ contents
