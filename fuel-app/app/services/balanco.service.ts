import {
    BalanceApi,
    BalanceResponse,
    Configuration,
  } from '../api/client/index';
  
  const configuration = new Configuration({
    basePath:  process.env.NEXT_PUBLIC_API_BASE_URL,
  });
  
  const api = new BalanceApi(configuration);
  
  export const BalancoService = {
    async getBalancos(): Promise<BalanceResponse> {
      const response = await api.getBalanceApiV1BalanceGet(2024);
      return response.data;
    },
  };