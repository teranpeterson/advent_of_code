import Data.Bifunctor
import Data.List
import Data.List.Split
import System.IO
import Text.Regex.Posix

main :: IO ()
main = do
  let list = []
  fileHandle <- openFile "input.txt" ReadMode
  contents <- hGetContents fileHandle
  let mulRegex = "(mul\\([0-9]+,[0-9]+\\)|do\\(\\)|don't\\(\\))"
  let commands = getAllTextMatches (contents =~ mulRegex) :: [String]
  let values = [execute command | command <- commands]
  print values
  print (sum2 1 values)
  hClose fileHandle

execute :: String -> Int
execute ['d', 'o', '(', ')'] = 1
execute ['d', 'o', 'n', '\'', 't', '(', ')'] = 0
execute command = multiply command

multiply :: String -> Int
multiply command = left * right
  where
    split = splitOn "," command
    left = read (drop 4 (split !! 0))
    right = read (reverse (drop 1 (reverse (split !! 1))))

sum2 :: Int -> [Int] -> Int
sum2 n [] = 0
sum2 0 [x] = 0
sum2 1 [x] = x
sum2 0 (0 : xs) = sum2 0 xs
sum2 0 (1 : xs) = sum2 1 xs
sum2 1 (0 : xs) = sum2 0 xs
sum2 1 (1 : xs) = sum2 1 xs
sum2 0 (x : xs) = sum2 0 xs
sum2 1 (x : xs) = x + sum2 1 xs