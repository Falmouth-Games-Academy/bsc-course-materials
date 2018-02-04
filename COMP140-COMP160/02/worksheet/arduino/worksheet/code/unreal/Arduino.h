// Fill out your copyright notice in the Description page of Project Settings.

#pragma once


#define ARDUINO_WAIT_TIME 2000

#include "GameFramework/Actor.h"
#include "Arduino.generated.h"

UCLASS()
class ARDUINOEXAMPLE_API AArduino : public AActor
{
	GENERATED_BODY()
private:
	//Serial comm handler
	HANDLE hSerial;
	//Connection status
	bool connected;
	//Get various information about the connection
	COMSTAT status;

	unsigned long int *errors;
	
	void connect(wchar_t *portName);


public:	
	// Sets default values for this actor's properties
	AArduino();

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;
	
	// Called every frame
	virtual void Tick( float DeltaSeconds ) override;

	//Read data in a buffer, if nbChar is greater than the
	//maximum number of bytes available, it will return only the
	//bytes available. The function return -1 when nothing could
	//be read, the number of bytes actually read.
	unsigned long int ReadData(char *buffer, unsigned int nbChar);
	//Writes data from a buffer through the Serial connection
	//return true on success.

	bool WriteData(char *buffer, unsigned int nbChar);
	//Check if we are actually connected
	bool IsConnected();

	virtual void EndPlay(const EEndPlayReason::Type EndPlayReason) override;



	
};
