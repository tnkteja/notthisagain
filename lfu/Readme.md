Any sane mind would do it using a hashmap for the cache. The other structure for holding the frequencies and returning me the frequencies was using a heapq but updating the heapq was bit of a problem. here the issue is maintaining the key with their frequencies and accessing the lfu immedietelty. You can also maintain a dashboard of the keys in the order of their frequencies. But when all the frequencies are same the swap has to happen on the last element and the finding it would be O(n), but it does not always happen, for aput operation it might take O(n) for swapping but we can use binary search for the increamented item and get the location. And maintain another dictionary to get the positions of the updated dictionary.  To reduce the space complexity we can reduce the use of two maps to one map.