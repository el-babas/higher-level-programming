#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - show python list info
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
	long int i = 0;
	PyObject *py_object;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (; i < Py_SIZE(p); i++)
	{
		py_object = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(py_object)->tp_name);
	}
}
