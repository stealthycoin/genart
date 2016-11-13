def cached(fn):
    M = {}
    
    def wrapper(*args):
        key = str(list(map(str, args)))
        result = M.get(key, None)
        if result is None:
            result = fn(*args)
            M[key] = result
        return result
        
    return wrapper
