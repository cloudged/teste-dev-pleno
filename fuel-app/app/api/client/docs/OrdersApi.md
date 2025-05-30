# OrdersApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**createNewOrderApiV1OrderPost**](#createneworderapiv1orderpost) | **POST** /api/v1/order | Create New Order|

# **createNewOrderApiV1OrderPost**
> OrderResponse createNewOrderApiV1OrderPost(orderCreate)


### Example

```typescript
import {
    OrdersApi,
    Configuration,
    OrderCreate
} from './api';

const configuration = new Configuration();
const apiInstance = new OrdersApi(configuration);

let orderCreate: OrderCreate; //

const { status, data } = await apiInstance.createNewOrderApiV1OrderPost(
    orderCreate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **orderCreate** | **OrderCreate**|  | |


### Return type

**OrderResponse**

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

