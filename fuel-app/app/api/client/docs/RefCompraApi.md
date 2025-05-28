# RefCompraApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**listarRefCompraApiV1RefCompraGet**](#listarrefcompraapiv1refcompraget) | **GET** /api/v1/ref_compra | Listar Ref Compra|

# **listarRefCompraApiV1RefCompraGet**
> Array<PrecoCompra> listarRefCompraApiV1RefCompraGet()


### Example

```typescript
import {
    RefCompraApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new RefCompraApi(configuration);

let combustivelId: number; // (optional) (default to undefined)
let mes: number; // (optional) (default to undefined)

const { status, data } = await apiInstance.listarRefCompraApiV1RefCompraGet(
    combustivelId,
    mes
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **combustivelId** | [**number**] |  | (optional) defaults to undefined|
| **mes** | [**number**] |  | (optional) defaults to undefined|


### Return type

**Array<PrecoCompra>**

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

