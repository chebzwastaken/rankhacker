
def condit(n)
    if n % 2 == 0 && n >= 2 && n <= 5
    puts "Not Wierd"
    elsif n % 2 == 0 && n > 20
        puts "Not Wierd"
    else
        puts "Wierd"
    end
end

condit(4)