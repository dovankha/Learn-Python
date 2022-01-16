def parameter_type(p1, p2, *args, k, **kwargs):
    print("Positional or keyword {}....{}".format(p1, p2))
    print("Var-positional: {}".format(args))
    print("Keyword: {}".format(k))
    print("Var-Keyword: {}".format(kwargs))


# các loại đối số của hàm. k là khoá, khi gọi k lại thì biến vẫn là k
parameter_type(1, 2, 3, 4, 5, 6, k=5, jasf=3, kadfadfey1=8)
