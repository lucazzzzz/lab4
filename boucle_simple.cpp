#include <Python.h>
#include <iostream>
#include <list>
#include <math.h>



static PyObject* boucle(PyObject* self, PyObject* args) {

	std::list<double> L;
	int iteration = 999999;
	
	for (int i = 0; i <= iteration; i++){
		L.push_back(tanh(i));
	}
	
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