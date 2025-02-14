// header.h
#ifndef HEADER_H
#define HEADER_H

#include <zmq.hpp>
#include <string>

void publisher(zmq::context_t& context);
void subscriber(zmq::context_t& context);

#endif // HEADER_H
