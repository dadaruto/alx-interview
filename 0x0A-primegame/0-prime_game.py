#!/usr/bin/python3
"""Prime game module.
"""
def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    # Determine the maximum value in nums to sieve primes up to that number
    max_num = max(nums)
    
    # Sieve of Eratosthenes to find all primes up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p * p <= max_num:
        if sieve[p]:
            for multiple in range(p * p, max_num + 1, p):
                sieve[multiple] = False
        p += 1

    primes = [num for num, is_prime in enumerate(sieve) if is_prime]

    def play_game(n):
        remaining = list(range(1, n + 1))
        current_player = 0  # Maria starts (0 for Maria, 1 for Ben)

        while any(sieve[num] for num in remaining):
            for prime in primes:
                if prime > n:
                    break
                if prime in remaining:
                    # Remove prime and its multiples
                    remaining = [num for num in remaining if num % prime != 0]
                    current_player = 1 - current_player  # Switch player
                    break

        # Return the winner of this game (0 for Maria, 1 for Ben)
        return 1 - current_player

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        if play_game(num) == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
