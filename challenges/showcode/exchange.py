class Solution: 
    def calculate_exchange_rate(exchange_rates, from_currency, to_currency):
        exchanges = []
        values = []
        for i in exchange_rates: 
            if all(x in i for x in [from_currency, to_currency]):
                exchangerate = i

                for i in exchangerate:
                    if i.isdigit():
                        values.append(i)
                
                value = float(''.join(values)) /10000

                if not(from_currency == exchangerate[:3] and to_currency == exchangerate[-3:]):
                    return round(value, 4)
                else: 
                    return round(1/value, 4)
                
            elif from_currency or to_currency in i:
                exchanges.append(i)
        s_values = []
        for exchange in exchanges:
            for i in exchange:
                if i.isdigit():
                    s_values.append(i)
            values.append(float(''.join(s_values))/10000)
            s_values = []

        index = 1 / values[0]
        for i in range(1, len(values)):
            index = index * (1 / values[i])
        
        return round(index, 4)

       


            



print(Solution.calculate_exchange_rate([ "FOO15.0000/BAR", "BAR0.1250/BIT" ], "BAR", "FOO"))
print(Solution.calculate_exchange_rate([ "FOO15.0000/BAR", "BAR0.1250/BIT" ], "FOO", "BIT"))