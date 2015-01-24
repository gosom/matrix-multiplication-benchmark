#include <boost/python.hpp>

namespace py = boost::python;

py::list naive_mul(const py::list& A, const py::list& B){
    py::ssize_t n = py::len(A);

    std::vector<std::vector<int>> av;
    av.reserve(n);
    std::vector<std::vector<int>> bv;
    bv.reserve(n);

    for(int i=0; i<n; ++i){
        std::vector<int> rowa;
        rowa.reserve(n);
        std::vector<int> rowb;
        rowb.reserve(n);
        for(int j=0; j<n; ++j){
            rowa.push_back(py::extract<int>(A[i][j]));
            rowb.push_back(py::extract<int>(B[i][j]));
        }
        av.push_back(rowa);
        bv.push_back(rowb);
    }

    std::vector<std::vector<int>> res;
    res.reserve(n);
    for(int i=0; i<n; ++i){
        std::vector<int> row(n);
        for(int j=0; j<n; ++j){
            for(int k=0; k<n; ++k){
                int a = av[i][k];
                int b = bv[k][j];
                row[j] += a * b;
            }
        }
        res.push_back(row);
    }

    py::list C;
    for(int i=0; i<n; ++i){
        py::list tmp;
        for(int j=0; j<n; ++j){
            tmp.append(res[i][j]);
        }
        C.append(tmp);
    }

    return C;
}

BOOST_PYTHON_MODULE(dummy_matrix_mul){
    using namespace boost::python;

    def("standardMatrixProduct", naive_mul);
}
