#include <WiFi.h>

const char* ssid = "Nombre_de_tu_Red_WiFi";
const char* password = "Contraseña_de_tu_Red_WiFi";

const int bombaPin = D1; // Pin donde está conectada la bomba de agua

WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  pinMode(bombaPin, OUTPUT);
  digitalWrite(bombaPin, LOW);
  connectToWiFi();
  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  if (client) {
    String request = client.readStringUntil('\r');
    client.flush();
    
    if (request.indexOf("/activar_riego") != -1) {
      digitalWrite(bombaPin, HIGH);
    }
    if (request.indexOf("/desactivar_riego") != -1) {
      digitalWrite(bombaPin, LOW);
    }
    
    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/html");
    client.println("");
    client.stop();
  }
}

void connectToWiFi() {
  Serial.println("Connecting to WiFi");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting...");
  }
  Serial.println("Connected to WiFi");
}


