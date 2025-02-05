def validate_callout(lines: list[str])->bool:
    in_callout = False
    config_lines: list[str] = []
    for line in lines:
        line = line.strip()
        if line == '```callout':
            in_callout = True
            config_lines = []
            continue
        if in_callout:
            if line == '----':
                in_callout = False # configの終わりではなく、configの区切りと解釈
                if not config_lines:
                    continue # 設定行がない場合は次のcalloutを探す
                config = {}
                for config_line in config_lines:
                    if ':' not in config_line:
                        continue # key-value形式でない行は無視する
                    key, value = config_line.split(':', 1)
                    config[key.strip()] = value.strip()

                if 'title' in config and 'icon' in config and len(config) == 2:
                    return True # 有効なcalloutが見つかったらTrueを返す
                config_lines = [] # reset config_lines for the next callout block
                continue
            if line == '```':
                in_callout = False # calloutブロック全体の終わり
                config_lines = [] # calloutが終わるのでconfig_linesをリセット
                continue
            config_lines.append(line)
    return False # 有効なcalloutブロックが見つからなかった
