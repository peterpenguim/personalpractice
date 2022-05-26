import Data.Char
main :: IO ()
main = do
    entrada <- getLine
    let lista = wordsWhen (==' ') (removeProibidos (map toLower entrada))
    if entrada /= "-1"
        then do
            print $ lista
            main
    else putStrLn "cabou"

removeProibidos xs = [x | x <- xs, not(x `elem` ['.','"','(','*','$','#',':'])]

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
                      "" -> []
                      s' -> w : wordsWhen p s''
                            where (w, s'') = break p s'