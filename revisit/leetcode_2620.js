var createCounter = function(n) {
    
    // n is our initial number
    // we also need a counter that += 1 every time the function is called
    // then add that to n and return
    counter = n
    return function() {
        counter += 1
        return counter
    }
}