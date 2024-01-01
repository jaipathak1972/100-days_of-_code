import prettytable

table = prettytable.PrettyTable()
table.add_column("Pokemon" , ["Chespin" , "Quilladin" ,"Froakie"])
table.add_column("type" ,["Grass", "Grass", "water"]  )
table.align = "l"

print(table)