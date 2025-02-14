#ifndef PUBLISHER_HPP
#define PUBLISHER_HPP

#include <zmq.hpp>
#include <string>

class Publisher {
public:
    Publisher(const std::string& address);
    void send_message(const std::string& message);

private:
    zmq::context_t context;
    zmq::socket_t socket;
};

#endif // PUBLISHER_HPP
