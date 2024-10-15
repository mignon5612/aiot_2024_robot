cmake_minimum_required(VERSION 3.0)
project(helloOpenCV)

find_package(OpenCV REQUIRED)
file(GLOB SOURCES "*.cpp")

foreach(SOURCES ${SOURCES})
    get_filename_component(EXE_NAME ${SOURCES} NAME_WE)
    add_executable(${EXE_NAME} ${SOURCES})
    target_link_libraries(${EXE_NAME} ${OpenCV_LIBS})
    target_link_directories(${EXE_NAME} PUBLIC ${OpenCV_LIB_DIR})
endforeach()

# add_executable(main helloOpenCV.cpp)
# target_link_libraries(main ${OpenCV_LIBS})
# target_link_directories(main PUBLIC ${OpenCV_LIB_DIR})

# add_executable(mainclass mainclass.cpp)
# target_link_libraries(mainclass ${OpenCV_LIBS})
# target_link_directories(mainclass PUBLIC ${OpenCV_LIB_DIR})
