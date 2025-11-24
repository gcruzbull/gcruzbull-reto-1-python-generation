productos = [
    {"id": 1, "nombre": "Laptop Pro 14", "categoria": "Computo", "precio": 25000, "descuento": 0.10, "stock": 5},
    {"id": 2, "nombre": "Mouse Gamer X", "categoria": "Accesorios", "precio": 1200, "descuento": 0.15, "stock": 20},
    {"id": 3, "nombre": "Teclado Mecánico K1", "categoria": "Accesorios", "precio": 2200, "descuento": 0.05, "stock": 10},
    {"id": 4, "nombre": "Monitor 27'' 4K", "categoria": "Computo", "precio": 8000, "descuento": 0.20, "stock": 7},
    {"id": 5, "nombre": "Audífonos Bluetooth Z", "categoria": "Audio", "precio": 1500, "descuento": 0.0, "stock": 15},
]

ventas = [
    {"venta_id": 101, "producto_id": 1, "cantidad": 1, "cliente": "Ana"},
    {"venta_id": 102, "producto_id": 2, "cantidad": 2, "cliente": "Luis"},
    {"venta_id": 103, "producto_id": 4, "cantidad": 1, "cliente": "Sofía"},
    {"venta_id": 104, "producto_id": 2, "cantidad": 1, "cliente": "Carlos"},
    {"venta_id": 105, "producto_id": 5, "cantidad": 3, "cliente": "Ana"},
]

tienda_info = ("TechieStore", "Santiago", 2025)

# 🎯 Objetivos del Reto

"""Completa las siguientes tareas dentro de `reto_ecommerce.py`:"""

#------------------------------------------------------------------------

## ✅ 1. Mensaje de bienvenida

"""Usa la tupla `tienda_info` para imprimir:

    Bienvenido a TechieStore en Santiago (2025)"""

print(f"Bienvenido a {tienda_info[0]} en {tienda_info[1]} ({tienda_info[2]})")

#------------------------------------------------------------------------

## ✅ 2. Mostrar cuántos productos existen

"""Usa `len(productos)` para mostrar:

Total de productos: 5"""

total_productos = len(productos)
print(total_productos)

#------------------------------------------------------------------------

## ✅ 3. Precio final con descuento (sin loops)

"""Para cada producto (a mano, uno por uno), calcula:

precio_final = precio - (precio * descuento)

Y muestra:

    Laptop Pro 14 → $22500.0
    Mouse Gamer X → $1020.0
    ..."""

precio_laptop = productos[0]["precio"]
precio_mouse = productos[1]["precio"]
precio_teclado = productos[2]["precio"]
precio_monitor = productos[3]["precio"]
precio_audifonos = productos[4]["precio"]

descuento_laptop = productos[0]["descuento"]
descuento_mouse = productos[1]["descuento"]
descuento_teclado = productos[2]["descuento"]
descuento_monitor = productos[3]["descuento"]
descuento_audifonos = productos[4]["descuento"]

precio_final_laptop = precio_laptop - (precio_laptop*descuento_laptop)
precio_final_mouse = precio_mouse - (precio_mouse*descuento_mouse)
precio_final_teclado = precio_teclado - (precio_teclado*descuento_teclado)
precio_final_monitor = precio_monitor - (precio_monitor*descuento_monitor)
precio_final_audifonos = precio_audifonos - (precio_audifonos*descuento_audifonos)

print(f"""Laptop Pro 14 → ${precio_final_laptop},
       Mouse Gamer X → ${precio_final_mouse},
       Teclado Mecánico K1 → ${precio_final_teclado},
       Monitor 27'' 4K → ${precio_final_monitor},
       Audífonos Bluetooth Z → ${precio_audifonos}"""
       )
#------------------------------------------------------------------------

## ✅ 4. Total de cada venta (sin loops)

"""Para cada venta:

1.  Identifica el producto correspondiente\
2.  Usa el precio final calculado\
3.  Multiplica por la cantidad

Ejemplo para la venta 101:

    Venta 101: Ana compró 1 Laptop Pro 14 y pagó 22500.0"""

print(f"Venta {ventas[0]["venta_id"]}: Ana compró {ventas[0]["cantidad"]} {productos[0]["nombre"]} y pagó {precio_final_laptop}")
print(f"Venta {ventas[1]["venta_id"]}: Ana compró {ventas[1]["cantidad"]} {productos[1]["nombre"]} y pagó {precio_final_mouse}")
print(f"Venta {ventas[2]["venta_id"]}: Ana compró {ventas[2]["cantidad"]} {productos[3]["nombre"]} y pagó {precio_final_monitor}")
print(f"Venta {ventas[3]["venta_id"]}: Ana compró {ventas[3]["cantidad"]} {productos[1]["nombre"]} y pagó {precio_final_mouse}")
print(f"Venta {ventas[4]["venta_id"]}: Ana compró {ventas[4]["cantidad"]} {productos[4]["nombre"]} y pagó {precio_final_audifonos}")

#------------------------------------------------------------------------

## ✅ 5. Ingreso total de la tienda

"""Suma manualmente:

    ingreso_total = total_venta_101 + total_venta_102 + ...

Luego imprime:

    Ingreso total: XXXXX"""

cantidad_laptop = ventas[0]["cantidad"]
cantidad_mouse = ventas[1]["cantidad"] + ventas[3]["cantidad"]
cantidad_monitor = ventas[2]["cantidad"] 
cantidad_audifonos = ventas[4]["cantidad"]

ingreso_total = (precio_final_laptop*cantidad_laptop) + (precio_final_mouse*cantidad_mouse) + (precio_final_monitor*cantidad_monitor) + (precio_final_audifonos*cantidad_audifonos)
print("Ingreso Total: ", ingreso_total)
#------------------------------------------------------------------------

# 📄 Entrega Final

"""El archivo debe llamarse:

    reto_ecommerce.py

Y debe estar en la raíz de tu repositorio."""

#------------------------------------------------------------------------

# 🔵 🚀 Flujo completo de GitHub

### (Fork → Clone → Crear archivo → Commit → Push → Pull Request)

#-----------------------------------------------------------------------