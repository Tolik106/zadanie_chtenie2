







# result_12 = file2.read()
# print(result_12)
# result_13 = file3.read()
# print(result_13)
        
    #res = [f'1.txt\n, {result_1} \n, {"line"}\n']
    #with open('resultat.txt','w') as file:
        #file.writelines(res)


file_1 = open('1.txt', 'rt',encoding='utf-8')
file_2 = open('2.txt', 'rt',encoding='utf-8')
file_3 = open('3.txt', 'rt',encoding='utf-8')
   
result_1 = len(file_1.readlines())
print(f' строк в 1.txt {result_1}')
    

result_2 = len(file_2.readlines())
print(f' строк в 2.txt {result_2}')

result_3 = len(file_3.readlines())
print(f' Строк в 3.txt {result_3}')



with open('1.txt', 'rt',encoding='utf-8') as file1,open('2.txt', 'rt',encoding='utf-8') as file2,open('3.txt', 'rt',encoding='utf-8') as file3, open('rezultat.txt', 'w', encoding = 'utf-8') as f:
       
    
    for line2 in file2:
        f.writelines(f'{file2.name}\n{len(file_2.readlines())+1}\n')
        result_12 = []   
        result_12 = line2 
        
        for num_line2, lines2 in enumerate(file2,1):
            otvet2 = f'файл 2, строка, {num_line2},   {lines2}'
            print(otvet2)       
            f.writelines(otvet2)
        

    for line in file1:
        f.writelines(f'\n {file1.name}\n{len(file_1.readlines())+1}\n')
        result_11 = []   
        result_11 = line 
        for num_line, lines in enumerate(file1,1):
            otvet = f'файл 1, строка, {num_line},   {lines}'
            print(otvet)
            f.writelines(otvet)


    for line in file3:
        f.writelines(f'\n {file3.name}\n{len(file_3.readlines())+1}\n')
        result_13 = []   
        result_13 = line 
        for num_line, lines in enumerate(file3,1):
            otvet = f'файл 3, строка, {num_line},   {lines}'
            print(otvet)
            f.writelines(otvet)

       
# res = "1.txt"
# res2 = '2.txt'
# res3 = '3.txt'
    
# with open('resultat.txt','w+', encoding = 'utf-8') as file_redact:
#     file_redact.writelines(f'{res}\n, {result_1}\n,{result_11}')
#     file_redact.writelines(f'{res2}\n, {result_2}\n,{result_12}')
#     file_redact.writelines(f'{res3}\n, {result_3}\n,{result_13}')

file_1.close()
file_2.close()
file_3.close()
file_1.close()
file_2.close()
file_3.close()
   





# print(result.sort())
