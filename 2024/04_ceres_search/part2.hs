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
  let trimmed = [c | c <- contents, c /= '\n']
  print (wordSearch trimmed 0)
  hClose fileHandle

l = 140

h = 140

wordSearch :: String -> Int -> Int
wordSearch puzzle n
  | n >= l * h = 0
  | puzzle !! n /= 'A' = wordSearch puzzle (n + 1)
  | otherwise = countMatches puzzle n + wordSearch puzzle (n + 1)

countMatches :: String -> Int -> Int
countMatches puzzle n = if value == "MMASS" || value == "MSAMS" || value == "SMASM" || value == "SSAMM" then 1 else 0
  where
    value = extractX puzzle n

extractX :: String -> Int -> String
extractX puzzle n
  | (n + 1 * l + 1) `div` l >= h = "NONE"
  | (n - 1 * l + 1) `div` l < 0 = "NONE"
  | n `mod` l < (n + 1 * l - 1) `mod` l = "NONE"
  | n `mod` l >= (n + 1 * l + 1) `mod` l = "NONE"
  | otherwise = [puzzle !! (n - 1 * l - 1), puzzle !! (n - 1 * l + 1), puzzle !! n, puzzle !! (n + 1 * l - 1), puzzle !! (n + 1 * l + 1)]
