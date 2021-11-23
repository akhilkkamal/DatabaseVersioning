from logging.config import fileConfig
from lib.util.ini_handler import load_parm_config
from copy import copy
from alembic import context
from alembic.config import Config

def alembic_config_builder(_context: context,_config: Config) -> Config:
    runtime_args = _context.get_x_argument(as_dictionary=True)
    fileConfig(_config.config_file_name)

    runtime_args_unwind = load_unwind_runtime_args(runtime_args)
    _runtime_args_unwind = runtime_args_unwind.copy() # don't want our alembic parm dict to impact the config dict needed for revisions
    _runtime_args_unwind.pop("original_alembic_sections", None)

    for _key in _runtime_args_unwind:
        _config.set_main_option(_key, _runtime_args_unwind[_key])
    return _config

def load_unwind_runtime_args(_runtime_args: dict) -> dict:
    ret_dict = {}
    ret_dict['original_alembic_sections'] = {}
    parm_config_list = ['parm_config']
    for p in parm_config_list:
        _parm_config = _runtime_args.get(p)
        ret_dict[p] = _parm_config
        ini_load = load_parm_config(_parm_config)
        _parm_config_keys = ini_load[0]
        ret_dict['original_alembic_sections'] = {**ret_dict['original_alembic_sections'], **ini_load[1]}

        for _key in _parm_config_keys:
            ret_dict[_key] = _parm_config_keys[_key]
    return ret_dict
