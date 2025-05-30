import {
    OrdersApi,
    OrderCreate,
    OrderResponse,
    Configuration,
  } from '../api/client/index';

   
  const configuration = new Configuration({
    basePath: process.env.NEXT_PUBLIC_API_BASE_URL,
  });

    const api = new OrdersApi(configuration);

    export const OperacoesService = {
        async postOperation(payload: OrderCreate): Promise<OrderResponse> {
          const response = await api.createNewOrderApiV1OrderPost(payload);
          return response.data;
        },
      };