from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from graph import Vertex, Graph
from util import Stack, Queue


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
traversal_graph = {}

# grab the exits from the player's starting room and populate my initial graph


def populate_graph():
    traversal_graph[player.current_room.id] = {}

    for exit in player.current_room.get_exits():
        traversal_graph[player.current_room.id][exit] = "?"


def update_graph(exit):
    if player.current_room.id not in traversal_graph:
        traversal_graph[player.current_room.id] = {}

        for ex in player.current_room.get_exits():
            if ex not in traversal_graph[player.current_room.id]:
                traversal_graph[player.current_room.id][ex] = "?"
    else:
        room_in_direction = player.current_room.get_room_in_direction(exit)
        traversal_graph[player.current_room.id][exit] = room_in_direction.id

# pick a random unexplored direction from the player's current room


def grab_opposite_exit(exit):
    if exit == "n":
        exit = "s"
        return exit
    elif exit == "s":
        exit = "n"
        return exit
    elif exit == "e":
        exit = "w"
        return exit
    elif exit == "w":
        exit = "e"
        return exit
    else:
        print("INVALID EXIT")
        return


def pick_random():
    room_exits = player.current_room.get_exits()
    number_exits = len(room_exits)
    random_exit = room_exits[random.randint(0, number_exits - 1)]

    return random_exit

# create an empty stack and a visited set
# push the player's starting room to the stack
# while the stack has rooms in there...
# pop the current room
# choose a random exit that I haven't gone before
# go there and update my graph with my new information
# keep track of the path I just followed ("north")


visited = set()


def explore():
    stack = Stack()
    # start exploring from the player's current room
    stack.push([player.current_room.id])

    while stack.size() > 0:
        path_as_room_ids = stack.pop()
        current_room = path_as_room_ids[-1]
        if current_room not in visited:
            visited.add(current_room)
            print("Visited: ", visited)
            print("Path as Room IDs: ", path_as_room_ids)
            # choose a random exit from that room
            random_exit = pick_random()
            if traversal_graph[player.current_room.id][random_exit] == "?":
                update_graph(random_exit)
                player.travel(random_exit)
                traversal_path.append(random_exit)
                new_path_as_room_ids = path_as_room_ids + \
                    [player.current_room.id]
                opposite_direction = grab_opposite_exit(random_exit)
                populate_graph()
                update_graph(opposite_direction)
                stack.push(new_path_as_room_ids)


populate_graph()
print("Starting Graph: ", traversal_graph)
explore()
print("Updated Graph: ", traversal_graph)
print(f"{len(visited)} out of {len(room_graph)} rooms visited.")

### DO NOT WRITE ANYTHING BELOW THIS LINE ###


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
