import pickle
import pandas as pd
from typing import List, Callable, Any, Union

def rlen(x: List, y: int = 0) -> range:
    """
    Returns a range object from 0 to the length of the list x plus y.
    """
    return range(len(x) + y)

def printi(x: List, y: Any = None) -> None:
    """
    Prints each element in the list x. If y is provided, it prints y after each element.
    """
    for i in x:
        print(i, y) if y is not None else print(i)

def readdataset(file: Union[str, List], func: Callable = None) -> Any:
    """
    Reads a dataset from a file or list. Optionally applies a function to the dataset.
    """
    if isinstance(file, str):
        with open(file, 'r') as f:
            x = f.readlines()
    elif isinstance(file, list):
        x = file
    else:
        raise TypeError("file must be a string or a list")
    
    return func(x) if func else x

def readdatasets(filename: str, func: Callable = None) -> Any:
    """
    Reads the entire content of a file. Optionally applies a function to the content.
    """
    with open(filename, 'r') as file:
        z = file.read()
    return func(z) if func else z

def prod(*elements: Union[float, List[float]]) -> float:
    """
    Calculates the product of a list of numbers, ignoring zeros.
    """
    if isinstance(elements[0], list):
        elements = elements[0]
    return float(pd.Series([i for i in elements if i != 0.0]).prod())

def rms(*elements: Union[float, List[float]]) -> float:
    """
    Calculates the root mean square of a list of numbers.
    """
    if isinstance(elements[0], list):
        elements = elements[0]
    result = ((1/len(elements)) * sum(i**2 for i in elements))**0.5
    print(result)
    return result

def throw() -> None:
    """
    Raises an exception for debugging purposes.
    """
    raise Exception("Debug")

def dump(x: Any, name: str) -> None:
    """
    Dumps an object to a file using pickle.
    """
    with open(name, "wb") as f:
        pickle.dump(x, f)

def load(name: str) -> Any:
    """
    Loads an object from a pickle file.
    """
    with open(name, "rb") as f:
        return pickle.load(f)

def loadpd(name: str) -> pd.DataFrame:
    """
    Loads a pandas DataFrame from a pickle file.
    """
    return pd.read_pickle(name)

def tslice(flist: List[List], column: int) -> List:
    """
    Extracts a column from a list of lists.
    """
    return [i[column] for i in flist]

flatten = lambda t: [item for sublist in t for item in sublist]
"""
Flattens a list of lists into a single list.
"""

def xor(hex_string: str) -> str:
    """
    Perform XOR operation on two halves of a hex string.
    
    Args:
        hex_string (str): The input hexadecimal string.
    
    Returns:
        str: The result of XOR operation as a hexadecimal string.
    """
    length = len(hex_string) // 2
    first_half = int(hex_string[:length], 16)
    second_half = int(hex_string[length:], 16)
    return hex(first_half ^ second_half)[2:].zfill(length)

def digit(x: float) -> int:
    """
    Returns the number of digits before the decimal point in x. If x is less than 1, returns the negative number of leading zeros.
    """
    if x == 0:
        return 0
    if x >= 1:
        return len(str(int(x)))
    i = 0
    while x < 1:
        x *= 10
        i += 1
    return -i
