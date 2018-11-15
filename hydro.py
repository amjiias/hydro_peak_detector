#!/usr/bin/env python

import unittest


def peak_detect(data, k):
    """
    Detects 10 highest peaks of time series 'data'. A peak is detected
    when 'k' values before and 'k' values after the data point are smaller.
    
    """
    assert len(data) >= k * 2 + 1
    
    peaks = []
    b = 0
    for i in range(len(data) - k * 2):
      
        idx = i + k
        cnt = True
                
        for j in range(i, i + k):
            if data[idx] <= data[j]:
                cnt = False
                break
        if cnt:
            for j in range(i + k + 1, i + 2 * k + 1): 
                if data[idx] <= data[j]:
                    cnt = False
                    break
        if cnt:  
            peaks.append(data[idx])
            # Store only 10 highest peaks
            peaks.sort(reverse=True)
            if len(peaks) > 10:
                peaks.pop()            
    return peaks


class Test(unittest.TestCase):
    
    def test1(self):
        peaks = peak_detect([0,0,0,0,0,1,0,0,0,0,0], 5)
        self.assertEqual(1, len(peaks))
        self.assertEqual(1, peaks[0])

    def test2(self):
        peaks = peak_detect([0,0,0,0,0,1,4,3,7,12,25,44,45,23,17,8,6,6,4,0,0,0,0,0], 7)
        self.assertEqual(1, len(peaks))
        self.assertEqual(45, peaks[0])
        
    def test3(self):
        """
        Tests the ability to limit number of returned peaks to 10
        """
        peaks = peak_detect([0,0,11,0,0,10,0,0,9,0,0,8,0,0,7,0,0,6,0,0,5,0,0,4,0,0,3,0,0,2,0,0,1,0,0], 2)
        self.assertEqual(10, len(peaks))
        self.assertEqual(11, peaks[0])
        

if __name__ == "__main__":
    unittest.main()