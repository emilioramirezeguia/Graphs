# explore algorithm attempts

def explore_1():
    stack = Stack()
    stack.push(player.current_room.id)

    while stack.size() > 0:
        current_room = stack.pop()
        print("=======> Starting Graph: ", traversal_graph)
        print("======> Current Room: ", current_room)
        print("=====> Visited: ", visited)
        if current_room not in visited:
            visited.add(current_room)
            random_exit = pick_random()
            print("===> Random Exit: ", random_exit)
            exit_room = traversal_graph[player.current_room.id][random_exit]
            print("==> Exit Room: ", exit_room)
            if exit_room == "?":
                update_graph(random_exit)
                player.travel(random_exit)
                traversal_path.append(random_exit)
                opposite_direction = grab_opposite_exit(random_exit)
                backward_path.append(opposite_direction)
                populate_graph()
                update_graph(opposite_direction)
                stack.push(player.current_room.id)
            else:
                while "?" in traversal_graph[player.current_room.id].values():
                    random_exit = pick_random()
            backward_exit = backward_path[-1]
            player.travel(backward_exit)


def explore_2():
    stack = Stack()
    # start exploring from the player's current room
    stack.push([player.current_room.id])

    while stack.size() > 0:
        print("=======> Starting Graph: ", traversal_graph)
        path_as_room_ids = stack.pop()
        current_room = path_as_room_ids[-1]
        print("======> Current Room: ", current_room)
        if current_room not in visited:
            visited.add(current_room)
            print("=====> Visited: ", visited)
            print("====> Path as Room IDs: ", path_as_room_ids)
            # choose a random exit from that room
            random_exit = pick_random()
            room_in_direction = player.current_room.get_room_in_direction(
                random_exit)
            print("===> Random Exit: ", random_exit)
            print("==> Room at that exit: ", room_in_direction.name)
            print("=> Room unexplored(?): ",
                  traversal_graph[player.current_room.id][random_exit])
            while "?" in traversal_graph[player.current_room.id].values():
                if traversal_graph[player.current_room.id][random_exit] == "?":
                    update_graph(random_exit)
                    player.travel(random_exit)
                    traversal_path.append(random_exit)
                    new_path_as_room_ids = path_as_room_ids + \
                        [player.current_room.id]
                    opposite_direction = grab_opposite_exit(random_exit)
                    backward_path.append(opposite_direction)
                    populate_graph()
                    update_graph(opposite_direction)
                    stack.push(new_path_as_room_ids)
                    print("=> Updated Graph", traversal_graph)
                else:
                    random_exit = pick_random()
                    # player.travel(random_exit)
                    # traversal_path.pop()
                    # stack.push(new_path_as_room_ids)
            backward_exit = backward_path[-1]
            player.travel(backward_exit)
