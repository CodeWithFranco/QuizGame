#include "blinkAllColorFast.h"
#include "blinkAllColorNeo.h"
#include "dimmingFast.h"
#include "dimmingNeo.h"
#include <SoftwareSerial.h>  // Include SoftwareSerial library for HC-05/HC-06

SoftwareSerial SerialBT;

String command = "";
int brightness = 255;
String chipset = "";

void setup() {
    Serial.begin(115200);          // Start serial monitor (optional)
    SerialBT.begin("ESP32_ELE");   //Bluetooth name
    Serial.printIn("Bluetooth started. Ready to connect");
}

void loop() {
    if (SerialBT.available()) {
        char received = SerialBT.read();  // Read one character from Bluetooth
        if (received == '\n') {
            processCommand(command);  // Process the command once a newline character is received
            command = "";             // Clear the command after processing
        } else {
            command += received;      // Build the command string one character at a time
        }
    }
}

void processCommand(String cmd) {
    if (cmd == "R") {
        setColor("RED");  // Set LEDs to red
    } else if (cmd == "G") {
        setColor("GREEN");  // Set LEDs to green
    } else if (cmd == "B") {
        setColor("BLUE");  // Set LEDs to blue
    } else if (cmd == "W") {
        setColor("WHITE");  // Set LEDs to white
    } else if (cmd.startsWith("BRIGHTNESS=")) {
        brightness = cmd.substring(11).toInt();  // Extract brightness level
        setBrightness(brightness);  // Adjust brightness level
    }
}

void setColor(String color) {
    if (color == "RED") {
        // Assuming you have a function to set color in blinkAllColorFast.h or blinkAllColorNeo.h
        setLEDColor(255, 0, 0);  // Set to Red
    } else if (color == "GREEN") {
        setLEDColor(0, 255, 0);  // Set to Green
    } else if (color == "BLUE") {
        setLEDColor(0, 0, 255);  // Set to Blue
    } else if (color == "WHITE") {
        setLEDColor(255, 255, 255);  // Set to White
    }
}

void setBrightness(int level) {
    // Assuming you have a function in dimmingFast.h or dimmingNeo.h to set brightness
    adjustLEDBrightness(level);
}
