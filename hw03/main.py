"""
HW03 — Rumor Loop Detector (Cycle in Undirected Graph)

Implement:
- has_cycle(graph)
- find_cycle(graph)
"""

def has_cycle(graph):
    """Return True if the undirected graph has any cycle; else False."""
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph.get(node, []):
            # Self-loop is a cycle
            if neighbor == node:
                return True
            # If not visited, explore it
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            # If visited and not the parent, we found a cycle
            elif neighbor != parent:
                return True
        return False
    
    # Check all connected components
    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False

def find_cycle(graph):
    """Return a list of nodes forming a simple cycle where first == last.
    If no cycle, return None.

    Note:
    - Use DFS and a parent map.
    - Self-loop counts: return [u, u].
    """
    visited = set()
    parent_map = {}
    
    def dfs(node, parent):
        visited.add(node)
        parent_map[node] = parent
        
        for neighbor in graph.get(node, []):
            # Self-loop is a cycle
            if neighbor == node:
                return [node, node]
            
            # If not visited, explore it
            if neighbor not in visited:
                result = dfs(neighbor, node)
                if result is not None:
                    return result
            # If visited and not the parent, we found a cycle
            elif neighbor != parent:
                # Reconstruct path from cycle_end back to cycle_start
                path = []
                current = node
                while current != neighbor:
                    path.append(current)
                    current = parent_map[current]
                path.append(neighbor)
                # Close the cycle so first == last (use starting node)
                path.append(path[0])
                return path
        
        return None
    
    # Check all connected components
    for node in graph:
        if node not in visited:
            result = dfs(node, None)
            if result is not None:
                return result
    
    return None
