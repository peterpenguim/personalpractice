import Data.Char
main :: IO()
main = do
 entrada' <- getLine
 let entrada = entrada'
 let soma = (contador entrada 'a' + contador entrada 'A' + contador entrada 'e' + contador entrada 'E' + contador entrada 'o' + contador entrada 'O' + contador entrada 'i' + contador entrada 'I' + contador entrada 't' + contador entrada 'T' + contador entrada 's' + contador entrada 'S')
 if not(null entrada) && (encontrarElem '0' entrada || encontrarElem '1' entrada || encontrarElem '2' entrada || encontrarElem '3' entrada || encontrarElem '4' entrada || encontrarElem '5' entrada || encontrarElem '6' entrada || encontrarElem '7' entrada || encontrarElem '8' entrada || encontrarElem '9' entrada) 
   then putStrLn $ "numeros\n" ++ show 0
 else if not(null entrada) && not(encontrarElem '0' entrada || encontrarElem '1' entrada || encontrarElem '2' entrada || encontrarElem '3' entrada || encontrarElem '4' entrada || encontrarElem '5' entrada || encontrarElem '6' entrada || encontrarElem '7' entrada || encontrarElem '8' entrada || encontrarElem '9' entrada)
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

encontrarElem _ [] = False
encontrarElem n (x:xs)
  | x == n = True
  | otherwise = encontrarElem n xs
