import random
import time

# Implement bubble_sort function.
# Repeated compares adjacent items, switches them based order, bubbling the largest item to the end of the list
# Ensure it is adaptive
def bubble_sort(L):
    """Sorts L using bubble sort"""
    n = len(L)
    num_swaps = 0

    for i in range(n-1):
        made_swaps = False
        for j in range(n-1-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                made_swaps = True
                num_swaps += 1
        if not made_swaps: return num_swaps
   
    return num_swaps


# Implement insertion_sort function.
# Finds the next unsorted item and sorts it into the correct location, building the sorted list one step at a time
# Ensure it is adaptive
def insertion_sort(L):
    """Sort L using insertion sort"""
    n = len(L)
    num_swaps = 0

    for i in range(n): 
        j = n-i-1
        while j < n - 1 and L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
            num_swaps += 1
            j += 1

    return num_swaps
 

# Implement selection_sort function.
# Repeatedly finds the max value and puts it at the end of the list, which creates the sorted part of the list
# Ensure it is adaptive
def selection_sort(L):
    """Sorts L using selection sort"""
    n = len(L)
    num_swaps = 0

    for i in range(n - 1):
        i_max = 0
        for j in range(n - i):
            if L[j] > L[i_max]: 
                i_max = j
        if n-i-1 != i_max:
            num_swaps += 1

        L[n - i - 1], L[i_max] = L[i_max], L[n - i - 1]

    return num_swaps


#Feel free to write any additional functions that may be necessary 
# to populate the results required in part 2.
def is_sorted(L):
    """Checks if a list is sorted or not"""
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            return False
    return True


def random_list(n):
    """Returns a random list of size n"""
    l = [random.randint(0, 100) for n in range(n-1)]
    l.append(-1)
    return l


def sorted_list(n):
    """Returns a sorted list of size n"""
    return [i for i in range(n)]


def reversed_list(n):
    """Returns a reverse sorted list of size n"""
    return [i for i in range(n, 0, -1)]


def front_to_end_list(n):
    """Returns a sorted list of size n where 5% of the items from the front are moved to the end of the list"""
    l = sorted_list(n)
    five_percent = round(n * 0.05)

    # Add 5% of the front items to the end first
    for i in range(five_percent):
        l.append(l[i])

    # Pop the 5% of the front items after appending them to the end of the list
    for i in range(five_percent):
        l.pop(0)

    return l


def end_to_front_list(n):
    """Returns a sorted list of size n where 5% of the items from the end are moved to the front of the list"""
    l = sorted_list(n)
    five_percent = round(n * 0.05)

    # Insert the last 5% items to the beginning before popping them from the end
    for i in range(five_percent):
        l.insert(0, n-1-i)
    
    # Pop the 5% items from the end of the list
    for i in range(five_percent):
        l.pop()

    return l


def calculate_time(L, func):
    """Takes in a list and a sorting function and counts the number of swaps and the calculates the time it takes to run that sorting method"""
    start = time.time()
    swaps = func(L)
    end = time.time()
    total_time = round((end - start), 5)
    assert is_sorted(L)

    return (swaps, total_time)


def print_results(list_type, list_func):
    """Takes in a type of list and a list of n values, calculates and prints out the results for how many swaps and and how long the sorting method takes"""
    print("----------------------------------------------------------------------------------------------------------")
    
    ns = [2000, 3000, 4000, 5000, 10000]
    for n in ns:
        bub_swaps, bub_time = calculate_time(list_func(n), bubble_sort)
        insert_swaps, insert_time = calculate_time(list_func(n), insertion_sort)
        selec_swaps, selec_time = calculate_time(list_func(n), selection_sort)

        print(f"|    {list_type}    |    {n}    |    ({bub_swaps}, {bub_time})    |    ({insert_swaps}, {insert_time})    |     ({selec_swaps}, {selec_time})    |")


if __name__ == "__main__":
    # Generate the table
    print("----------------------------------------------------------------------------------------------------------")
    print("|   Scenario   | List Size |      Bubble Sort     |      Insertion Sort      |       Selection Sort      |")
    print("----------------------------------------------------------------------------------------------------------")
    print("|              |           |      Swaps, Time     |        Swaps, Time       |        Swaps, Time        |")

    # sort a random list and print results
    print_results("Random", random_list)
    print_results("Sorted", sorted_list)
    print_results("Reverse", reversed_list)
    print_results("Move front to end", front_to_end_list)
    print_results("Move end to front", end_to_front_list)


'''
Part 3: Conclusion

Based on your performance analysis, write a conclusion that addresses the following points:

1. Provide a ranking of the sorting algorithms based on their performance in each scenario. Which sorting algorithm performed best in each case (Random, Sorted, Reverse Order, Move End to Front, Move Front to End), and why do you think it performed better?
    Random List: 
        Selection sort works the best on a random list. If we look at the number of swaps made and the running time for the selection sort method, it is clearly a lot faster and more efficient than bubble or insertion sort.
        Bubble and insertion sort seem to perform similarly on a random list as they have similar number of swaps and runtimes for each of the list sizes.
        However, on larger lists it is clear that insertion sort is faster than bubble sort.
        Selection sort works best on a random list because it is not sorted in any way. Since selection sort has to check through every single item in the list, as it looks for the largest value, if we already have a sorted list, then these checks will be irrelevant.
        However, since this list is completed random, selection sort works the fastest because this is the type of list it is made to sort efficiently with O(n^2) comparisons and O(n) writes.
        Insertion and bubble sort on the other hand require O(n^2) comparisons and O(n^2) writes, which is why they both perform slower than selection sort in this random list where it is necessary to make every comparison.

    Sorted List:
        All lists work the same in the sense that they make no swaps on a list that is already sorted.
        However, if we look at the run times, we can see that selection sort performs the worst, while bubble and insertion sort have similar runtimes.
        Even on every large lists, bubble and insertion sort perform at less than a second, however bubble sort is faster than insertion sort.
        Bubble sort is the fastest on a sorted list because bubble sort has the ability to terminate early if it traverses through a list without making any swaps.
        Insertion and selection sorts are slower than bubble sort because they still have to check through the list and make comparisons, even though the list is already sorted.

    Reversed List:
        Selection sort is the fastest as it makes the least number of swaps and performs at the fastest runtime.
        Bubble and insertion sort make the same number of swaps, but bubble sort performs faster than insertion sort.
        Similar to why selection sort worked the best on a random list, a reversed list is kind of like a random list because none of the items are in order.
        So, since selection sort works best on a random list, it makes sense for why it also works the best on a reveresed list.
        Bubble sort is faster than insertion sort due to the short-circuiting ability of the sorting method, which insertion sort does not have.

    Front to End List:
        Selection sort makes the least number of swaps, but it is the second fastest.
        Insertion sort is the fastest while bubble sort is the slowest, even though they both make the same number of swaps.
        Insertion sort is the fastest because only the end of the list is unsorted, and since insertion sort finds the next sorted item and puts it in its correct location, it is easy to do that when all the unsorted items are at the end.
        However, bubble sort is the slowest because the largest items have to bubble to the end of the list, so it would end up rewriting EVERYTHING in order to bring the smallest values to the front of the list again.

    End to Front List:
        The number of swaps in this list is the same as in the front to end list for all the sorting methods.
        However, bubble sort is the fastest, followed by insertion sort and then selection sort.
        Bubble sort is the fastest because it bubbles the largest items to the end of the list. Since 5% of the largest items are in the beginning of the list, bubble sort would simply bubble them to the end, make one last check over the whole list and short-circuit once it recognizes that the list is sorted.
        Insertion sort is the second fastest because it has to find the next unsorted item and insert it down to the correct position. Since the 95% of the terms at the end would be considered "unsorted" since the 5% of the largest terms are in the front, insertion sort would have to rewrite all of those terms, which takes more time.
        Selection sort is the slowest because it has to repeated find the max value, which are in the beginning of the list at the start of the sorting process, but once they are all at the end of the list, selection sort doesn't have a way of short-circuiting, so it takes longer.

2. Explain how the number of swaps made by each algorithm affects both efficiency and time complexity across different scenarios.
    The number of swaps made by each algorithm affects the time complexity across different secnarios because the more swaps you have to make, the longer it takes to sort the list.
    In bubble sort, for example, you are making a lot of swaps, which usually takes longer, as shown in the data below. 
    However, if you have a list that is almost sorted, it takes at best only O(n) to run bubble sort because it simply checks through each item to ensure that it is sorted.
    Insertion sort also makes around the same number of swaps as bubble sort does, but it is a lot faster in most cases because it has the ability to account for rabbits and turtles at a faster speed than bubble sort does.
    Selection sort, however, does not have the short-circuiting feature of bubble sort or the rabbit/turtle feature of insertion sort, which is why selection sort works the slowest on lists that are partially sorted and fastest on lists that are random or reversed.
    As for the efiiciency of each algorithm based on the number of swaps, selection sort does seem to be the most efficent as it makes the least number of swaps.
    However, this doesn't mean that lower number of swaps equates to faster running time. As shown on the table below, there are several instances where selection sort is the slowest, even if it makes the same number of swaps or even a smaller number of swaps than the other two algorithms.
    This is most likely due to the fact that selection sort does not have a short-circuiting feature and it must make O(n^2) comparisons even it its best case.


3. Discuss the impact of the initial order of data on how well each algorithm performs. Explain why some algorithms perform differently on sorted, reversed, or random lists.
        The initial order of the list matters a lot when choosing the right sorting algorithm. 
        If you were to have a list that was fully sorted, bubble sort is the best bet because of its ability to terminate early.
        If you had a list that was reversed or random, both of which feature ONLY items that are not in the right order, selection sort is the best algorithm as it avoids excessive swaps throughout the method.
        If you had a list that was partially sorted, we need to determine if we have a rabbit or a turtle. 
        Rabbits are big items at the beginning of a list, such as the case with the list where 5% of the end items are moved to the front of the list.
        These type of lists work best with bubble sort because they would just bubble to the end very quickly. 
        On the other hand, lists with turtles, small items at the end of the list such as in the front to end list, work best with insertion sort because those items would easily get inserted into the beginning of the list.
        Bubble sort works the worst for a list with turtles because it would have to bubble up all the larger items to the end of the list instead of just bringing that one small item to the beginning fo the list like insertion sort would.
        Selection sort works the worst for these cases of partially sorted lists because it still has to make the O(n^2) comparisons since it cannot short-circuit.

'''

'''
Include the results table here:
----------------------------------------------------------------------------------------------------------
|   Scenario   | List Size |      Bubble Sort     |      Insertion Sort      |       Selection Sort      |
----------------------------------------------------------------------------------------------------------
|              |           |      Swaps, Time     |        Swaps, Time       |        Swaps, Time        |
----------------------------------------------------------------------------------------------------------
|    Random    |    2000    |    (941100, 0.39657)    |    (999091, 0.23906)    |     (1992, 0.10547)    |
|    Random    |    3000    |    (2199231, 0.63067)    |    (2229427, 0.49996)    |     (2994, 0.22817)    |
|    Random    |    4000    |    (3954426, 1.11028)    |    (3891530, 0.87071)    |     (3993, 0.41695)    |
|    Random    |    5000    |    (6261053, 1.75022)    |    (6297940, 1.4168)    |     (4994, 0.6551)    |
|    Random    |    10000    |    (24970716, 7.09909)    |    (24715316, 5.60762)    |     (9994, 2.64258)    |
----------------------------------------------------------------------------------------------------------
|    Sorted    |    2000    |    (0, 0.00016)    |    (0, 0.00032)    |     (0, 0.11928)    |
|    Sorted    |    3000    |    (0, 0.00025)    |    (0, 0.00048)    |     (0, 0.26002)    |
|    Sorted    |    4000    |    (0, 0.00032)    |    (0, 0.00064)    |     (0, 0.46305)    |
|    Sorted    |    5000    |    (0, 0.0004)    |    (0, 0.00081)    |     (0, 0.72716)    |
|    Sorted    |    10000    |    (0, 0.00077)    |    (0, 0.00165)    |     (0, 2.9051)    |
----------------------------------------------------------------------------------------------------------
|    Reverse    |    2000    |    (1999000, 0.37676)    |    (1999000, 0.44722)    |     (1000, 0.10922)    |
|    Reverse    |    3000    |    (4498500, 0.86498)    |    (4498500, 1.03512)    |     (1500, 0.24601)    |
|    Reverse    |    4000    |    (7998000, 1.54614)    |    (7998000, 1.80741)    |     (2000, 0.44004)    |
|    Reverse    |    5000    |    (12497500, 2.4123)    |    (12497500, 2.86006)    |     (2500, 0.68588)    |
|    Reverse    |    10000    |    (49995000, 9.87565)    |    (49995000, 11.30085)    |     (5000, 2.77897)    |
----------------------------------------------------------------------------------------------------------
|    Move front to end    |    2000    |    (190000, 0.17154)    |    (190000, 0.04168)    |     (1900, 0.11008)    |
|    Move front to end    |    3000    |    (427500, 0.3892)    |    (427500, 0.09568)    |     (2850, 0.25398)    |
|    Move front to end    |    4000    |    (760000, 0.69709)    |    (760000, 0.17026)    |     (3800, 0.45087)    |
|    Move front to end    |    5000    |    (1187500, 1.08791)    |    (1187500, 0.2647)    |     (4750, 0.70381)    |
|    Move front to end    |    10000    |    (4750000, 4.48537)    |    (4750000, 1.06175)    |     (9500, 2.88532)    |
----------------------------------------------------------------------------------------------------------
|    Move end to front    |    2000    |    (190000, 0.04061)    |    (190000, 0.04321)    |     (1900, 0.10132)    |
|    Move end to front    |    3000    |    (427500, 0.08681)    |    (427500, 0.09771)    |     (2850, 0.23509)    |
|    Move end to front    |    4000    |    (760000, 0.1513)    |    (760000, 0.17578)    |     (3800, 0.42683)    |
|    Move end to front    |    5000    |    (1187500, 0.23689)    |    (1187500, 0.26636)    |     (4750, 0.65196)    |
|    Move end to front    |    10000    |    (4750000, 0.97729)    |    (4750000, 1.08827)    |     (9500, 2.79008)    |
'''
