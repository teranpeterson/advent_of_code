import Data.Bifunctor
import Data.List
import Data.List.Split
import Data.Set (Set)
import Data.Set qualified as Set
import System.IO
import Text.Regex.Posix

main :: IO ()
main = do
  let list = []
  fileHandle <- openFile "input.txt" ReadMode
  contents <- hGetContents fileHandle
  let rules = [parseRule line | line <- lines contents, '|' `elem` line]
  let updates = [parseUpdate line | line <- lines contents, ',' `elem` line]
  let ruleSet = Set.fromList rules
  print (foldr (\update -> (+) (if verify update ruleSet then center update else 0)) 0 updates)
  hClose fileHandle

parseRule :: String -> (Int, Int)
parseRule line = (left, right)
  where
    split = splitOn "|" line
    left = read (split !! 0)
    right = read (split !! 1)

parseUpdate :: String -> [Int]
parseUpdate line = map read split
  where
    split = splitOn "," line

verify :: [Int] -> Set (Int, Int) -> Bool
verify [x] ruleSet = True
verify (x : xs) ruleSet = (and [Set.member (x, y) ruleSet | y <- xs]) && verify xs ruleSet

center :: [Int] -> Int
center l = l !! (length l `div` 2)
