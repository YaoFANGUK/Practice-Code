merge :: Ord a => [a] -> [a] -> [a]
merge xs [] = xs
merge [] ys = ys
merge xxs@(x : xs) yys@(y : ys) | x == y = x : merge xs ys
                                | x < y  = x : merge xs yys
                                | x > y  = y : merge xxs ys
ham :: [Integer]
ham = 1 : merge (map (*2) ham) (merge (map (*3) ham) (map (*5) ham))