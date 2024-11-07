def main():
    graph = [[-1] * 50 for _ in range(50)]
    nn = int(input("Enter Number of Nodes: "))
    
    
    for i in range(nn):
        for j in range(nn):
            graph[i][j] = -1

    
    ch = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    
    for i in range(nn):
        for j in range(nn):
            if i == j:
                graph[i][j] = 0
            if graph[i][j] == -1:
                t = int(input(f"Enter Distance between {ch[i]} - {ch[j]}: "))
                graph[i][j] = graph[j][i] = t

    via = [[-1] * 50 for _ in range(50)]
    
    
    print("\nAfter Initialization")
    for i in range(nn):
        print(f"\n{ch[i]} Table")
        print("Node\tDist\tVia")
        for j in range(nn):
            print(f"{ch[j]}\t{graph[i][j]}\t{via[i][j]}")

    
    sh = [[[-1] * 50 for _ in range(50)] for _ in range(50)]
    for i in range(nn):
        for j in range(nn):
            for k in range(nn):
               
                if graph[i][j] > -1 and graph[j][k] > -1:
                    sh[i][j][k] = graph[j][k] + graph[i][j]
                else:
                    sh[i][j][k] = -1

   
    for i in range(nn):
        print(f"\n\nFor {ch[i]}")
        for j in range(nn):
            print(f"\nFrom {ch[j]}")
            for k in range(nn):
                print(f" {ch[k]} {sh[i][j][k]}")


    final = [[-1] * 50 for _ in range(50)]
    for i in range(nn):
        for j in range(nn):
            final[i][j] = graph[i][j]
            via[i][j] = i
            
           
            for k in range(nn):
                if (final[i][j] > sh[i][k][j]) or (final[i][j] == -1):
                    if sh[i][k][j] > -1:
                        final[i][j] = sh[i][k][j]
                        via[i][j] = k

            
            if final[i][j] == -1:
                for k in range(nn):
                    if final[i][k] != -1 and final[k][j] != -1:
                        if (final[i][j] == -1) or (final[i][j] > final[i][k] + final[k][j]):
                            if final[i][k] + final[k][j] > -1:
                                final[i][j] = final[i][k] + final[k][j]
                                via[i][j] = k


    print("\nAfter Update:")
    for i in range(nn):
        print(f"\n{ch[i]} Table")
        print("Node\tDist\tVia")
        for j in range(nn):
            via_node = '-' if i == via[i][j] else ch[via[i][j]]
            print(f"{ch[j]}\t{final[i][j]}\t{via_node}")

if __name__ == "__main__":
    main()