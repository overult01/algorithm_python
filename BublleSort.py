# 거품정렬
# 성능 : O(n^2)

import unittest
# 단위 테스트란? - 모듈 또는 응용 프로그램 내의 개별 코드 단위가 예상대로 작동하는지 확인하는 반복 가능한 활동

def bubblesort(alist):
    for i in range(len(alist)-1):
        for j in range(len(alist)-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist

class unit_test(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], bubblesort([4, 6, 1, 3, 5, 2]))
        self.assertEqual([1, 2, 3, 4, 5, 6], bubblesort([6, 4, 3, 1, 2, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 6], bubblesort([6, 5, 4, 3, 2, 1]))