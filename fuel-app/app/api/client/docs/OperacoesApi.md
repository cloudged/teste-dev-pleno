# OperacoesApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**criarOperacaoEndpointApiV1OperacoesPost**](#criaroperacaoendpointapiv1operacoespost) | **POST** /api/v1/operacoes | Criar Operacao Endpoint|

# **criarOperacaoEndpointApiV1OperacoesPost**
> OperacaoResponse criarOperacaoEndpointApiV1OperacoesPost(operacaoCreate)


### Example

```typescript
import {
    OperacoesApi,
    Configuration,
    OperacaoCreate
} from './api';

const configuration = new Configuration();
const apiInstance = new OperacoesApi(configuration);

let operacaoCreate: OperacaoCreate; //

const { status, data } = await apiInstance.criarOperacaoEndpointApiV1OperacoesPost(
    operacaoCreate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **operacaoCreate** | **OperacaoCreate**|  | |


### Return type

**OperacaoResponse**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

