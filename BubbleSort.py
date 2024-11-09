
import unittest

def bubble_sort(arr):
    
    if not isinstance(arr, list):
        raise TypeError("Invalid")
    for element in arr:
        if not isinstance(element, (int, float)):
            raise ValueError("Error")
    
    for n in range(len(arr) - 1, 0, -1):
        swapped = False
        
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True  
        if not swapped:  
            break
    return arr
        
   
class TestBubbleSort(unittest.TestCase):
    
    def test_positive(self):
        self.assertEqual(bubble_sort([50,13,7,23,19,21,22]), [7,13,19,21,22,23,50])
        
    def test_negative(self):
        with self.assertRaises(TypeError):
            bubble_sort("Error")
        with self.assertRaises(ValueError):
            bubble_sort([2, "three", 4])      
    
    def test_performance(self):
        large_array = list(range(1000,0,-1))
        sorted_array = list(range(1,1001))
        self.assertEqual(bubble_sort(large_array), sorted_array)
        
    def test_boundary(self):
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(bubble_sort([19,19,19]), [19,19,19])
        self.assertEqual(bubble_sort([10,11,12,13,14,15]), [10,11,12,13,14,15])
        self.assertEqual(bubble_sort([15,14,13,12,11,10]), [10,11,12,13,14,15])
        
    def test_idempotency(self):
        arr = [19,24,23,22,21,20]
        sorted_once = bubble_sort(arr.copy())
        sorted_twice = bubble_sort(sorted_once.copy())
        self.assertEqual(sorted_once, sorted_twice)
        
if __name__ == "__main__":
    unittest.main()
