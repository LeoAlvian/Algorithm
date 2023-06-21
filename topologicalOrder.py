from collections import deque

dress_dep = {
    'shirt': ['watch','jacket'],
    'underpants': ['pants', 'sock'],
    'pants': ['shirt', 'shoes'],
    'sock': ['shoes','pants'],
    'jacket': [],
    'watch': ['jacket'],
    'shoes': []
}

def top(d):
    dep = {el:0 for el in d}
    for item in d:
        for el in d[item]:
            dep[el] += 1
    
    q = deque(el for el in dep if dep[el] == 0)
    order = []

    while q:
        item = q.popleft()
        order.append(item)
        for el in d[item]:
            dep[el] -= 1
            if dep[el] == 0:
                q.append(el)
                
    return order

print(top(dress_dep))