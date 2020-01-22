// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Runtime/Online/HTTP/Public/Http.h"
#include "Json.h"
#include "JsonUtilities.h"


#include "MyHTTPRequest.generated.h"

USTRUCT()
struct FRequest_Login {
	GENERATED_BODY()
		UPROPERTY() FString email;
	UPROPERTY() FString password;

	FRequest_Login() {}
};

USTRUCT()
struct FResponse_Login {
	GENERATED_BODY()
		UPROPERTY() int id;
	UPROPERTY() FString name;
	UPROPERTY() FString hash;

	FResponse_Login() {}
};

USTRUCT()
struct FRequest_ScoreDetails {
	GENERATED_BODY()
	UPROPERTY() FString name;
	UPROPERTY() int score;

	FRequest_ScoreDetails() {}
};

USTRUCT()
struct FResponse_ScoreDetails {
	GENERATED_BODY()
	UPROPERTY() TArray< FRequest_ScoreDetails> details;
	
	FResponse_ScoreDetails() {}
};


UCLASS(Blueprintable, hideCategories = (Rendering, Replication, Input, Actor, "Actor Tick"))
class TEST00_API AMyHTTPRequest : public AActor
{
	GENERATED_BODY()

private:
	FHttpModule* Http;
	FString ApiBaseUrl = "http://localhost:8000/";

	FString AuthorizationHeader = TEXT("Authorization");
	void SetAuthorizationHash(FString Hash, TSharedRef<IHttpRequest>& Request);

	TSharedRef<IHttpRequest> RequestWithRoute(FString Subroute);
	void SetRequestHeaders(TSharedRef<IHttpRequest>& Request);

	TSharedRef<IHttpRequest> GetRequest(FString Subroute);
	TSharedRef<IHttpRequest> PostRequest(FString Subroute, FString ContentJsonString);
	void Send(TSharedRef<IHttpRequest>& Request);

	bool ResponseIsValid(FHttpResponsePtr Response, bool bWasSuccessful);

	template <typename StructType>
	void GetJsonStringFromStruct(StructType FilledStruct, FString& StringOutput);
	template <typename StructType>
	void GetStructFromJsonString(FHttpResponsePtr Response, StructType& StructOutput);
	
public:	
	// Sets default values for this actor's properties
	AMyHTTPRequest();

	UFUNCTION(BlueprintCallable, Category="AMyHTTPRequest")
	void OnButtonPress();

	UFUNCTION(BlueprintCallable, Category = "AMyHTTPRequest")
	void OnAddScoreButtonPress();

	UFUNCTION(BlueprintCallable, Category = "AMyHTTPRequest")
	void OnGetScoresButtonPress();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;
	
	void PostScoreDetails_Response(FHttpRequestPtr Request, FHttpResponsePtr Response, bool bWasSuccessful);
	void GetScores_Response(FHttpRequestPtr Request, FHttpResponsePtr Response, bool bWasSuccessful);

};
