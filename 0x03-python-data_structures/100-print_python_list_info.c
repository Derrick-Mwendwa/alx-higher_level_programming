#include <Python.h>

/**
 * print_python_list_info - prints info about Python lists
 * @p: PyObject list
 * 
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int len, alloc, i;
	PyObject *object;

	len = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", len);
	
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < len; i++)
	{
		printf("Element %d: ", i);
		object = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
