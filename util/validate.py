import yaml


def validate_callout_config(config_lines: list[str]) -> str | None:
    config = yaml.safe_load("\n".join(config_lines))
    if not isinstance(config, dict):
        return "Callout config must be a YAML dictionary"
    if "title" not in config or "icon" not in config:
        return "Callout config must contain a type field"
    return None


def validate_callout(lines: list[str]) -> str | None:
    is_callout = False
    callout_config_lines: list[str] = []
    is_config = False
    for i, line in enumerate(lines):
        if is_callout:
            if line.strip() == "```":
                if is_config:
                    return f"Callout config block not closed at line {i}"
                is_callout = False
            elif is_config:
                if line.strip().startswith("----"):
                    is_config = False
                    validate_res = validate_callout_config(callout_config_lines)
                    if validate_res is not None:
                        return f"Invalid callout config at line {i}: {validate_res}"
                    callout_config_lines = []
                else:
                    callout_config_lines.append(line)
            elif line.strip().startswith("----"):
                is_config = True
        elif line.startswith("```callout"):
            is_callout = True
    return None
