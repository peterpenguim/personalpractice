main :: IO()
main = do
 entrada' <- getLine
 let entrada = entrada'
 putStrLn $ reverse (replaceO entrada)
 print (countLetters entrada 'a' + countLetters entrada 'A' + countLetters entrada 'e' + countLetters entrada 'E' + countLetters entrada 'o' + countLetters entrada 'O' + countLetters entrada 'i' + countLetters entrada 'I' + countLetters entrada 't' + countLetters entrada 'T' + countLetters entrada 's' + countLetters entrada 'S')

replaceO [] = []
replaceO (x : xs)
  | x == 'a' = '@' : replaceO xs
  | x == 'A' = '@' : replaceO xs
  | x == 'e' = '3' : replaceO xs
  | x == 'E' = '3' : replaceO xs
  | x == 'i' = '1' : replaceO xs
  | x == 'I' = '1' : replaceO xs
  | x == 'o' = '0' : replaceO xs
  | x == 'O' = '0' : replaceO xs
  | x == 't' = '7' : replaceO xs
  | x == 'T' = '7' : replaceO xs
  | x == 's' = '5' : replaceO xs
  | x == 'S' = '5' : replaceO xs
  | otherwise = x : replaceO xs

countLetters :: String -> Char -> Int
countLetters str c = length $ filter (== c) str