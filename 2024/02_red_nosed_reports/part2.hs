import Data.Bifunctor
import Data.List
import System.IO

main :: IO ()
main = do
  let list = []
  fileHandle <- openFile "input.txt" ReadMode
  contents <- hGetContents fileHandle
  let reports = [[read word :: Int | word <- words line] | line <- lines contents]
  let count = foldl (\x xs -> x + fromEnum (checkReportV2 xs)) 0 reports
  print count
  hClose fileHandle

checkReportV2 :: [Int] -> Bool
checkReportV2 report = checkReport report || doubleCheckReport report

doubleCheckReport :: [Int] -> Bool
doubleCheckReport report = checkReportWithRemoval (length report - 1) report

checkReportWithRemoval :: Int -> [Int] -> Bool
checkReportWithRemoval 0 report = checkReport (deleteAt 0 report)
checkReportWithRemoval n report = checkReport (deleteAt n report) || checkReportWithRemoval (n - 1) report

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

deleteAt :: Int -> [a] -> [a]
deleteAt idx xs = left ++ right where (left, _ : right) = splitAt idx xs
