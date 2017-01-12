
# PEP 526: Syntax for variable annotations (Type Hints)

# This is not running code. Just shows some syntax.

from typing import ClassVar

# Type hints available for module-level
module_level = 'generic string'  #type: str

class Bludger:
    # Instance vars with or without initialization
    instvar: int
    valvar = 'hello'  #type: str

    dfl = 'initialized string'  #type: str
    # ClassVars
    clsvar: ClassVar = 3.14 #type: float



    def whack(self):
        # Type hints for local vars with initialization
        local = 42   #type: int
        ins_local: str  #Uninitialized string value



