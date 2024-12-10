import Data.Bifunctor
import Data.List
import System.IO

main :: IO ()
main = do
  let list = []
  fileHandle <- openFile "input.txt" ReadMode
  contents <- hGetContents fileHandle
  let reports = [[read word :: Int | word <- words line] | line <- lines contents]
  let count = foldl (\x xs -> x + fromEnum (checkReport xs)) 0 reports
  print count
  hClose fileHandle

checkReport :: [Int] -> Bool
checkReport report = checkIncrease report || checkDecrease report

checkIncrease :: [Int] -> Bool
checkIncrease [] = True
checkIncrease [x] = True
checkIncrease (x : y : xs) = x < y && abs (x - y) <= 3 && checkIncrease (y : xs)

checkDecrease :: [Int] -> Bool
checkDecrease [] = True
checkDecrease [x] = True
checkDecrease (x : y : xs) = x > y && abs (x - y) <= 3 && checkDecrease (y : xs)