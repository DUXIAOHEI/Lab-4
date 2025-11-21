from itertools import combinations

items = [
    ('r','rifle', 3, 25),
    ('p','pistol',2,15),
    ('a','ammo',  2,15),
    ('m','medkit',2,20),
    ('i','inhaler',1,5),  
    ('k','knife',1,15),
    ('x','axe',3,20),
    ('t','talisman',1,25),
    ('f','flask',1,15),
    ('d','antidot',1,10),  
    ('s','supplies',2,20),
    ('c','crossbow',2,20)
]

CAP = 9  
BASE = 15  
MUST_HAVE = 'd'  

total_all = sum(it[3] for it in items)

print(f"总物品数: {len(items)}")
print(f"总可能组合数: {2**len(items)}")
print(f"所有物品总价值: {total_all}")

mandatory_idx = None
for i, item in enumerate(items):
    if item[0] == MUST_HAVE:
        mandatory_idx = i
        break

best = ([], float('-inf'))
n = len(items)

for r in range(n+1):
    for combo in combinations(range(n), r):
        if mandatory_idx not in combo:
            continue
            
        size = sum(items[i][2] for i in combo)
        if size > CAP: 
            continue
        val = sum(items[i][3] for i in combo)
        
        not_taken = total_all - val
        final = BASE + val - not_taken
        
        if final > best[1]:
            best = (list(combo), final)

chosen, final_score = best
sum_taken = sum(items[i][3] for i in chosen)    

print(f"\n最优组合:")
cells = []
for i in chosen:
    print(f"  {items[i][1]} ({items[i][0]}), 大小: {items[i][2]}, 价值: {items[i][3]}")
    cells += [items[i][0]] * items[i][2]

cells += ['.'] * (CAP - len(cells))

rows = [cells[:3], cells[3:6], cells[6:9]]

print(f"\n背包布局 (3x3):")
for r in rows:
    print(' '.join(f'[{x}]' for x in r))

print(f"\n统计信息:")
print(f"已选物品总价值: {sum_taken}")
print(f"未选物品总价值: {total_all - sum_taken}")
print(f"最终生存点数: {final_score}")