from dataclasses import dataclass, field
from savitrigen.guideline import (
    check_module_naming,
    check_field_naming
)

@dataclass
class Module(object):
    fields:dict

    unicon:str = ''
    route:bool = False
    report:bool = False
    presets:list = None

    """Those below are unused"""
    documentation:str = 'undocumented'
    translation:dict = None

@dataclass
class Field(object):
    label:str
    type:str

    description:str = None

    required:bool = False
    readonly:bool = False
    values:list = None


@dataclass
class BackendConfig(object):
    entities:dict
    _entities:dict = field(init=False, repr=False)

    plugins:list[str] = None

    @property
    def entities(self) -> dict:
        return self._entities

    @entities.setter
    def entities(self, value:dict) -> None:
        ms = dict()

        for k, v in value.items():
            ms[k] = module = Module(**v)
            check_module_naming(k)

            for f_k, f_v in module.fields.items():
                module.fields[f_k] = Field(**f_v).__dict__
                check_field_naming(f_k)

        self._entities = ms
