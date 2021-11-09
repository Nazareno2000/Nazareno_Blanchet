from heap import HeapMax

h=HeapMax()


h.arribo('empleado',1)

h.arribo('empleado',1)

h.arribo('empleado',1)

print(h.atencion())

h.arribo('staff',2)
h.arribo('staff',2)
h.arribo('gerente',3)
h.arribo('gerente',3)

print(h.atencion())
print(h.atencion())

h.arribo('empleado',1)
h.arribo('empleado',1)
h.arribo('gerente',3)

while(not h.vacio()):
      print(h.atencion())