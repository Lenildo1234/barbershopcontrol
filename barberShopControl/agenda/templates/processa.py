import cgi

res_formulario = cgi.FieldStorage() 

servico = []
for i in range(2):
    if res_formulario.getvalue(str(i)):
        servico.append(res_formulario.getvalue(str(i)))
        
print(servico)
        