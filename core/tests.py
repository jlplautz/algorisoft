# Para habilitar os teste inserir o import wsgi
# from src.wsgi import *
# from core.models import *

# lista os registro de uma tabela
# query = Type.objects.all()
# print(query)
# # <QuerySet [<Type: Gerente>, <Type: Balconista>, <Type: Diretor>]>

# Para inserir um registro na tabela
# t = Type()
# t.name = 'Presidente'
# t.save()

# query = Type.objects.all()
# print(query)
# <QuerySet [<Type: Gerente>, <Type: Balconista>, <Type: Diretor>, <Type: Presidente>]>

# editar um registro com update
# t = Type.objects.get(id=1)
# t.name = 'Gerente-Chefe'
# t.save
# print(t.name)

# # com fazer um delete
# t = Type.objects.get(id=1)
# t.delete()
# print(t.name)

# com otimizar os erro para visyualizar no console
# try:
#     t = Type.objects.get(id=1)
#     t.delete()
# except Exception as e:
#     print(e)
# -> Type matching query does not exist.

# Usar o metodo filter
# print(Type.objects.filter(name__contains='pre'))
# print(Type.objects.filter(name__icontains='diretor'))
# print(Type.objects.filter(name__startswith='a'))
# print(Type.objects.filter(name__endswith='a'))
# print(Type.objects.filter(name__contains='Auxiliar').query)
# -><QuerySet [<Type: Diretor>]>
# -> <QuerySet [<Type: Auxiliar>]>
# -> <QuerySet [<Type: Balconista>]>
# -> SELECT "core_type"."id", "core_type"."name" FROM "core_type" WHERE "core_type"."name" LIKE %Auxiliar% ESCAPE '\'
#    ORDER BY "core_type"."id" ASC

# print(Type.objects.filter(name__endswith='a').exclude(id=5))
# <QuerySet [<Type: Balconista>]>

# for i in Type.objects.filter(name__endswith='e'):
#     print(i.name)
#
#  para consultar registros entre tabelas
# obj = Employee.objects.filter(type_id=1)

# query = Category.objects.all()
# print(query)

# para popular um tabela
# data = ['Leche y derivados', 'Carnes, pescados y huevos', 'Patatas, legumbres, frutos secos',
#         'Verduras y Hortalizas', 'Frutas', 'Cereales y derivados, azúcar y dulces',
#         'Grasas, aceite y mantequilla']
#
# for i in data:
#     cat = Category(name=i)
#     cat.save()
#     print('Guardado registro N°{}'.format(cat.id))
