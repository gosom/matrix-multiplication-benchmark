TEMPLATE = lib
CONFIG += plugin
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += \
    dummy_matrix_mul.cpp

QMAKE_CXXFLAGS += -std=c++11

INCLUDEPATH += /usr/include/boost /usr/include/python2.7
DEFINES += BOOST_PYTHON_DYNAMIC_LIB
LIBS += -L/usr/local/lib -L/usr/lib/python2.7 -lpython2.7 -lboost_python

QMAKE_PRE_LINK = rm -f dummy_matrix_mul.so
QMAKE_POST_LINK = ln -s libdummy_matrix_mul.so dummy_matrix_mul.so
QMAKE_DISTCLEAN += dummy_matrix_mul.so

TARGET = dummy_matrix_mul
