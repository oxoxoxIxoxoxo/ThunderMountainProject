#ifndef CLIENT_HPP
#define CLIENT_HPP

#include <zmq.hpp>
#include <string>

class Client {
public:
    Client(const std::string& address);
    void receive_message();

private:
    zmq::context_t context;
    zmq::socket_t socket;
};

#endif // CLIENT_HPP
