import marshal
import types
import dis
with open("Trojan_test1.pyc", "rb") as f:
    f.read(16)
    code = marshal.load(f)
def dump(co):
    print(f"\n===== {co.co_name} =====")
    dis.dis(co)

    for const in co.co_consts:
        if isinstance(const, types.CodeType):
            dump(const)
dump(code)