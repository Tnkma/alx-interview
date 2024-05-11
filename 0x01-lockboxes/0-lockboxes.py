#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ checks if the key can open the box and return false if it does not"""
    n = len(boxes)
    seen_box = set([0])
    unseen_box = set(boxes[0]).difference(set([0]))
    while len(unseen_box) > 0:
        boxIdx = unseen_box.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_box:
            unseen_box = unseen_box.union(boxes[boxIdx])
            seen_box.add(boxIdx)
    return n == len(seen_box)
