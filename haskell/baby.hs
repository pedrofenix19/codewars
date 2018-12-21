doubleMe x = x + x
doubleUs x y = x*2 + y*2
factorial x = if x == 1 then 1 else factorial (x-1) * x
fibonacci x = if x == 0 then 0 else if x ==1 then 1 else fibonacci (x-1) + fibonacci (x-2)

fibonacci2 :: (Integral a) => a -> Integer
fibonacci2 0 = 0
fibonacci2 1 = 1
fibonacci2 n = fibonacci2 (n-1) + fibonacci2 (n-2)

rev :: [x] -> [x]
rev x = if null x  then [] else last x : rev (init x)
evenTo x = [2,4..x]
evenFrom x = reverse (evenTo x)
evenFrom2 x = if x `mod` 2 == 0 then [x,x-2..1] else [x-1,x-3..1]

evenTo3 n = [x*2 | x <- [1..floor (n/2)]]
evenTo4 n = [x | x <- [1..n], x `mod` 2 == 0]

--isPrime :: (Integral a) => a -> Bool
--isPrime n = if null [x | x <- [2..ceiling (sqrt n)], n `mod` x == 0] then True else False
--primesUpTo n = [x | x <- [1..n], isPrime x]
substring :: [Char] -> Int -> Int -> [Char]
substring str start end = [ str!!x | x <- [start..end] ]

first :: (a,b,c) -> a
first (a,_,_) = a

head2 :: [a] -> a
head2 [] = error "Lista vacia"
head2 (x:_) = x

encolar :: a -> [a] -> [a]
encolar a b = a:b

--desencolar :: [a] -> a
--desencolar a = 

tell :: (Show a) => [a] -> String
tell [] = "Lista vacia"
tell (x:[]) = "Un elemento: " ++ show x
tell (x:y:[]) = "Dos " ++ show x ++ " y " ++ show y
tell (x:y:_) = "Hay mas de dos"

sum2 :: (Num a) => [a] -> a
sum2 [] = 0
sum2 (x:xs) = x + sum2 xs

--as patterns
firstLetter :: String -> String
firstLetter "" = "String vacio"
firstLetter str@(a:b) = "La primera letra de " ++ show str ++ " es " ++ show a ++ " y el resto es " ++ show b

--guards
edad :: Integer -> String
edad x 
    | x < 2 = "Eres un bebe"
    | x < 13 = "Eres un infante"
    | x <= 19 = "Eres un adolescente"
    | otherwise = "Eres un adulto"

primesUpTo2 :: Integer -> [Integer]
primesUpTo2 n = [x | x <- [1..n], isPrime x]
    where isPrime n 
            | [x | x <- [2..n-1], n `mod` x == 0] == [] = True 
            | otherwise = False