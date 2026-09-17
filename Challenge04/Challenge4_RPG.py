def calculate_damage(attacker_power, multiplier=1):
    #calcula el daño realizado
    return attacker_power * multiplier

def apply_healing(current_hp, heal_amount):
    #aplica curación sin exceder 100 HP
    return min(current_hp + heal_amount, 100)

def limit_health(hp):
    #mantiene la vida entre 0 y 100
    return max(0, min(hp, 100))

def check_battle_status(player_hp, monster_hp):
    #determina el estado de la batalla
    if player_hp <= 0 and monster_hp <= 0:
        return "MUTUAL DEFEAT"
    elif monster_hp <= 0:
        return "VICTORY"
    elif player_hp <= 0:
        return "DEFEAT"
    else:
        return "Battle Continues"

def turn_resolution(player_hp, player_mana, player_atk, monster_hp, monster_atk, choice):
    choice = choice.lower()

    if choice == "attack":
        damage = calculate_damage(player_atk)
        monster_hp -= damage
        player_hp -= monster_atk

    elif choice == "magic":
        if player_mana >= 15:
            damage = calculate_damage(player_atk, 2.5)
            monster_hp -= damage
            player_mana -= 15
            player_hp -= monster_atk / 2
        else:
            print("Not enough mana! Spell failed.")
            player_hp -= monster_atk

    elif choice == "heal":
        player_hp = apply_healing(player_hp, 30)
        player_hp -= monster_atk / 2

    else:
        print("Invalid action!")
        return

    player_hp = limit_health(player_hp)
    monster_hp = limit_health(monster_hp)

    status = check_battle_status(player_hp, monster_hp)

    print("\n--- End of Turn ---")
    print(f"Player HP: {player_hp}")
    print(f"Player Mana: {player_mana}")
    print(f"Monster HP: {monster_hp}")
    print(f"Status: {status}")


def main():
    print("=== Dungeon Encounter ===")

    player_hp = float(input("Player HP (0-100): "))
    player_mana = float(input("Player Mana (0-50): "))
    player_atk = float(input("Player Attack Power: "))

    monster_hp = float(input("Monster HP (0-100): "))
    monster_atk = float(input("Monster Attack Power: "))

    choice = input("Choose action (attack, magic, heal): ")

    turn_resolution(player_hp, player_mana, player_atk, monster_hp, monster_atk, choice)

main()
