# Galactic Cargo Management System (GCMS)

In a galaxy where interstellar shipping companies face challenges of efficiently managing cargo space, **The Galactic Cargo Management System (GCMS)** was created to optimize space cargo bin utilization on starships. This project models a large-scale cargo management system that prioritizes cargo packing based on size and special handling instructions. The system assigns bins based on different bin-packing algorithms tailored to specific types of cargo, simulating real-life constraints of space travel.

## Project Overview

The **Galactic Cargo Management System** assigns each cargo bin a unique integer ID and capacity, and each cargo item has a unique ID, size, and color designation (blue, yellow, red, or green). Each color signifies a different handling priority, which dictates the algorithm used to assign the cargo to a bin:

- **Blue Cargo**: Compact Fit, Least ID
- **Yellow Cargo**: Compact Fit, Greatest ID
- **Red Cargo**: Largest Fit, Least ID
- **Green Cargo**: Largest Fit, Greatest ID

### Core Algorithms

1. **Largest Fit Algorithm**  
   This algorithm places cargo in the bin with the largest remaining capacity.  
   - **Time Complexity**: \(O(\log(n))\) for insertion, where \(n\) is the number of bins.
  
2. **Compact Fit Algorithm**  
   This algorithm places cargo in the bin with the smallest remaining capacity that can still accommodate it.  
   - **Time Complexity**: \(O(\log(n))\) for insertion.

### Data Structures and Time Complexity

The system is designed for efficient space management, using AVL Trees to maintain a balanced structure for storing bins and objects. This ensures efficient searching, insertion, and deletion operations.

| Operation       | Time Complexity                                     |
|-----------------|-----------------------------------------------------|
| `add_bin`       | O(log(n))                                           |
| `add_object`    | O(log(n) + log(m))                                  |
| `delete_object` | O(log(n) + log(m))                                  |
| `object_info`   | O(log(n) + log(m))                                  |
| `bin_info`      | O(log(n) + S), where S is the number of objects in the bin |


### Classes and Functionalities

The system comprises several classes, each with a unique role in the cargo management process:

- **`GCMS`**: Initializes the cargo system, managing bin and object assignments.
- **`add_bin(bin_id, capacity)`**: Adds a bin to the system.
- **`add_object(object_id, size, color)`**: Assigns cargo based on size and color, reducing the bin's capacity as needed.
- **`delete_object(object_id)`**: Removes a cargo item, freeing up bin capacity.
- **`object_info(object_id)`**: Retrieves the bin ID of a specific cargo item.
- **`bin_info(bin_id)`**: Returns the remaining capacity and a list of object IDs currently stored in the bin.

### Constraints and Error Handling

The system is optimized with specific constraints:
- **Space Complexity**: \(O(n + m)\)
- **Time Complexity**: At most \(O(\log(n) + \log(m))\) for most operations
- **NoBinFoundException**: Raised when no bin meets the requirements for a specific cargo item.

### Testing

A comprehensive testing suite (`tester.py`) verifies the functionality of the cargo management system by simulating different scenarios:

1. **Bin Addition**: Tests adding bins of various capacities and IDs.
2. **Cargo Assignment**: Simulates assigning cargo based on different algorithms and validates expected outcomes.
3. **Capacity Management**: Ensures bins accurately reflect capacity changes as cargo is added or removed.
4. **Error Handling**: Verifies the correct exceptions are raised when appropriate.
