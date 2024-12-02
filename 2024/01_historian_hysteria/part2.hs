import Data.Bifunctor
import Data.List
import System.IO

main :: IO ()
main = do
  let list = []
  fileHandle <- openFile "input.txt" ReadMode
  contents <- hGetContents fileHandle
  let singleWords = words contents
  let split = splitOnPos singleWords
  let processed = bimap convertToInt convertToInt split
  print (uncurry calculate processed)
  hClose fileHandle

splitOnPos :: [a] -> ([a], [a])
splitOnPos [] = ([], [])
splitOnPos (x1 : x2 : xs) = (x1 : odds, x2 : evens)
  where
    (odds, evens) = splitOnPos xs

convertToInt :: [String] -> [Int]
convertToInt = map read

countOccurrences :: Int -> [Int] -> Int
countOccurrences x = length . filter (x ==)

calculate :: [Int] -> [Int] -> Int
calculate [] ys = 0
calculate (x : xs) ys = (x * countOccurrences x ys) + calculate xs ys
