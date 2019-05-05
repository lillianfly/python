import sys
class _const:
    class ConstError(TypeError):pass
    class ConstCaseError(ConstError):pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("can not rebind const (%s)" % name)
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise self.ConstError("can not unbind const (%s)" % name)
        raise NameError(name)

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.name
        else:
            return None

sys.modules[__name__] = _const()
import const
const.FIRST = 1