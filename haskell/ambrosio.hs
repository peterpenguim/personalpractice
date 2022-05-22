jogadas :: Int -> Int -> Int -> Int -> IO ()
jogadas casa ultimacasa n contador = do
    if casa /= ultimacasa
        then do
            if n > 6 then jogadas casa ultimacasa 1 contador
            else if casa > ultimacasa then jogadas (casa - ultimacasa) ultimacasa n contador
            else do 
                jogadas (casa + n) ultimacasa (n + 1) (contador + 1)
    else putStrLn $ show (contador - 1)

main :: IO ()
main = do
    let casa = 1
    let contador = 1
    let n = 1
    ultimacasa' <- getLine
    let ultimacasa = read ultimacasa' :: Int
    jogadas casa ultimacasa n contador