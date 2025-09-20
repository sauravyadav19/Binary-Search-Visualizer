#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <map>

namespace py = pybind11;

// Each step will store low, mid, high, value_at_mid, and found flag
using Step = std::map<std::string, int>;
using Steps = std::vector<Step>;

Steps binary_search(const std::vector<int>& arr, int target) {
    Steps steps;
    int low = 0, high = (int)arr.size() - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        Step step;
        step["low"] = low;
        step["high"] = high;
        step["mid"] = mid;
        step["value"] = arr[mid];
        step["found"] = (arr[mid] == target) ? 1 : 0;
        steps.push_back(step);

        if (arr[mid] == target) break;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }

    return steps;
}

PYBIND11_MODULE(binary_search_cpp, m) {
    m.doc() = "C++ Binary Search exposed to Python";
    m.def("binary_search", &binary_search, "Perform binary search and return steps");
}