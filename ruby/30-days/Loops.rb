def multiples(n)
    for i in 1..10 do
        x = n * i 
        puts "%d x %d = %d" % [n, i, x]
        i += 1
    end
end
multiples(3)

