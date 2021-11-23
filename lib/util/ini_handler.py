import configparser
import json
from typing import Tuple


def load_parm_config(_parm_config: str) -> Tuple[dict, dict]:
    c = configparser.ConfigParser()
    c.optionxform = str  # Preserve casing
    c.read(_parm_config)

    ret_dict = {}
    sections_raw = json.loads(json.dumps(c._sections))

    for _section in c.sections():
        for _key in c[_section]:
            ret_dict[_key] = c[_section][_key]
    return ret_dict, sections_raw