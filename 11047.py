"""
백준 11047 문제 : 동전 0
problem : https://www.acmicpc.net/problem/11047
"""
import sys

if __name__ == "__main__":
    line = list(map(int, sys.stdin.readline().strip().split()))
 
    m = 0
    coin_list = []
    for i in range(line[0]):
        coin_list.append(int(input()))
    
    coin_list.reverse()
    for coin in coin_list:
        m += line[1] // coin
        line[1] = line[1] % coin
        
    print(m)
