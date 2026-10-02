def spawn_next_level(current_level, enemy_list):
    # 1. Clear any remaining enemies from the previous level
    enemy_list.clear()

    # 2. Scale the grid size and speed based on the level number
    rows = 3 + (current_level // 2)  # Adds a new row every 2 levels
    cols = 8                         # Number of enemies per row
    enemy_speed = 2 + (current_level * 0.5)  # Increases speed each level

    # 3. Create the new enemy grid positions
    for row in range(rows):
        for col in range(cols):
            # Adjust 60 and 50 to change horizontal and vertical spacing
            x_position = 50 + (col * 60)
            y_position = 50 + (row * 50)

            # Creates an enemy dictionary holding its hit-box and speed
            new_enemy = {
                "rect": pygame.Rect(x_position, y_position, 40, 30),
                "speed": enemy_speed
            }
            enemy_list.append(new_enemy)

    return enemy_speed


# --- HOW TO TRIGGER IT IN YOUR MAIN GAME LOOP ---
# (Uncomment and put this inside your while loop where you check for updates)
#
# if len(enemy_list) == 0:
#     game_level += 1
#     current_speed = spawn_next_level(game_level, enemy_list)
