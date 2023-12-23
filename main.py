def coins_div(money_bag):
  sum = 0  # переменная для суммы
  max_el = max(money_bag)
  for i in range(len(money_bag)):
    sum += money_bag[i]
  if sum % 3 != 0 or max_el > sum / 3 or len(money_bag) < 3:
    return False
  money_bag.sort(reverse=True)
  m = sum / 3
  ss = 0
  n = 0
  for _ in range(len(money_bag)):
    lst = []
    for i in range(len(money_bag)):
      if money_bag[i] == m:
        n += 1
        money_bag[i] = 0
        continue
      elif money_bag[i] != 0:
        ss = money_bag[i]
        lst.append(money_bag[i])
      for j in range(i + 1, len(money_bag)):
        if ss + money_bag[j] <= m and money_bag[j] != 0:
          lst.append(money_bag[j])
          ss += money_bag[j]
          if ss == m:
            n += 1
            for x in range(len(lst)):
              if lst[x] in money_bag:
                money_bag[money_bag.index(lst[x])] = 0
            lst = []
      lst = []
  return (n >= 3)
