import numpy as np
from juliacall import Main as jl

class daggerjl:
    is_initialized = False

    @staticmethod
    def init():
        if daggerjl.is_initialized:
            return
        jl.seval("using Dagger, PythonCall")
        daggerjl.is_initialized = True

    @staticmethod
    def spawn(func, *args):
        daggerjl.init()

        # Create a Julia function from the Python function
        julia_func = jl.PythonCall.pyfunc(func)

        # Call Dagger.spawn with the converted arguments, and return the `DTask` object
        #return jl.Dagger.spawn(julia_func, *args)
        return jl.Dagger.spawn(func, *args)

    @staticmethod
    def fetch(dtask):
        daggerjl.init()

        # Fetch the `DTask` result
        return jl.Dagger.fetch(dtask)

    @staticmethod
    def wait(dtask):
        daggerjl.init()

        # Wait on the `DTask` to complete
        jl.Dagger.wait(dtask)
