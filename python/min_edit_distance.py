#!-*- coding:utf-8 -*-
'''
A python implement for min edit distance
'''
# weight for insert operator
INSERT_COST = 1
# weight for delete operator
DELETE_COST = 1
def min_edit_distance(source, target):
    m = len(source)
    n = len(target)
    distance_matrix = [[0 for col in range(m+1)] for row in range(n+1)]
    distance_matrix[0][0] = 0
    for i in xrange(1,m+1):
        distance_matrix[0][i] = i * DELETE_COST
    for i in xrange(1,n+1):
        distance_matrix[i][0] = i * INSERT_COST
    for i in xrange(1,n+1):
        for j in xrange(1,m+1):
            insert_cost = distance_matrix[i-1][j] + 1
            if source[j-1] == target[i-1]:
                substitle_cost = distance_matrix[i-1][j-1]
            else:
                substitle_cost = distance_matrix[i-1][j-1] + 2
            delete_cost = distance_matrix[i][j-1] + 1
            value = min(insert_cost, min(substitle_cost, delete_cost))
            distance_matrix[i][j] = value
    return distance_matrix[n][m]
if __name__ == '__main__':
    # source:interesting target:insert
    print min_edit_distance('interesting', 'insert')

