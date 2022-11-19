def swap_count(kyul):
   pos = sorted(list(enumerate(kyul)), key=lambda x: x[1])
   times_swapped = 0

   for index in range(len(kyul)):
      while True:
         if (pos[index][0] == index):
            break
         else:
            times_swapped += 1
            swap_index = pos[index][0]
            pos[index], pos[swap_index] = pos[swap_index], pos[index]

   return times_swapped

def solution(kyul):
   return min(swap_count(kyul), swap_count(kyul[::-1]))