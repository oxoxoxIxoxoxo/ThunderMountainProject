#include "publisher.hpp"
#include "client.hpp"
#include <thread>

int main() {
    // Publisher setup
    Publisher publisher("tcp://*:5555");

    // Client setup
    Client client("tcp://localhost:5555");

    // Run publisher in a separate thread to continuously send messages
    std::thread publisher_thread([&publisher]() {
        while (true) {
            publisher.send_message("Hello");
            std::this_thread::sleep_for(std::chrono::seconds(1));  // Sleep for a second before sending the next message
        }
    });

    // Run client in the main thread to receive messages
    while (true) {
        client.receive_message();
    }

    publisher_thread.join();  // Join publisher thread to avoid abrupt termination
    return 0;
}
