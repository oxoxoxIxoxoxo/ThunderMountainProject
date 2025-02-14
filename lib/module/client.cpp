#include "client.hpp"
#include <iostream>

Client::Client(const std::string& address)
    : context(1), socket(context, ZMQ_SUB) {
    socket.connect(address);
    socket.set(zmq::sockopt::subscribe, "");  // Subscribe to all messages
}

void Client::receive_message() {
    zmq::message_t message;
    (void)socket.recv(message, zmq::recv_flags::none);  // Ignore the return value
    std::string msg(static_cast<char*>(message.data()), message.size());
    std::cout << "Received: " << msg << std::endl;
}
