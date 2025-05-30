# OrderCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fuel_id** | **number** | ID do combustível | [default to undefined]
**tipo** | **string** | Tipo da operação: compra ou venda | [default to undefined]
**data** | **string** | Data da operação | [default to undefined]
**litros** | **number** | Quantidade de litros | [default to undefined]
**selic** | **number** | Valor do selic aplicado | [default to undefined]

## Example

```typescript
import { OrderCreate } from './api';

const instance: OrderCreate = {
    fuel_id,
    tipo,
    data,
    litros,
    selic,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
