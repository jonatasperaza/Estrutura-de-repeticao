from decimal import Decimal

x: Decimal = Decimal('1.0')
while (x <= Decimal('5')):
    primeira_parte = Decimal('3') + Decimal('2') * x + Decimal('6')*x**Decimal('2')
    sgunda_parte = Decimal('1') + Decimal('9')*x +Decimal('16')*x**Decimal('2')
    completo = primeira_parte / sgunda_parte
    print(f"Resultado para x={x}: {completo}")
    x += Decimal('0.01')
