def formatted_numbers():
    
    fin_table = []
    
    title = "|{:^10}|{:^10}|{:^10}|".format("decimal","hex","binary")
    
    fin_table.append(title)
    
    for val in range(16):
        str = "|{:<10d}|{:^10x}|{:>10b}|".format(val,val,val)
        fin_table.append(str)
    
    for r in fin_table:
        print(r)
    return (fin_table)

print(formatted_numbers()) 