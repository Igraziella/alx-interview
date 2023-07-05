#!/usr/bin/python3
"""Method to unlock boxes"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened"""
    opened_boxes = [False] * len(boxes)
    opened_boxes[0] = True

    queue = [0]

    while queue:
        current_box = queue.pop(0)
        keys = boxes[current_box]

        for key in keys:
            if not opened_boxes[key]:
                opened_boxes[key] = True
                queue.append(key)

    return all(opened_boxes)
