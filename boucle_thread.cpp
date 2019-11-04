#include <Python.h>
#include <iostream>
#include <list>
#include <math.h>    
#include <thread>

void task1();
std::list<double> L;

static PyObject* boucle(PyObject* self, PyObject* args) {

	
	std::thread t1(task1);
	std::thread t2(task1);
	std::thread t3(task1);
	std::thread t4(task1);

	t1.join();
	t2.join();
	t3.join();
	t4.join();
	

	PyObject * python_val = Py_BuildValue("f", fs.count());
	return python_val;
}

void task1() {
	int iteration = 1000000;
	for (int i = 0; i < iteration/4; i++) {
		L.push_back(i);
	}
}

static PyMethodDef methods[] = {
		{ "boucle",(PyCFunction)boucle, METH_VARARGS,
		"Generate random number betweeen 0-9" },
		{ NULL, NULL, 0, NULL }
};

static struct PyModuleDef myModule4 =
{
	PyModuleDef_HEAD_INIT, "myModule4", "", -1, methods
};

PyMODINIT_FUNC PyInit_myModule4(void)
{
	return PyModule_Create(&myModule4);
}