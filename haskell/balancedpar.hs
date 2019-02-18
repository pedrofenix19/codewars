-- getgetBalancedParens stringparcial -> n -> abiertos -> cerrados -> listastringbalanceados
getBalancedParens :: [x] -> Integer -> Integer -> Integer -> [x]
getBalancedParens [] 0 0 0 = []
getBalancedParens [x] n a c 
    | a > c = 


balancedParens :: Int -> [String]
balancedParens n = getBalancedParens [] n 0 0