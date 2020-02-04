from typing import Generator, Tuple


def extract_version_parts(v: str) -> Generator[Tuple[str, bool], None, None]:
    """
    Yields the next version part, also an integer type indicator.
    A version part is a sequence of alnum characters until the next non alnum character.
    For example: 123.12-1 has three parts (123, 12, 1).
    :param v: String version value.
    :return: Generator of version parts with its int indicator (1 if it is, 0 otherwise)
    """
    if v is not None:
        numeric = True
        i = 0
        for j in range(len(v) + 1):
            if j < len(v) and v[j].isalpha():
                numeric = False
            if j == len(v) or not v[j].isalnum():
                if i < j:
                    yield v[i:j], numeric
                    numeric = True
                i = j + 1


def compare_versions(va: str, vb: str) -> int:
    """
    Indicates which of the two versions values is greater.
    Time Complexity: O(n), n is the number of characters in the version values.
    Space Complexity: O(n), n is the number of characters in the actual version parts.
    :param va: String version value.
    :param vb: String version value.
    :return: 0 if both versions are equal. -1 if va is greater, otherwise 1.
    """
    if va is None and vb is None:
        return 0
    elif va is None:
        return 1
    elif vb is None:
        return -1
    vapg = extract_version_parts(va)
    vbpg = extract_version_parts(vb)
    for vap, vbp in zip(vapg, vbpg):
        if vap[0] == vbp[0]:
            continue
        if vap[1] and vbp[1]:
            return -1 if int(vap[0]) > int(vbp[0]) else 1
        else:
            return -1 if vap[0] > vbp[0] else 1
    if len(va) != len(vb):
        return -1 if len(va) > len(vb) else 1
    return 0
