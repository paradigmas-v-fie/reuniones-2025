"""
Patrón Adapter
Descripción: Compatibilidad entre interfaces incompatibles
"""

# Sistema antiguo con interfaz incompatible
class SistemaPagoAntiguo:
    """
    Sistema de pago legacy que usa una interfaz antigua.
    Opera con montos en centavos y tiene nombres de métodos diferentes.
    """

    def __init__(self):
        self.transacciones = []

    def realizar_pago_legacy(self, monto_centavos):
        self.transacciones.append(monto_centavos)
        return f"Pago legacy procesado: {monto_centavos} centavos"

    def obtener_balance_legacy(self):
        return sum(self.transacciones)

# Interfaz nueva que esperan los sistemas actuales
class SistemaPagoNuevo:
    """
    Interfaz moderna que esperan los sistemas actuales.
    Opera con montos en dólares y tiene nombres de métodos actualizados.
    """

    def procesar_pago(self, monto_dolares):
        pass

    def obtener_balance(self):
        pass

# Adapter que hace compatible el sistema antiguo con la interfaz nueva
class AdapterPago(SistemaPagoNuevo):
    """
    Adapter que permite usar el sistema de pago antiguo
    con la interfaz nueva que esperan los sistemas modernos.
    """

    def __init__(self, sistema_antiguo):
        self.sistema_antiguo = sistema_antiguo

    def procesar_pago(self, monto_dolares):
        # Convertir de pesos a centavos para el sistema antiguo
        monto_centavos = int(monto_dolares * 100)

        # Llamar al método del sistema antiguo
        resultado_legacy = self.sistema_antiguo.realizar_pago_legacy(monto_centavos)

        # Adaptar la respuesta para que sea consistente con la interfaz nueva
        return f"Pago adaptado: ${monto_dolares:.2f} procesado exitosamente"

    def obtener_balance(self):
        # Obtener balance en centavos del sistema antiguo
        balance_centavos = self.sistema_antiguo.obtener_balance_legacy()

        # Convertir de centavos a dólares para la interfaz nueva
        return balance_centavos / 100.0

# Sistema moderno que espera la interfaz nueva
class TiendaOnline:
    """
    Sistema moderno que espera trabajar con la interfaz nueva de pagos.
    No conoce los detalles del sistema antiguo.
    """

    def __init__(self, sistema_pago):
        self.sistema_pago = sistema_pago
        self.productos = {
            "laptop": 1500.00,
            "mouse": 25.50,
            "teclado": 75.00,
            "monitor": 300.00
        }

    def realizar_compra(self, producto):
        if producto in self.productos:
            precio = self.productos[producto]
            resultado = self.sistema_pago.procesar_pago(precio)
            return f"Compra exitosa: {producto} - {resultado}"
        else:
            return f"Producto '{producto}' no encontrado"

    def mostrar_balance_total(self):
        balance = self.sistema_pago.obtener_balance()
        return f"Balance total de transacciones: ${balance:.2f}"

# Ejemplo de uso
if __name__ == "__main__":
    print("=== Patrón Adapter: Integrando sistema de pago legacy ===\n")

    # Crear una instancia del sistema antiguo
    sistema_legacy = SistemaPagoAntiguo()
    print("1. Sistema legacy creado")

    # Crear el adapter para hacer compatible el sistema antiguo
    adapter = AdapterPago(sistema_legacy)
    print("2. Adapter creado para compatibilidad")

    # Crear la tienda online que usa la interfaz moderna
    tienda = TiendaOnline(adapter)
    print("3. Tienda online configurada con adapter\n")

    # Realizar compras usando la interfaz moderna
    print("=== Realizando compras ===")
    productos_a_comprar = ["laptop", "mouse", "teclado", "producto_inexistente"]

    for producto in productos_a_comprar:
        resultado = tienda.realizar_compra(producto)
        print(f"• {resultado}")

    print(f"\n• {tienda.mostrar_balance_total()}")

    # Verificar que el sistema legacy también registró las transacciones
    print(f"\n=== Verificación del sistema legacy ===")
    print(f"• Transacciones en el sistema legacy: {sistema_legacy.transacciones}")
    print(f"• Balance legacy en centavos: {sistema_legacy.obtener_balance_legacy()}")

    # Demostrar uso directo del sistema legacy (sin adapter)
    print(f"\n=== Uso directo del sistema legacy ===")
    pago_directo = sistema_legacy.realizar_pago_legacy(5000)  # 50 dólares en centavos
    print(f"• {pago_directo}")
    print(f"• Nuevo balance total: ${adapter.obtener_balance():.2f}")
