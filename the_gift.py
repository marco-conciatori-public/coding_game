import sys
import math

oods_budgets = []
max_budget = 0
solution = []

n = int(input())
cost = int(input())
for i in range(n):
    b = int(input())
    oods_budgets.append(b)
    max_budget += b
print("n ", n, file=sys.stderr)
print("cost ", cost, file=sys.stderr)
print("max_budget ", max_budget, file=sys.stderr)

if max_budget < cost:
    solution = ["IMPOSSIBLE"]
else:
    while cost > 0:
        mean_cost, reminder = divmod(cost, len(oods_budgets))
        print("mean_cost ", mean_cost, file=sys.stderr)
        print("reminder ", reminder, file=sys.stderr)

        oods_to_remove = []
        for ood in oods_budgets:
            if ood <= mean_cost:
                cost -= ood
                solution.append(ood)
                oods_to_remove.append(ood)

        if len(oods_to_remove) == 0:
            for i in range(len(oods_budgets)):
                ood = oods_budgets[i]
                if reminder > 0 and ood > mean_cost:
                    reminder -= 1
                    solution.append(mean_cost + 1)
                else:
                    solution.append(mean_cost)
            break

        for ood in oods_to_remove:
            oods_budgets.remove(ood)

    solution.sort()

for elem in solution:
    print(elem)
