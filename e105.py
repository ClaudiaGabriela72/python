def notas(* nots, sitacao=False):
    """
    -> Para analisar notas e situaçaoes de alunos
    :param nots: sao as notas passadas
    :param sitacao:para docstapy
    :return:dicionario
    """
    dic = dict()
    dic['notas'] = nots
    dic['total'] = len(nots)
    dic['maior'] = max(nots)
    dic['menor'] = min(nots)
    dic['media'] = sum(nots) / len(nots)
    print(dic)
    if sitacao == True:
        print(help())


notas(2, 6, 8, True)
help(notas())
