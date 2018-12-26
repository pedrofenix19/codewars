findNb :: Integer -> Integer
findNb m = findFloors 1 m

findFloors :: Integer -> Integer -> Integer
findFloors n 0 = n-1
findFloors n m 
  | m >= n^3 = findFloors (n+1) (m-n^3)
  | otherwise = -1
     
--findNb :: Integer -> Integer
--findNb m =
--  let n = (-1 + sqrt (1 + 8 * (sqrt (fromIntegral m))))/2
--      isValidN n x = fromIntegral (floor n) == n && 
--  in if isValidN n then floor n else -1