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
  | puzzle !! n /= 'X' = wordSearch puzzle (n + 1)
  | otherwise = countMatches puzzle n + wordSearch puzzle (n + 1)

countMatches :: String -> Int -> Int
countMatches puzzle n = foldl (\x xs -> x + if xs == "XMAS" || xs == "SAMX" then 1 else 0) 0 (extractAll puzzle n)

extractAll :: String -> Int -> [String]
extractAll puzzle n = [right puzzle n, left puzzle n, up puzzle n, down puzzle n, diagDL puzzle n, diagDR puzzle n, diagUL puzzle n, diagUR puzzle n]

right :: String -> Int -> String
right puzzle n
  | (n + 3) `div` l >= h = "NONE"
  | n `div` l /= (n + 3) `div` l = "NONE"
  | otherwise = [puzzle !! n, puzzle !! (n + 1), puzzle !! (n + 2), puzzle !! (n + 3)]

left :: String -> Int -> String
left puzzle n
  | (n + 3) `div` l < 0 = "NONE"
  | n `div` l /= (n - 3) `div` l = "NONE"
  | otherwise = [puzzle !! n, puzzle !! (n - 1), puzzle !! (n - 2), puzzle !! (n - 3)]

down :: String -> Int -> String
down puzzle n
  | n `div` l + 3 >= h = "NONE"
  | otherwise = [puzzle !! n, puzzle !! (n + 1 * l), puzzle !! (n + 2 * l), puzzle !! (n + 3 * l)]

up :: String -> Int -> String
up puzzle n
  | n `div` l - 3 < 0 = "NONE"
  | otherwise = [puzzle !! n, puzzle !! (n - 1 * l), puzzle !! (n - 2 * l), puzzle !! (n - 3 * l)]

diagDR :: String -> Int -> String
diagDR puzzle n
  | (n + 3 * l + 3) `div` l >= h = "NONE"
  | n `mod` l >= (n + 3 * l + 3) `mod` l = "NONE"
  | otherwise = [puzzle !! n, puzzle !! (n + 1 * l + 1), puzzle !! (n + 2 * l + 2), puzzle !! (n + 3 * l + 3)]

diagDL :: String -> Int -> String
diagDL puzzle n
  | (n + 3 * l + 3) `div` l >= h = "NONE"
  | n `mod` l < (n + 3 * l - 3) `mod` l = "NONE"
  | otherwise = [puzzle !! n, puzzle !! (n + 1 * l - 1), puzzle !! (n + 2 * l - 2), puzzle !! (n + 3 * l - 3)]

diagUR :: String -> Int -> String
diagUR puzzle n
  | (n - 3 * l + 3) `div` l < 0 = "NONE"
  | n `mod` l >= (n - 3 * l + 3) `mod` l = "NONE"
  | otherwise = [puzzle !! n, puzzle !! (n - 1 * l + 1), puzzle !! (n - 2 * l + 2), puzzle !! (n - 3 * l + 3)]

diagUL :: String -> Int -> String
diagUL puzzle n
  | (n - 3 * l - 3) `div` l < 0 = "NONE"
  | n `mod` l < (n - 3 * l - 3) `mod` l = "NONE"
  | otherwise = [puzzle !! n, puzzle !! (n - 1 * l - 1), puzzle !! (n - 2 * l - 2), puzzle !! (n - 3 * l - 3)]
