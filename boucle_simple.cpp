#include <Python.h>
#include <iostream>
#include <list>
#include <chrono>
#include <math.h>    

int total;
static PyObject* boucle(PyObject* self, PyObject* args) {

	PyArg_ParseTuple(args, "i", &total);

	std::list<double> L;
	int iteration = 999999;
	typedef std::chrono::high_resolution_clock Time;
	typedef std::chrono::milliseconds ms;
	typedef std::chrono::duration<float> fsec;
	
	auto t0 = Time::now();
	for (int i = 0; i <= total; i++){
		L.push_back(tanh(i));
	}
	auto t1 = Time::now();

	fsec fs = t1 - t0;

	PyObject * python_val = Py_BuildValue("f", fs.count());
	return python_val;
}
static PyMethodDef methods[] = {
		{ "boucle",(PyCFunction)boucle, METH_VARARGS,
		"Generate random number betweeen 0-9" },
		{ NULL, NULL, 0, NULL }
};

static struct PyModuleDef myModule3 =
{
	PyModuleDef_HEAD_INIT, "myModule3", "", -1, methods
};

PyMODINIT_FUNC PyInit_myModule3(void)
{
	return PyModule_Create(&myModule3);
}