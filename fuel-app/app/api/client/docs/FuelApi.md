# FuelApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getFuelsApiV1FuelGet**](#getfuelsapiv1fuelget) | **GET** /api/v1/fuel | Get Fuels|

# **getFuelsApiV1FuelGet**
> Array<FuelResponse> getFuelsApiV1FuelGet()


### Example

```typescript
import {
    FuelApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FuelApi(configuration);

const { status, data } = await apiInstance.getFuelsApiV1FuelGet();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<FuelResponse>**

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

