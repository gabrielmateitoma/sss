from pathlib import Path


def resolve_under_root(root, user_path):
    """Resolve user_path under root.

    Contract: the returned resolved path must remain under root. Absolute paths
    or traversal paths that escape root must be rejected by raising ValueError.
    """
    root_path = Path(root).resolve()
    input_path = Path(user_path)
    if input_path.is_absolute():
        raise ValueError("absolute path is not allowed")
    resolved = (root_path / input_path).resolve()
    try:
        resolved.relative_to(root_path)
    except ValueError as exc:
        raise ValueError("path escapes root") from exc
    return resolved
