# BalancoApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**obterBalancoApiV1BalancoGet**](#obterbalancoapiv1balancoget) | **GET** /api/v1/balanco | Obter Balanco|

# **obterBalancoApiV1BalancoGet**
> BalancoConsultaResponse obterBalancoApiV1BalancoGet()


### Example

```typescript
import {
    BalancoApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new BalancoApi(configuration);

let ano: number; //Ano para consulta (default to undefined)

const { status, data } = await apiInstance.obterBalancoApiV1BalancoGet(
    ano
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **ano** | [**number**] | Ano para consulta | defaults to undefined|


### Return type

**BalancoConsultaResponse**

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

