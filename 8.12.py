def fazer_sanduiche(tamanho_pao, *ingredientes):
    print('Pedido feito com sucesso!!!')
    print('===== Informações do Pedido =====')
    print(f'Tamanho do pão: {tamanho_pao}')
    for ingrediente in ingredientes:
        print(ingrediente.tittle())



fazer_sanduiche('Grande', 'Carne', 'Feijão', 'Arroz', 'Alface')
