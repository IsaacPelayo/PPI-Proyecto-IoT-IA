#include <WiFi.h>

const char* ssid = "Nombre_de_tu_Red_WiFi";
const char* password = "Contrase�a_de_tu_Red_WiFi";

const char* host = "192.168.1.100"; // Direcci�n IP de tu dispositivo m�vil
const int port = 80; // Puerto para la comunicaci�n

void setup() {
  Serial.begin(115200);
  connectToWiFi();
}

void loop() {
  // Leer datos del sensor de humedad del suelo
  int moistureLevel = analogRead(A0);
  
  // Enviar datos al servidor (dispositivo m�vil)
  sendDataToServer(moistureLevel);
  
  delay(1000); // Espera 1 segundo antes de volver a leer el sensor
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

void sendDataToServer(int data) {
  WiFiClient client;
  if (!client.connect(host, port)) {
    Serial.println("Connection failed");
    return;
  }

  Serial.println("Connected to server");

  // Env�a los datos al servidor
  client.print("GET /data=");
  client.print(data);
  client.println(" HTTP/1.1");
  client.print("Host: ");
  client.println(host);
  client.println("Connection: close");
  client.println();
}

