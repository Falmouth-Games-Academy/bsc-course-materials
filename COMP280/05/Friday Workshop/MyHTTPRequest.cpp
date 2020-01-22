// Fill out your copyright notice in the Description page of Project Settings.


#include "MyHTTPRequest.h"
#include "Engine/Engine.h"

// Sets default values
AMyHTTPRequest::AMyHTTPRequest()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

}

// Called when the game starts or when spawned
void AMyHTTPRequest::BeginPlay()
{
	Super::BeginPlay();

	Http = &FHttpModule::Get();

	// You can uncomment this out for testing.
	//FRequest_Login LoginCredentials;
	//LoginCredentials.email = TEXT("asdf@asdf.com");
	//LoginCredentials.password = TEXT("asdfasdf");
	//Login(LoginCredentials);
	
}

// Called every frame
void AMyHTTPRequest::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

void AMyHTTPRequest::OnButtonPress()
{
	GEngine->AddOnScreenDebugMessage(-1, 100.0f, FColor::Red, TEXT("OnButtonPress"));

	FString ContentJsonString;
	FRequest_ScoreDetails score;
	score.name = "aaa";
	score.score = 100;

	GetJsonStringFromStruct<FRequest_ScoreDetails>(score, ContentJsonString);

	TSharedRef<IHttpRequest> Request = PostRequest("add_score", ContentJsonString);
	Request->OnProcessRequestComplete().BindUObject(this, &AMyHTTPRequest::PostScoreDetails_Response);
	Send(Request);
}


/**************************************************************************************************************************/




TSharedRef<IHttpRequest> AMyHTTPRequest::RequestWithRoute(FString Subroute) {
	TSharedRef<IHttpRequest> Request = Http->CreateRequest();
	GEngine->AddOnScreenDebugMessage(-1, 100.0f, FColor::Red, ApiBaseUrl);
	Request->SetURL(ApiBaseUrl + Subroute);
	SetRequestHeaders(Request);
	return Request;
}

void AMyHTTPRequest::SetRequestHeaders(TSharedRef<IHttpRequest>& Request) {
	Request->SetHeader(TEXT("User-Agent"), TEXT("X-UnrealEngine-Agent"));
	Request->SetHeader(TEXT("Content-Type"), TEXT("application/json"));
	Request->SetHeader(TEXT("Accepts"), TEXT("application/json"));
}

TSharedRef<IHttpRequest> AMyHTTPRequest::GetRequest(FString Subroute) {
	TSharedRef<IHttpRequest> Request = RequestWithRoute(Subroute);
	Request->SetVerb("GET");
	return Request;
}

TSharedRef<IHttpRequest> AMyHTTPRequest::PostRequest(FString Subroute, FString ContentJsonString) {
	TSharedRef<IHttpRequest> Request = RequestWithRoute(Subroute);

	GEngine->AddOnScreenDebugMessage(-1, 100.0f, FColor::Red, TEXT("POSTing") );
	GEngine->AddOnScreenDebugMessage(-1, 100.0f, FColor::Red, Subroute);
	GEngine->AddOnScreenDebugMessage(-1, 100.0f, FColor::Red, ContentJsonString);
	Request->SetVerb("POST");
	Request->SetContentAsString(ContentJsonString);
	return Request;
}

void AMyHTTPRequest::Send(TSharedRef<IHttpRequest>& Request) {
	Request->ProcessRequest();
}

bool AMyHTTPRequest::ResponseIsValid(FHttpResponsePtr Response, bool bWasSuccessful) 
{
	if (!bWasSuccessful || !Response.IsValid())
	{
		if(bWasSuccessful == false)	GEngine->AddOnScreenDebugMessage(-1, 100.0f, FColor::Red, TEXT("bWasSuccessful - false") ); 
		if(Response.IsValid() == false)	GEngine->AddOnScreenDebugMessage(-1, 100.0f, FColor::Red, TEXT("Response.isValid() - false"));

		return false;
	}

	if (EHttpResponseCodes::IsOk(Response->GetResponseCode())) return true;
	
	UE_LOG(LogTemp, Warning, TEXT("Http Response returned error code: %d"), Response->GetResponseCode());

	GEngine->AddOnScreenDebugMessage(-1, 100.0f, FColor::Red, TEXT("Http Response returned error code: %d"), Response->GetResponseCode());

	return false;
}

void AMyHTTPRequest::SetAuthorizationHash(FString Hash, TSharedRef<IHttpRequest>& Request) {
	Request->SetHeader(AuthorizationHeader, Hash);
}



/**************************************************************************************************************************/



template <typename StructType>
void AMyHTTPRequest::GetJsonStringFromStruct(StructType FilledStruct, FString& StringOutput) {
	FJsonObjectConverter::UStructToJsonObjectString(StructType::StaticStruct(), &FilledStruct, StringOutput, 0, 0);
}

