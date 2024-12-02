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
  let val = bimap sort sort processed
  print (createSum (uncurry zip val))
  hClose fileHandle

splitOnPos :: [a] -> ([a], [a])
splitOnPos [] = ([], [])
splitOnPos (x1 : x2 : xs) = (x1 : odds, x2 : evens)
  where
    (odds, evens) = splitOnPos xs

convertToInt :: [String] -> [Int]
convertToInt = map read

createSum :: (Num a) => [(a, a)] -> a
createSum [] = 0
createSum ((x, y) : xs) = abs (x - y) + createSum xs
