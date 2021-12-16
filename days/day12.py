def all_paths(edge_map, adv=True, out="start", path=["start"],
 seen=set(["start"]), revisit=False):
    if out == "end": return [[p for p in path]]
    nexts, res, flag = edge_map[out], [], False
    for v in nexts:
        if v == "start" or (v in seen and (not adv or revisit)): continue
        if v in seen and adv and not revisit:
            flag, revisit = True, True
        if v.lower() == v: seen.add(v)
        path.append(v)
        res.extend(all_paths(edge_map, adv, v, path, seen, revisit))
        path.remove(v)
        if not flag and v in seen: seen.remove(v)
        if flag: revisit, flag = False, False
    return res

if __name__ == "__main__":
    edges = []
    while True:
        i = input()
        if i == '': break
        edges.append(i.split("-"))
    edge_map = {}
    for edge in edges:
        if edge[0] in edge_map: edge_map[edge[0]].append(edge[1])
        else: edge_map[edge[0]] = [edge[1]]
        if edge[1] in edge_map: edge_map[edge[1]].append(edge[0])
        else: edge_map[edge[1]] = [edge[0]]
    print(len(all_paths(edge_map, adv=True)))