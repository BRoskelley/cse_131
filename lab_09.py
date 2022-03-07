# 1. Name:
#      Brighton Roskelley
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      this program takes a list of variables and sorts them into alphbetical or numeric order.
# 4. What was the hardest part? Be as specific as possible.
#      I had a bit if difficulty getting the combine function to work properly
# 5. How long did it take for you to complete the assignment?
#      this assignment took me about 1.5 hours.


def sort(array):
    size = len(array)
    src = array
    des = [0]*size
    num = 2

    while num > 1:
        num = 0
        begin1 = 0 
        while begin1 < size:
            end1 = begin1+1

            while end1 < size and src[end1-1] <= src[end1]:
                end1 += 1
            
            begin2 = end1
            if begin2 < size:
                end2 = begin2 + 1
            else:
                end2 = begin2
            while end2 < size and src[end2-1 ] <= src[end2]:
                end2 += 1
            
            num += 1
            combine(src, des, begin1, begin2, end2)
            begin1 = end2
            
        src,des = des,src


    return src

def combine(src, des, begin1, begin2, end2):
    end1 = begin2

    for i in range(begin1,end2):
        if begin1 < end1 and (begin2 == end2 or src[begin1] < src[begin2]):
            des[i] = src[begin1]
            begin1 += 1
        else:
            des[i] = src[begin2]
            begin2 += 1
    return des



array1 = ["b","a"]
array2 = []
array3 = [2,1]
array4 = [2]
array5 = [2,2]
array6 = [2,1,5,3,4]

assert sort(array1) == ["a","b"] , print('string case failed')
print('string case worked')
assert sort(array2) == [] , print('empty case failed')
print('empty case works')
assert sort(array3) == [1,2] , print('small list case failed')
print('small list case works')
assert sort(array4) == [2] , print('single element case failed')
print('single element case works')
assert sort(array5) == [2,2] , print('duplicate number string case failed')
print('duplicate number string case works')
assert sort(array6) == [1,2,3,4,5] , print('long list case failed')
print('long list case works')