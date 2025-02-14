#include "publisher.hpp"
#include <iostream>

Publisher::Publisher(const std::string& address)
    : context(1), socket(context, ZMQ_PUB) {
    socket.bind(address);
}

void Publisher::send_message(const std::string& message) {
    zmq::message_t zmq_message(message.size());
    memcpy(zmq_message.data(), message.c_str(), message.size());
    socket.send(zmq_message, zmq::send_flags::none);
    std::cout << "Sent: " << message << std::endl;
}
