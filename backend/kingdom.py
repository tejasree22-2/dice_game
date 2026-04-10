import random

def roll(n=1):
    return [random.randint(1, 6) for _ in range(n)]

def create_kingdom(name):
    return {
        "name": name,
        "hp": 100,
        "soldiers": 10,
        "shields": 0,
        "territories": 5
    }

def attack(attacker, defender):
    dice = roll(2)
    damage = sum(dice) * attacker["soldiers"] // 10
    actual_damage = max(0, damage - defender["shields"])
    defender["hp"] -= actual_damage
    defender["shields"] = 0
    if defender["hp"] < 0:
        defender["hp"] = 0
    if defender["hp"] <= 20 * defender["territories"] and defender["territories"] > 0:
        defender["territories"] -= 1
    return {"dice": dice, "damage": actual_damage, "raw_damage": damage}

def defend(kingdom):
    dice = roll(1)
    kingdom["shields"] += dice[0] * 2
    return {"dice": dice, "shields": kingdom["shields"]}

def recruit(kingdom):
    dice = roll(1)
    kingdom["soldiers"] += dice[0]
    return {"dice": dice, "soldiers": kingdom["soldiers"]}

def computer_action(computer, player):
    if computer["hp"] < 40:
        return "defend", defend(computer)
    elif computer["soldiers"] < 8:
        return "recruit", recruit(computer)
    else:
        return "attack", attack(computer, player)

def check_winner(k1, k2):
    if k1["territories"] == 0 or k1["hp"] <= 0:
        return k2["name"]
    if k2["territories"] == 0 or k2["hp"] <= 0:
        return k1["name"]
    return None