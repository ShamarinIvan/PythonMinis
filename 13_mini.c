#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>

int is_square_matrix(PyObject* matrix, Py_ssize_t* size) {
    if (!PyList_Check(matrix)) {
        PyErr_SetString(PyExc_TypeError, "Matrix must be a list of lists");
        return 0;
    }

    Py_ssize_t n = PyList_Size(matrix);
    for (Py_ssize_t i = 0; i < n; i++) {
        PyObject* row = PyList_GetItem(matrix, i);
        if (!PyList_Check(row) || PyList_Size(row) != n) {
            PyErr_SetString(PyExc_ValueError, "Matrix must be square");
            return 0;
        }
    }
    *size = n;
    return 1;
}

void multiply_matrices(Py_ssize_t n, double result, double a, double** b) {
    for (Py_ssize_t i = 0; i < n; i++) {
        for (Py_ssize_t j = 0; j < n; j++) {
            result[i][j] = 0.0;
            for (Py_ssize_t k = 0; k < n; k++) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}

void copy_matrix(Py_ssize_t n, double dest, double src) {
    for (Py_ssize_t i = 0; i < n; i++) {
        for (Py_ssize_t j = 0; j < n; j++) {
            dest[i][j] = src[i][j];
        }
    }
}

void matrix_power(Py_ssize_t n, double result, double matrix, int power) {
    double** temp = malloc(n * sizeof(double*));
    for (Py_ssize_t i = 0; i < n; i++) {
        temp[i] = malloc(n * sizeof(double));
        for (Py_ssize_t j = 0; j < n; j++) {
            temp[i][j] = (i == j) ? 1.0 : 0.0;
        }
    }

    copy_matrix(n, result, temp);

    double** current = malloc(n * sizeof(double*));
    for (Py_ssize_t i = 0; i < n; i++) {
        current[i] = malloc(n * sizeof(double));
    }

    while (power > 0) {
        if (power % 2 == 1) {
            multiply_matrices(n, current, result, matrix);
            copy_matrix(n, result, current);
        }
        multiply_matrices(n, current, matrix, matrix);
        copy_matrix(n, matrix, current);
        power /= 2;
    }

    for (Py_ssize_t i = 0; i < n; i++) {
        free(temp[i]);
        free(current[i]);
    }
    free(temp);
    free(current);
}

static PyObject* foreign_matrix_power(PyObject* self, PyObject* args) {
    PyObject* matrix;
    int power;

    if (!PyArg_ParseTuple(args, "Oi", &matrix, &power)) {
        return NULL;
    }

    if (power < 0) {
        PyErr_SetString(PyExc_ValueError, "Power must be a non-negative integer");
        return NULL;
    }

    Py_ssize_t n;
    if (!is_square_matrix(matrix, &n)) {
        return NULL;
    }

    double** input_matrix = malloc(n * sizeof(double*));
    double** result_matrix = malloc(n * sizeof(double*));
    for (Py_ssize_t i = 0; i < n; i++) {
        input_matrix[i] = malloc(n * sizeof(double));
        result_matrix[i] = malloc(n * sizeof(double));

        PyObject* row = PyList_GetItem(matrix, i);
        for (Py_ssize_t j = 0; j < n; j++) {
            input_matrix[i][j] = PyFloat_AsDouble(PyList_GetItem(row, j));
        }
    }

    matrix_power(n, result_matrix, input_matrix, power);

    PyObject* result = PyList_New(n);
    for (Py_ssize_t i = 0; i < n; i++) {
        PyObject* row = PyList_New(n);
        for (Py_ssize_t j = 0; j < n; j++) {
            PyList_SetItem(row, j, PyFloat_FromDouble(result_matrix[i][j]));
        }
        PyList_SetItem(result, i, row);
    }

    for (Py_ssize_t i = 0; i < n; i++) {
        free(input_matrix[i]);
        free(result_matrix[i]);
    }
    free(input_matrix);
    free(result_matrix);

    return result;
}

static PyMethodDef ForeignMethods[] = {
    {"foreign_matrix_power", foreign_matrix_power, METH_VARARGS, "Raise a square matrix to a power"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef foreignmodule = {
    PyModuleDef_HEAD_INIT,
    "foreign",
    "Matrix Power Foreign Extension",
    -1,
    ForeignMethods
};

PyMODINIT_FUNC PyInit_foreign(void) {
    return PyModule_Create(&foreignmodule);
}
