def motif(s, t):
    results = []
    for i in range(len(s) - len(t)):
        if s[i:i+len(t)] == t:
            results.append(i + 1)

    return results
q=str(motif(s, t))
q.replace(',', '') #Для внесения ответа в розалинду
