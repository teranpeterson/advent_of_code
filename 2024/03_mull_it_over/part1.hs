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
  let mulRegex = "mul\\([0-9]+,[0-9]+\\)"
  let commands = getAllTextMatches (contents =~ mulRegex) :: [String]
  print (sum [multiply command | command <- commands])
  hClose fileHandle

multiply :: String -> Int
multiply command = left * right
  where
    split = splitOn "," command
    left = read (drop 4 (split !! 0))
    right = read (reverse (drop 1 (reverse (split !! 1))))
