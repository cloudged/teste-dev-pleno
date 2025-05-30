# CombustiveisApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getCombustiveisApiV1CombustiveisGet**](#getcombustiveisapiv1combustiveisget) | **GET** /api/v1/combustiveis | Get Combustiveis|

# **getCombustiveisApiV1CombustiveisGet**
> Array<CombustivelResponse> getCombustiveisApiV1CombustiveisGet()


### Example

```typescript
import {
    CombustiveisApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new CombustiveisApi(configuration);

const { status, data } = await apiInstance.getCombustiveisApiV1CombustiveisGet();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<CombustivelResponse>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

