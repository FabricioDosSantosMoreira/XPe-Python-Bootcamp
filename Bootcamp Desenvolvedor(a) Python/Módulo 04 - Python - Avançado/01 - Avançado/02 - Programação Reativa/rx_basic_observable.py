import rx
import rx.operators as ops

# Cria um observable sequence a partir de uma lista
source = rx.from_iterable([1, 2, 3, 4, 5, 6])


# Aplica dois operadores ao observable source
# O operador 'map' subtrai 1 de cada item do observable
# O operador 'filter' filtra os números pares
disposable = source.pipe(
    ops.map(lambda i: i - 1),
    ops.filter(lambda i: i % 2 == 0),
).subscribe(
    # Define o que acontece quando um novo item é emitido
    on_next=lambda i: print("on_next: {}".format(i)),
    # Define o que acontece quando o observable é completado
    on_completed=lambda: print("on_completed"),
    # Define o que acontece quando ocorre um erro (não utilizado neste exemplo)
    on_error=lambda e: print("on_error: {}".format(e))
)


# Chama 'dispose()' no objeto disposable para encerrar a inscrição e liberar recursos associados
disposable.dispose()
