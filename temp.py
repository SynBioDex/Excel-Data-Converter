import random
sbol_ids = ["1", "2", "3"]

hash_map = {}

def get_flapjack(id):
    return random.random()

for id in sbol_ids:
    flapjack_id = get_flapjack(id)
    hash_map[id] = flapjack_id
    print(hash_map)
