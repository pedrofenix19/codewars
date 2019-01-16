main :: IO()
main = putStrLn (greet "World")

greeting = "Hola"
greet who = greeting ++ ", " ++ who
