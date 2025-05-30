# BalanceApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getBalanceApiV1BalanceGet**](#getbalanceapiv1balanceget) | **GET** /api/v1/balance | Get Balance|

# **getBalanceApiV1BalanceGet**
> BalanceResponse getBalanceApiV1BalanceGet()


### Example

```typescript
import {
    BalanceApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new BalanceApi(configuration);

let ano: number; //Ano para consulta (default to undefined)

const { status, data } = await apiInstance.getBalanceApiV1BalanceGet(
    ano
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **ano** | [**number**] | Ano para consulta | defaults to undefined|


### Return type

**BalanceResponse**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

