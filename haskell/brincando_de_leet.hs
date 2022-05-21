main :: IO()
main = do
 entrada' <- getLine
 let entrada = entrada'
 let soma = (contador entrada 'a' + contador entrada 'A' + contador entrada 'e' + contador entrada 'E' + contador entrada 'o' + contador entrada 'O' + contador entrada 'i' + contador entrada 'I' + contador entrada 't' + contador entrada 'T' + contador entrada 's' + contador entrada 'S')
 if not(null entrada) && (elem '0' entrada || elem '1' entrada || elem '2' entrada || elem '3' entrada || elem '4' entrada || elem '5' entrada || elem '6' entrada || elem '7' entrada || elem '8' entrada || elem '9' entrada)
   then putStrLn $ "numeros\n" ++ show 0
 else if not(null entrada) && not(elem '0' entrada || elem '1' entrada || elem '2' entrada || elem '3' entrada || elem '4' entrada || elem '5' entrada || elem '6' entrada || elem '7' entrada || elem '8' entrada || elem '9' entrada)
   then putStrLn $ reverse (mudarLetra entrada) ++ "\n" ++ show soma
 else putStrLn $ "vazio\n" ++ show 0

mudarLetra [] = []
mudarLetra (x : xs)
  | x == 'a' = '@' : mudarLetra xs
  | x == 'A' = '@' : mudarLetra xs
  | x == 'e' = '3' : mudarLetra xs
  | x == 'E' = '3' : mudarLetra xs
  | x == 'i' = '1' : mudarLetra xs
  | x == 'I' = '1' : mudarLetra xs
  | x == 'o' = '0' : mudarLetra xs
  | x == 'O' = '0' : mudarLetra xs
  | x == 't' = '7' : mudarLetra xs
  | x == 'T' = '7' : mudarLetra xs
  | x == 's' = '5' : mudarLetra xs
  | x == 'S' = '5' : mudarLetra xs
  | otherwise = x : mudarLetra xs

contador :: String -> Char -> Int
contador str c = length $ filter (== c) str
