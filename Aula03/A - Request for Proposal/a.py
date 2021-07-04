rfp = 1
best_proposals = []

while True:
    n, p = list(map(int, input().split()))

    if n == 0 and p == 0:
        break

    requirements_names = [input() for _ in range(n)]

    proposals = []
    for _ in range(p):
        name = input()

        d, r = input().split()
        d = float(d)
        r = int(r)

        met_req_names = [input() for _ in range(r)]

        proposal = { 
            'name': name, 
            'price': d, 
            'n_met_req': r, 
            'met_req_names': met_req_names
        }

        proposals.append(proposal)

    greater_met_req = max([p['n_met_req'] for p in proposals]) # Maior número de requisitos atendidos dentre as propostas
    greater_met_req_proposals = list(filter(lambda p: p['n_met_req'] == greater_met_req, proposals)) # Propostas que atendem mais requisitos

    lowest_price = min([p['price'] for p in greater_met_req_proposals]) # Menor preço dentre as propostas
    lowest_price_proposals = list(filter(lambda p: p['price'] == lowest_price, greater_met_req_proposals)) # Propostas com o menor preço

    best_proposal = lowest_price_proposals[0]
    best_proposals.append(best_proposal['name'])

    rfp += 1

best_proposals = ['RFP #{}\n{}'.format(i, name) for i, name in enumerate(best_proposals, start = 1)]

print(*best_proposals, sep = '\n\n')
