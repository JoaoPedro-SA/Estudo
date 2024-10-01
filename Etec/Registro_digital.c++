#include <Adafruit_Fingerprint.h>

#include <Adafruit_CircuitPlayground.h>
#include <Adafruit_Circuit_Playground.h>


#include <SoftwareSerial.h>
const int ledPino1 = 12;
int contador_loop = 0;
int counter;

uint8_t id;

uint8_t getFingerprintEnroll();

SoftwareSerial mySerial(2, 3); // Pino 2 como entrada do sensor (fio Verde)
                               // Pino 3 como saída do sendor (fio Branco)
Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);

void setup(){
   pinMode(13, OUTPUT);
   pinMode(ledPino1, OUTPUT);
  Serial.begin(9600);
  Serial.println("Procurando Leitor Biometrico ...");

  finger.begin(57600);   // Define a taxa de dados para a porta serial do sensor

  if (finger.verifyPassword()) {
    Serial.println("Leitor Biometrico encontrado");
  }
  else {
    Serial.println("Leitor Biometrico nao encontrado");
    while (1);
  }
}

uint8_t readnumber(void) {
  uint8_t num = 0;
  boolean validnum = false;
  while (1) {
    while (! Serial.available());
    char c = Serial.read();
    if (isdigit(c)) {
      num *= 10;
      num += c - '0';
      validnum = true;
    } else if (validnum) {
      return num;
    }
  }
}

void loop()   {
  digitalWrite(ledPino1, HIGH);
  delay(500);

  Serial.println("Pronto para Cadastrar Dados! Indique o ID# o qual deve ser salvo");
  id = readnumber();
  Serial.print("Inscrever ID#");
  Serial.println(id);

  while (!  getFingerprintEnroll() );
}

uint8_t getFingerprintEnroll() {

  int p = -1;
  Serial.print("Esperando digital para inscrever #");
  Serial.println(id);
  while (p != FINGERPRINT_OK) {
    p = finger.getImage();
    switch (p) {
      case FINGERPRINT_OK:
        Serial.println("Imagem Capturada");
        break;
      case FINGERPRINT_NOFINGER:
        Serial.println(".");
        break;
      case FINGERPRINT_PACKETRECIEVEERR:
        Serial.println("Erro ao se Comunicar");
        break;
      case FINGERPRINT_IMAGEFAIL:
        Serial.println("Erro ao Capturar Imagem");
        break;
      default:
        Serial.println("Erro Desconhecido");
        break;
    }
  }

  // OK success!

  p = finger.image2Tz(1);
  switch (p) {
    case FINGERPRINT_OK:
      Serial.println("Imagem convertida");
      break;
    case FINGERPRINT_IMAGEMESS:
      Serial.println("Imagem muito Confusa");
      return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("Erro ao se Comunicar");
      return p;
    case FINGERPRINT_FEATUREFAIL:
      Serial.println("Impossivel encontrar caracteristicas da digital");
      return p;
    case FINGERPRINT_INVALIDIMAGE:
      Serial.println("Impossível encontrar características da digital");
      return p;
    default:
      Serial.println("Erro Desconhecido");
      return p;
  }

  Serial.println("Retire o dedo");
  delay(2000);
  p = 0;
  while (p != FINGERPRINT_NOFINGER) {
    p = finger.getImage();
  }
  Serial.print("ID ");
  Serial.println(id);
  p = -1;
  Serial.println("Coloque o mesmo dedo novamente");
  while (p != FINGERPRINT_OK) {
    p = finger.getImage();
    switch (p) {
      case FINGERPRINT_OK:
        Serial.println("Imagem Capturada");
        break;
      case FINGERPRINT_NOFINGER:
        Serial.print(".");
        break;
      case FINGERPRINT_PACKETRECIEVEERR:
        Serial.println("Erro ao se Comunicar");
        break;
      case FINGERPRINT_IMAGEFAIL:
        Serial.println("Erro ao Capturar Imagem");
        break;
      default:
        Serial.println("Erro Desconhecido");
        break;
    }
  }

  // OK success!

  p = finger.image2Tz(2);
  switch (p) {
    case FINGERPRINT_OK:
      Serial.println("Imagem Convertida");
      break;
    case FINGERPRINT_IMAGEMESS:
      Serial.println("Imagem muito Confusa");
      return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("Erro ao se comunicar");
      return p;
    case FINGERPRINT_FEATUREFAIL:
      Serial.println("Nao foi possível encontrar características da impressao digital");
      return p;
    case FINGERPRINT_INVALIDIMAGE:
      Serial.println("Nao foi possível encontrar características da impressao digital");
      return p;
    default:
      Serial.println("Erro Desconhecido");
      return p;
  }

  // OK converted!
  Serial.print("Criando cadastro para #");
  Serial.println(id);

  p = finger.createModel();
  if (p == FINGERPRINT_OK) {
    Serial.println("Digital Combinada");
  } 
  else if (p == FINGERPRINT_PACKETRECIEVEERR) {
    Serial.println("Erro ao se Comunicar");
    return p;
  } 
  else if (p == FINGERPRINT_ENROLLMISMATCH) {
    Serial.println("Digital nao corresponde");
    return p;
  } 
  else {
    Serial.println("Erro Desconhecido");
    return p;
  }

  Serial.print("ID ");
  Serial.println(id);
  p = finger.storeModel(id);
  if (p == FINGERPRINT_OK) {
    Serial.println("Armazenado!");
  } 
  else if (p == FINGERPRINT_PACKETRECIEVEERR) {
    Serial.println("Erro ao se Comunicar");
    return p;
  } 
  else if (p == FINGERPRINT_BADLOCATION) {
    Serial.println("Impossível Armazenar Dados");
    return p;
  } 
  else if (p == FINGERPRINT_FLASHERR) {
    Serial.println("Erro ao salvar na memoria");
    return p;
  } 
  else {
    Serial.println("Erro Desconhecido");
    return p;
  }

  // Incrementa o contador
  contador_loop++;

  // Imprime o valor do contador
  Serial.print("Quantidade de registrados no sistema = ");
  Serial.println(contador_loop);

  // Verifica se o contador atingiu o limite
  if (contador_loop >= 100) {
    // Emite um alerta
    Serial.println("Limite atingido!");
  }

   for (counter = 0; counter < 3; ++counter) {
    digitalWrite(13, HIGH);
    tone(5,523, 1000); // play tone 60 (C5 = 523 Hz)
    delay(1000); // Wait for 1000 millisecond(s)
    digitalWrite(13, LOW);
    delay(1000); // Wait for 1000 millisecond(s)
   }
  
  // Desliga o primeiro LED
  digitalWrite(ledPino1, LOW);
  delay(1000);

}