from pathlib import Path


def resolve_under_root(root, user_path):
    """Resolve user_path under root.

    Contract: the returned resolved path must remain under root. Absolute paths
    or traversal paths that escape root must be rejected by raising ValueError.
    """
    return (Path(root) / user_path).resolve()