template <typename StructType>
void AMyHTTPRequest::GetStructFromJsonString(FHttpResponsePtr Response, StructType& StructOutput) {
	StructType StructData;
	FString JsonString = Response->GetContentAsString();
	FJsonObjectConverter::JsonObjectStringToUStruct<StructType>(JsonString, &StructOutput, 0, 0);
}



/**************************************************************************************************************************/



void AMyHTTPRequest::Login(FRequest_Login LoginCredentials) {
	FString ContentJsonString;
	GetJsonStringFromStruct<FRequest_Login>(LoginCredentials, ContentJsonString);

	TSharedRef<IHttpRequest> Request = PostRequest("user/login", ContentJsonString);
	Request->OnProcessRequestComplete().BindUObject(this, &AMyHTTPRequest::LoginResponse);
	Send(Request);
}

void AMyHTTPRequest::LoginResponse(FHttpRequestPtr Request, FHttpResponsePtr Response, bool bWasSuccessful) 
{
	if (!ResponseIsValid(Response, bWasSuccessful))
	{
		GEngine->AddOnScreenDebugMessage(-1, 100.0f, FColor::Red, TEXT("LoginResponse-FAIL"));

		//return;
	}
	FResponse_Login LoginResponse;
	GetStructFromJsonString<FResponse_Login>(Response, LoginResponse);

	UE_LOG(LogTemp, Warning, TEXT("Id is: %d"), LoginResponse.id);
	UE_LOG(LogTemp, Warning, TEXT("Name is: %s"), *LoginResponse.name);
}

void AMyHTTPRequest::PostScoreDetails_Response(FHttpRequestPtr Request, FHttpResponsePtr Response, bool bWasSuccessful)
{
	if (!ResponseIsValid(Response, bWasSuccessful))
	{
		GEngine->AddOnScreenDebugMessage(-1, 100.0f, FColor::Red, TEXT("PostScoreDetails_Response-FAIL"));

		return;
	}

	GEngine->AddOnScreenDebugMessage(-1, 100.0f, FColor::White, TEXT("PostScoreDetails_Response-SUCCESS"));

	FResponse_Login LoginResponse;
	GetStructFromJsonString<FResponse_Login>(Response, LoginResponse);

	UE_LOG(LogTemp, Warning, TEXT("Id is: %d"), LoginResponse.id);
	UE_LOG(LogTemp, Warning, TEXT("Name is: %s"), *LoginResponse.name);
}

void AMyHTTPRequest::GetScores_Response(FHttpRequestPtr Request, FHttpResponsePtr Response, bool bWasSuccessful)
{
	if (!ResponseIsValid(Response, bWasSuccessful))
	{
		GEngine->AddOnScreenDebugMessage(-1, 100.0f, FColor::Red, TEXT("GetScores_Response-FAIL"));

		return;
	}

	GEngine->AddOnScreenDebugMessage(-1, 100.0f, FColor::White, TEXT("GetScores_Response-SUCCESS"));

	FString rawJson = Response->GetContentAsString();
	
	GEngine->AddOnScreenDebugMessage(-1, 100.0f, FColor::White, rawJson);

	FResponse_ScoreDetails result;
	FJsonObjectConverter::JsonObjectStringToUStruct<FResponse_ScoreDetails >(Response->GetContentAsString(), &result, 0, 0);

	for (int32 Index = 0; Index != result.details.Num(); ++Index)
	{
		FString JoinedStr;
		JoinedStr += FString::FromInt(Index);
		JoinedStr += TEXT(" ");
		JoinedStr += result.details[Index].name;
		JoinedStr += TEXT(" ");
		JoinedStr += FString::FromInt(result.details[Index].score);

		GEngine->AddOnScreenDebugMessage(-1, 100.0f, FColor::Yellow, JoinedStr);
	}
		
}



void AMyHTTPRequest::OnAddScoreButtonPress()
{
	GEngine->AddOnScreenDebugMessage(-1, 100.0f, FColor::Blue, TEXT("OnAddScoreButtonPress"));

	FString ContentJsonString;
	FRequest_ScoreDetails score;
	score.name = "aaa";
	score.score = 100;

	GetJsonStringFromStruct<FRequest_ScoreDetails>(score, ContentJsonString);

	TSharedRef<IHttpRequest> Request = PostRequest("add_score", ContentJsonString);
	Request->OnProcessRequestComplete().BindUObject(this, &AMyHTTPRequest::PostScoreDetails_Response);
	Send(Request);
}

void AMyHTTPRequest::OnGetScoresButtonPress()
{
	GEngine->AddOnScreenDebugMessage(-1, 100.0f, FColor::Green, TEXT("OnGetScoresButtonPress"));

	TSharedRef<IHttpRequest> Request = GetRequest("get_scores");
	Request->OnProcessRequestComplete().BindUObject(this, &AMyHTTPRequest::GetScores_Response);
	Send(Request);
}