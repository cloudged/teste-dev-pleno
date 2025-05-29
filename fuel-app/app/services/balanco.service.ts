import {
    BalancoApi,
    BalancoConsultaResponse,
    Configuration,
  } from '../api/client/index';
  
  const configuration = new Configuration({
    basePath:  process.env.NEXT_PUBLIC_API_BASE_URL,
  });
  
  const api = new BalancoApi(configuration);
  
  export const BalancoService = {
    async getBalancos(): Promise<BalancoConsultaResponse> {
      const response = await api.obterBalancoApiV1BalancoGet(2024);
      return response.data;
    },
  };