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
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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
backward_path = []


def populate_graph():
    if player.current_room.id not in traversal_graph:
        traversal_graph[player.current_room.id] = {}

        for exit in player.current_room.get_exits():
            traversal_graph[player.current_room.id][exit] = "?"


def grab_exits(room):
    unvisited_rooms = list()

    for key, value in traversal_graph[room].items():
        if value == "?":
            unvisited_rooms.append(key)

    return unvisited_rooms


def update_graph(exit):
    if player.current_room.id not in traversal_graph:
        traversal_graph[player.current_room.id] = {}
        for ex in player.current_room.get_exits():
            traversal_graph[player.current_room.id][ex] = "?"

    room_in_direction = player.current_room.get_room_in_direction(exit)
    traversal_graph[player.current_room.id][exit] = room_in_direction.id


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

# choose a random exit that I haven't gone before (has a "?")
# go there and update my graph both ways with my new information
# keep track of the path I just followed forwards ("north")
# and at the same time keep track of the steps backwards ("south")
# as I move to new rooms, keep updating my graph
# when I hit a dead end, back up a room
# check for rooms that I haven't gone before ("?")
# if no rooms left to explore, go back again
# when I arrive at a room with rooms to explore, go there and repeat

# create an empty stack and a visited set
# push the player's starting room to the stack
# while the stack has rooms in there...
# pop the current room
# check if room is not in visited
#### make sure to push room into stack before skipping any logic ####
# if it's not visited, check if it's in the graph already
# if it's not in the graph, initialize it and grab unvisited rooms
# check length of unvisited rooms
# if has unvisited rooms, move player, push room into stack, update path
# if I don't have unvisited rooms, add room to visited and
# skip the rest of logic
# if the room is visited
# check if I have reverse path available
# remove direction from reverse path, move the player back and update traversal path
# room 0 is going to be put in visited at the very last


def explore():
    stack = Stack()
    visited = set()
    stack.push(player.current_room.id)

    while stack.size() > 0:
        current_room = stack.pop()

        if current_room not in visited:
            if current_room not in traversal_graph:
                populate_graph()

            unvisited_rooms = grab_exits(current_room)

            if len(unvisited_rooms) > 0:
                next_room = unvisited_rooms[0]

                update_graph(next_room)

                player.travel(next_room)

                opposite_exit = grab_opposite_exit(next_room)

                update_graph(opposite_exit)

                stack.push(player.current_room.id)
                traversal_path.append(next_room)

                backward_path.append(opposite_exit)

            else:
                visited.add(current_room)
                stack.push(current_room)

        else:
            if len(backward_path) > 0:
                previous_room = backward_path.pop()

                player.travel(previous_room)

                traversal_path.append(previous_room)
                stack.push(player.current_room.id)


explore()

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
