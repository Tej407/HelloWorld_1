import slash


@slash.parametrize('x',[1,2,3])
def test_2(fixture,x):
    #print("fixxxxx is used")
    pass


@slash.fixture()
def used_fixture1():
    """do something"""
    print("fix1 is used")
    pass

@slash.fixture()
def used_fixture2():
    """do another thing"""
    print("fix2 is used")
    pass

@slash.use_fixtures(["used_fixture1","used_fixture2"])
def test_something1():
    assert (5-3)==28

def test_5(fixture):
    #print(fixture,"fixxx ===========> is used  <=============")
    pass


@slash.generator_fixture
def fixture():
    for x in [1,2,3]:
        #print("kk")
        yield x

@slash.fixture(scope='session')
def some_session_fixture(this):
    @this.add_cleanup
    def cleanup():
        print('Hurray! the session has ended')


@slash.fixture(scope='module')
def some_module_fixture(this):
    @this.add_cleanup
    def cleanup():
        print('Hurray! We are finished with this module')

def test_3(some_session_fixture):
    print("session is called")


def test_4(some_module_fixture):
    print("module is called")

    
#fixture parametrization
def test_5(fixture):
    print("fixxx ===========> is used  <=============")

@slash.parametrize('x',[1,2,3])
@slash.fixture
def fixture(x):
    print("kk")

#excludes the numbers given in the exclude list
num_lst=[5,10,15,20,25]
@slash.exclude('fn.num',[10,20])
def test_num(fn):
    print("Number list")
    
@slash.parametrize('num',num_lst)
@slash.fixture
def fn(num):
    print(num)

def fn3():
    f1="fn1"
    return f1
def fn4():
    f1="fn2"
    return f1
@slash.parametrize('x',[fn3(),fn4()])
def test_fn(x):
    print("param is passed")
    print(x)

def fn1():
    pass
def fn2():
    pass


@slash.parametrize('x',[slash.param('first',fn1()),slash.param('second',fn2())])
def test_fn(x):
    print("param is passed")
    


num_lst=[5,10,15,20,25,30]
@slash.parametrize('num',num_lst)
@slash.exclude('num',[10,20])
def test_num(num):
    print(num)


num_lst=[5,10,15,20,25,30]

@slash.exclude('num.n',[10,20])
def test_num(num):
    return

@slash.parametrize('n',num_lst)
@slash.fixture
def num(n):
    print(n)    

num_lst=[5,10,15,20,25,30]

@slash.exclude(('num.n','num.size'),[(10,'ten'),(20,'twenty')])
def test_fn(num):
    return

@slash.parametrize('n',num_lst)
@slash.parametrize('size',['five','ten','fifteen','twenty','thirty'])
@slash.fixture
def num(n,size):
    print(n,'---->',size)



def test_11():
    assert 4==4


def test_21():
    assert 5-3==2


def test_31():
    assert 5*3==15

def test_41():
    assert 4-2==1



def test_12():
    assert 4==4


def test_22():
    assert 5-3==2


def test_32():
    assert 5*3==15

def test_42():
    assert 4-2==1


def test_13():
    assert 4==4


def test_23():
    assert 5-3==2


def test_33():
    assert 5*3==15

def test_43():
    assert 4-2==1


def test_111():
    assert 4==4


def test_211():
    assert 5-3==2


def test_311():
    assert 5*3==15

def test_411():
    assert 4-2==1



def test_121():
    assert 4==4


def test_221():
    assert 5-3==2


def test_321():
    assert 5*3==15

def test_421():
    assert 4-2==1


def test_131():
    assert 4==4


def test_231():
    assert 5-3==2


def test_331():
    assert 5*3==15

def test_431():
    assert 4-2==1


def test_115():
    assert 4==4


def test_215():
    assert 5-3==2


def test_315():
    assert 5*3==15

def test_415():
    assert 4-2==1



def test_125():
    assert 4==4


def test_225():
    assert 5-3==2


def test_325():
    assert 5*3==15

def test_425():
    assert 4-2==1


def test_135():
    assert 4==4


def test_235():
    assert 5-3==2


def test_335():
    assert 5*3==15

def test_435():
    assert 4-2==1


def test_1115():
    assert 4==4


def test_2115():
    assert 5-3==2


def test_3115():
    assert 5*3==15

def test_4115():
    assert 4-2==1



def test_1215():
    assert 4==4


def test_2215():
    assert 5-3==2


def test_3215():
    assert 5*3==15

def test_4215():
    assert 4-2==1


def test_1315():
    assert 4==4


def test_2315():
    assert 5-3==2


def test_3315():
    assert 5*3==15

def test_4315():
    assert 4-2==1


def test_116():
    assert 4==4


def test_216():
    assert 5-3==2


def test_316():
    assert 5*3==15

def test_416():
    assert 4-2==1



def test_126():
    assert 4==4


def test_226():
    assert 5-3==2


def test_326():
    assert 5*3==15

def test_426():
    assert 4-2==1


def test_136():
    assert 4==4


def test_236():
    assert 5-3==2


def test_336():
    assert 5*3==15

def test_436():
    assert 4-2==1


def test_1116():
    assert 4==4


def test_2116():
    assert 5-3==2


def test_3116():
    assert 5*3==15

def test_4116():
    assert 4-2==1



def test_1216():
    assert 4==4


def test_2216():
    assert 5-3==2


def test_3216():
    assert 5*3==15

def test_4216():
    assert 4-2==1


def test_1316():
    assert 4==4


def test_2316():
    assert 5-3==2


def test_3316():
    assert 5*3==15

def test_4316():
    assert 4-2==1


def test_1156():
    assert 4==4


def test_2156():
    assert 5-3==2


def test_3156():
    assert 5*3==15

def test_4156():
    assert 4-2==1



def test_1256():
    assert 4==4


def test_2256():
    assert 5-3==2


def test_3256():
    assert 5*3==15

def test_4256():
    assert 4-2==1


def test_1356():
    assert 4==4


def test_2356():
    assert 5-3==2


def test_3356():
    assert 5*3==15

def test_4356():
    assert 4-2==1


def test_11156():
    assert 4==4


def test_21156():
    assert 5-3==2


def test_31156():
    assert 5*3==15

def test_41156():
    assert 4-2==1



def test_12156():
    assert 4==4


def test_22156():
    assert 5-3==2


def test_32156():
    assert 5*3==15

def test_42156():
    assert 4-2==1


def test_13156():
    assert 4==4


def test_23156():
    assert 5-3==2


def test_33156():
    assert 5*3==15

def test_43156():
    assert 4-2==1







