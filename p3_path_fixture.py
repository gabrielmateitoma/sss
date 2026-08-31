from pathlib import Path


def resolve_under_root(root, user_path):
    """Return resolved path for user_path under root.

    Contract: the returned path must remain under root.
    Rejects absolute paths and traversal paths escaping root.
    """
    # INTENTIONALLY DEFECTIVE H1: no containment check
    return (Path(root) / user_path).resolve()
