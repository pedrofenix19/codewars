doubleMe x = x + x
doubleUs x y = x*2 + y*2
factorial x = if x == 1 then 1 else factorial (x-1) * x
fibonacci x = if x == 0 then 0 else if x ==1 then 1 else fibonacci (x-1) + fibonacci (x-2)
rev :: [x] -> [x]
rev x = if null x  then [] else last x : rev (init x)
evenTo x = [2,4..x]
evenFrom x = reverse (evenTo x)
evenFrom2 x = if x `mod` 2 == 0 then [x,x-2..1] else [x-1,x-3..1]

evenTo3 n = [x*2 | x <- [1..floor (n/2)]]
evenTo4 n = [x | x <- [1..n], x `mod` 2 == 0]

isPrime :: Int -> Bool
isPrime n = if null [x | x <- [2..ceiling (sqrt (n::Double))], n `mod` x == 0] then True else False
primesUpTo n = [x | x <- [1..n], isPrime x]
substring :: [Char] -> Int -> Int -> [Char]
substring str start end = [ str!!x | x <- [start..end] ]
